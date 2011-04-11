
var fs = require('fs');

var size = 1024;

/*console.log("filling stream");
var stream = fs.createWriteStream('./crap/big.txt');
for (; size>=0; size--) {
    stream.write('a');
}

console.log("closing stream");
stream.end();*/

fs.open('./crap/big.txt', 'w', function (err, fd) {
    var write = function (p) {
	if (p<size) {
	    fs.write(fd, 1, 0, 1, p, function (err, written, buffer) {
		console.log(err, written, buffer);
		write(p+1);
	    });
	}else{
	    fs.close(fd, function () {
		console.log("done writing");
	    });
	}
    }
    write(0);
});