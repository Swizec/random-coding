
// transition format: {from: 'q1', to: 'q2', via: 'A', put: 'B', move: 1/-1}
// spits out whether end state was reached
// basic way to run:  node turing.js machine.json 101 q4
// node turing.js <instructions> <word> <end-state>

var _ = require('underscore'), states = {};

var delta = function (states, step, end) {
    if (_.keys(step).indexOf(end) >= 0) return true;
    var _step = {}, foo = _.keys(step).map(function (k) {
        var i = step[k][0], t = step[k][1],
            cur = (i < 0 || i >= t.length) ? states[k]['esp'] :  states[k][t[i]];
            if (cur) cur.map(function(cur) {
                if (cur.put != "eps") t.splice(i, 1, cur.put);
                _step[cur.to] = [i+cur.move, t];
            });
    });
    return (_.size(_step)) ? delta(states, _step, end) : false;
};

JSON.parse(require('fs').readFileSync(process.argv[2], 'utf-8')).map(function (i) {
    states[i.from] = states[i.from] || {};
    states[i.from][i.via] = states[i.from][i.via] || [];
    states[i.from][i.via].push(i);
});

console.log(delta(states, {"q0": [0, process.argv[3].split("")]}, process.argv[4]));
