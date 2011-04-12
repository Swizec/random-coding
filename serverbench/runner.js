
var spawn = require('child_process').spawn,
    async = require('async');

var run = function (item, callback) {
    var bench = spawn('node', ['benchmark.js']);
    
    bench.stdin.end();

    //bench.stdout.on('data', function (data) {
	//callback(null, parseFloat((data+"").replace('\n', '')));
    //});
    var data = '';
    bench.stdout.on('data', function (chunk) {
	data += chunk;
    });

    bench.stderr.on('data', function (data) {
	console.log('stderr: ' + data);
    });

    bench.on('exit', function (code) {
	callback(null, parseFloat((data+"").replace('\n', '')));
    });
}

var benches = [];
for (var i=0; i<10; benches.push(i++));

var before = (new Date()).getTime();

async.map(benches, run, function (err, result) {
    async.reduce(result, 0, function (memo, item, callback) {
	callback(null, memo+item);
    }, function (err, sum) {
	console.log(sum/result.length);
	console.log("Total time", ((new Date()).getTime()-before)/1000);
    });
});