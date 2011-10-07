
var data = ['A', 'B', 'C', 'D'];

var _ = require('./underscore.js');

function pairs_functional(data) {
    return _.reduce(_.map(_.map(_.range(1, _.size(data)),
                      function (i) {
                          return _.zip(_.map(_.range(_.size(data)),
                                             function () {
                                                 return data[i-1]; }),
                                       _.rest(data,
                                              i));
                      }),
                function (pairs) {
                    return _.select(pairs, function (pair) {
                        return !_.include(pair, undefined);
                    });
                }),
          function (memo, pairs) {
              _.map(pairs, function (pair) {
                  memo.push(pair);
              });
              return memo;
          },[]);
}

function pairs_functional2(data) {
    return _.reduce(_.map(_.range(1, _.size(data)),
                         function (i) {
                             return _.map(_.rest(data, i),
                                          function (item) {
                                              return [data[i-1], item];
                                          });
                         }),
                   function (memo, pairs) {
                       _.map(pairs, function (pair) {
                           memo.push(pair);
                       });
                       return memo;
                   }, []);
}

function pairs_native(data) {
}

function pairs_iterative(data) {
    var out = [];
    for (var i=0; i<_.size(data); i++) {
        for (var j=i+1; j<_.size(data); j++) {
            out.push([data[i], data[j]]);
        }
    }
    return out;
}

console.log(pairs_functional(data));
console.log(pairs_iterative(data));
console.log(pairs_functional2(data));
cosnole.log(pairs_native(data));