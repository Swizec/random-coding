
var async = require('async');

var isPrime = function (n, callback) {
    if (n%2 == 0) {
	callback('0');
	return;
    }else{
	var root = Math.sqrt(n);
	for (var i=3; i<=root; i += 2) {
	    if (n%i == 0) {
		callback('0');
		return;
	    }
	}
    }
    callback(1);
}

var primes = function (n, callback) {
    var acc = new Array(n);

    for (var i=2; i<n; acc[i-2] = i++);

    async.map([2, 3], 
	      function (item, callback) { callback(true); }, function (err, results) {
	console.log(err);
	console.log(results);
	callback(results);
    });
}

primes(100, function (result) {
    console.log(result);
});