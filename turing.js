
// transition format: {from: 'q1', to: 'q2', via: 'A', put: 'B', move: 1/-1}
// spits out whether end state was reached
// basic way to run:  node turing.js machine.json 101 q4
// node turing.js <instructions> <word> <end-state>

var _ = require('underscore'), states = {};
var stack = 0;
var STACK_OVERFLOW = 1000;

/* --- golf'd --- */

var δ=function(S,s,e){var π=_.keys,Θ={},k,i,λ,μ,ι,Σ=_.size,β,ψ;
if(π(s).indexOf(e)>=0)return!0
for(k in s){i=s[k][0],λ=s[k][1],ψ=S[k][λ[i]]||S[k].B;for(ι=0;ψ,ι<Σ(ψ);){
μ=ψ[ι++],β=_.clone(λ),β.splice(i,1,μ.w),Θ[μ.n]=[i+μ.m,β]}}return Σ(Θ)?δ(S,Θ,e):!!0};

/* --- end of golf'd --- */
/*
var δ = function(S,s,e){
    var π=_.keys,Θ={},k,i,λ,μ,ι,Σ=_.size,β,ψ;
    if(π(s).indexOf(e)>=0) return!0
    for(k in s){
        i=s[k][0],
        λ=s[k][1],
        ψ=S[k][λ[i]]||S[k].B;

        for(ι=0; ψ,ι<Σ(ψ); ){
            μ=ψ[ι++];
            β=_.clone(λ);
            β.splice(i,1,μ.w);
            Θ[μ.n]=[i+μ.m,β];
        }
    }
    return Σ(Θ)?δ(S,Θ,e):!!0;
};*/

/*JSON.parse(require('fs').readFileSync(process.argv[2], 'utf-8')).map(function (i) {
    states[i.from] = states[i.from] || {};
    states[i.from][i.via] = states[i.from][i.via] || [];
    states[i.from][i.via].push(i);
});*/

states = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf-8'));


console.log(δ(states,
              {"q0": [0, process.argv[3].split("")]},
              process.argv[4]));
