
// transition format: {from: 'q1', to: 'q2', via: 'A', put: 'B', move: 1/-1}
// spits out end word
// basic way to run:  node turing.js machine.json 111 q0 q4
// node turing.js <instructions> <word> <start> <end>

var tape = process.argv[3];
var instructions = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf-8'));
var start = process.argv[4];
var stop = process.argv[5];

var delta = function (tape, states, state, i, end) {
    if (state == end) return true;
    var cur = (tape[i]) ? states[state][tape[i]] : states[state]['eps'];
    var yes = false;

    if (cur) {
        if (cur.put != "eps") tape.splice(i, 1, cur.put);
        yes = delta(tape, states, cur.to, i+cur.move, end);
    }
    return yes;
};

var states = {};
instructions.map(function (instr) {
    states[instr.from] = states[instr.from] || {};
    states[instr.from][instr.via] = instr;
});

console.log(delta(tape.split(""), states, start, 0, stop));
