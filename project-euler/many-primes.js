
var isPrime = function (n) {
    if (n%2 == 0) return false;

    var root = Math.sqrt(n);
    for (var i=3; i<=root; i += 2) {
	if (n%i == 0) return false;
    }
    
    return true;
}

var primes = function (n) {
    var acc = new Array();
    acc.push(2);

    for (var i=2; i<= n; i++) {
	if (isPrime(i)) {
	    acc.push(i);
	}
    }

    return acc;
}

console.log(primes(100000));