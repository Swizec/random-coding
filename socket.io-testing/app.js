
/**
 * Module dependencies.
 */

var express = require('express')
  , routes = require('./routes')
  , user = require('./routes/user')
  , http = require('http')
  , path = require('path');

var app = express();

app.configure(function(){
  app.set('port', process.env.PORT || 3000);
  app.set('views', __dirname + '/views');
  app.set('view engine', 'jade');
  app.use(express.favicon());
  app.use(express.logger('dev'));
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(app.router);
  app.use(express.static(path.join(__dirname, 'public')));
});

app.configure('development', function(){
  app.use(express.errorHandler());
});

app.get('/', routes.index);

var server = exports.server = http.createServer(app).listen(app.get('port'), function(){
 // console.log("Express server listening on port " + app.get('port'));
});

var io = require('socket.io').listen(server);
io.set("log level", 0);

io.sockets.on("connection", function (socket) {
    socket.on("echo", function (msg, callback) {
        callback = callback || function () {};

        socket.emit("echo", msg);
        
        callback(null, "Done.");
    });
});
