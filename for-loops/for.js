
var i = 5;

for (var i=0; i<2; i++) {
    console.log("for:"+i); // prints 0, 1
}

console.log("after:"+i); // prints 2

i = 5;

for (var j=0; j<2; j++) {
    var i = j+1;
    console.log("for2:"+i); // prints 1, 2
}

console.log("after:"+i); // prints 2
