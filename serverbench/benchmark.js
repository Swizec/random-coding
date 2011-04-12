
var http = require('http'),
    async = require('async');

var options = {
  host: 'localhost',
  port: 8124,
  path: '/',
  method: 'POST'
};

var benchmark = function (item, callback) {
    var before = (new Date()).getTime();

    var req = http.request(options, function(res) {
	res.on('end', function (chunk) {
	    callback(null, ((new Date()).getTime()-before)/1000);
	});
    });

    req.write(JSON.stringify({key: 'speed-benchmark',
			      value: before}));
    req.end();
}


var requests = [];
for (var i=0; i<512; requests.push(i++));

async.map(requests, benchmark, function (err, result) {
    async.reduce(result, 0, function (memo, item, callback) {
	callback(null, memo+item);
    }, function (err, sum) {
	console.log(sum/result.length);
    });
});