
var i = 5;

for (var i=0; i<2; i++) {
    console.log("for:"+i);
}

console.log("after:"+i);

i = 5;

for (var j=0; j<2; j++) {
    var i = j+1;
    console.log("for2:"+i);
}

console.log("after:"+i);
