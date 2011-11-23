
// transition format: {from: 'q1', to: 'q2', via: 'A', put: 'B', move: 1/-1}
// spits out whether end state was reached
// basic way to run:  node turing.js machine.json 111 q0 q4
// node turing.js <instructions> <word> <start> <end>

var tape = process.argv[3];
var instructions = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf-8'));
var start = process.argv[4];
var stop = process.argv[5];
var _ = require('underscore');

var delta = function (states, step, end) {
    if (_.keys(step).indexOf(end) >= 0) return true;
    var _step = {},
    yes = _.any(_.keys(step).map(function (k) {
        var i = step[k][0], t = step[k][1];
        var cur = (t[i]) ? states[k][t[i]] : states[k]['eps'];
        if (cur) {
            if (cur.put != "eps") t.splice(i, 1, cur.put);
            _step[cur.to] = [i+cur.move, t];
            return true;
        }
        return false;
    }));
    return (_step.length) ? yes || delta(states, _step, end) : false;
};

var states = {};
instructions.map(function (instr) {
    states[instr.from] = states[instr.from] || {};
    states[instr.from][instr.via] = states[instr.from][instr.via] || [];
    states[instr.from][instr.via].push(instr);
});

console.log(delta(states, {start: [0, tape.split("")]}, stop));
