
// transition format: {from: 'q1', to: 'q2', via: 'A', put: 'B', move: 1/-1}
// spits out whether end state was reached
// basic way to run:  node turing.js machine.json 111 q0 q4
// node turing.js <instructions> <word> <start> <end>

var _ = require('underscore');

var delta = function (states, step, end) {
    if (_.keys(step).indexOf(end) >= 0) return true;
    var _step = {};
    _.keys(step).map(function (k) {
        var i = step[k][0], t = step[k][1],
            cur = (i < 0 || i >= t.length) ? states[k]['esp'] :  states[k][t[i]];
        if (cur) {
            cur.map(function(cur) {
                if (cur.put != "eps") t.splice(i, 1, cur.put);
                _step[cur.to] = [i+cur.move, t];
            });
            return true;
        }
        return false;
    });
    return (_.size(_step)) ? delta(states, _step, end) : false;
};

var states = {};
JSON.parse(require('fs').readFileSync(process.argv[2], 'utf-8')).map(function (instr) {
    states[instr.from] = states[instr.from] || {};
    states[instr.from][instr.via] = states[instr.from][instr.via] || [];
    states[instr.from][instr.via].push(instr);
});

console.log(delta(states, {"q0": [0, process.argv[3].split("")]}, process.argv[4]));
