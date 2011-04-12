
var redis = require('redis').createClient(),
    http = require('http');

http.createServer(function (req, res) {
    var data = '';
    req.on('data', function (chunk) { data += chunk });
    req.on('end', function () {
	var input = JSON.parse(data);

	redis.get(input.key, function (err, value) {
	    redis.set(input.key, input.value, function (err) {
		res.writeHead(200, {'Content-Type': 'application/json'});
		res.end(value);
	    });
	});
    });
}).listen(8124, '127.0.0.1');