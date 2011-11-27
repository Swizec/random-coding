
function tm(I,t,e,s,i,c,k) {i=0;while(s!=e){c=t[i];k=(c)?I[s][c]:I[s].B;if(!k)return false;t.splice(i,1,k.w);i+=k.m;s=k.n;}return t;}

// for testing purposes, run in node as:
// node turing-140.js machine-140.json 111 q5
// instructions tape endstate
console.log(tm(JSON.parse(require('fs').readFileSync(process.argv[2], 'utf-8')),
               process.argv[3].split(""),
               process.argv[4],
               "q0"));
