
var spawn = require('child_process').spawn;

var N = 10000000;

var runs = function (n, i, avg) {
    var i = i || 0;
    var avg = avg || 0;

    var before = (new Date()).getTime();
    var child = spawn('node', ['many-primes.js', N], {cwd: __dirname});
    //var child = spawn('clj', ['many-primes.clj', N], {cwd: __dirname});

    child.on("exit", function (code) {
	var time = ((new Date()).getTime()-before)/1000;

	console.log(time);
	if (i < n) {
	    runs(n, i+1, avg+time);
	}else{
	    console.log(avg/n);
	}
    });
}

runs(5)