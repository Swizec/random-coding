
function tm(I,tape,end,state,i,cell,current) {
    i = 0;
    while(state != end) {
        cell = tape[i];
        current = (cell) ? I[state][cell] : I[state].B;
        if(!current)
            return false;
        tape.splice(i, 1, current.w);
        i += current.m;
        state = current.n;
    }
    return tape;
}

// for testing purposes, run in node as:
// node turing-140.js machine-140.json 111 q5
// instructions tape endstate
console.log(tm(JSON.parse(require('fs').readFileSync(process.argv[2], 'utf-8')),
               process.argv[3].split(""),
               process.argv[4],
               "q0").join(""));
