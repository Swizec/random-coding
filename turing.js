
// transition format: {from: 'q1', to: 'q2', via: 'A', put: 'B', move: 1/-1}
// needs list of instructions
// needs start and end state
// needs word
// implements delta function
// spits out end word

var tape = process.argv[3];
var instructions = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf-8'));
var start = process.argv[4];
var stop = process.argv[5];

var delta = function (tape, inst, cur, end, states) {
    states = states || {};
    // build map of states as you go (memoization of sorts)
    // perform changes on tape as per current instruction

};

console.log(delta(tape, instructions, start, stop));
