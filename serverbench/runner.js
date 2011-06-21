
var spawn = require('child_process').spawn,
    async = require('async');

var ERRORS = 0;

var run = function (item, callback) {
    var bench = spawn('node', ['benchmark.js']);
    var error = false;
    
    bench.stdin.end();

    //bench.stdout.on('data', function (data) {
	//callback(null, parseFloat((data+"").replace('\n', '')));
    //});
    var data = '';
    bench.stdout.on('data', function (chunk) {
	data += chunk;
    });

    bench.stderr.on('data', function (data) {
	ERRORS += 1;
	error = true;
    });

    bench.on('exit', function (code) {
	if (!error) {
	    callback(null, parseFloat((data+"").replace('\n', '')));
	}else{
	    callback(null, 10);
	}
    });
}

var once = function (n, counter) {
    var counter = counter || 1;

    var benches = [];
    for (var i=0; i<n; benches.push(i++));

    ERRORS = 0;

    var before = (new Date()).getTime();
    
    async.map(benches, run, function (err, result) {
	async.reduce(result, 0, function (memo, item, callback) {
	    callback(null, memo+item);
	}, function (err, sum) {
	    console.log('N:', counter, 'Err:', ERRORS, 'Avg:', sum/result.length, 'Total: ', ((new Date()).getTime()-before)/1000);

	    if (counter < n) { 
		setTimeout(function () {
		    once(n, counter+1);
		}, 2000);
	    }
	});
    });
}

once(10);