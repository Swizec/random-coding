
var charts = [];

(function ($) {
    var make_chart = function (id, title, subtitle, yAxis, stacking, series) {
            var chart = new Highcharts.Chart({
	        chart: {
	            renderTo: id,
	            defaultSeriesType: 'area'
	        },
	        title: {
	            text: title
	        },
	        subtitle: {
	            text: subtitle
	        },
	        xAxis: {
	            type: 'linear'
	        },
	        yAxis: {
	            title: {
		        text: yAxis
	            },
	            min: 0
	        },
	        tooltip: {
	            formatter: function() {
		        return '<b>'+ this.series.name +'</b><br/>'+
		            this.x+' --> '+ this.y;
	            }
	        },
                plotOptions: {
                    series: {
                        shadow: false,
                        lineWidth:1,
                        marker: {
                            enabled: false,
                            symbol: 'circle',
                            radius: 1,
                            states: {
                                hover: {
                                    enabled: true
                                }
                            }
                        },
                        stacking: stacking
                    }
                },
	        series: series
            });

        charts.push(chart);

        return chart;
    };

    var data_func = {
        'morning': function (name) { return _.map(horny_data[name].horny,
                                                  function (day) { return day[0]; }); },
        'evening': function (name) { return _.map(horny_data[name].horny,
                                                  function (day) { return day[1]; }); },
        'NHTD': function (name) { return _.map(horny_data[name].horny,
                                               function (day) { return day[2]; }); },
        'touchy': function (name) { return horny_data[name].touchy; },
        'cyber': function (name) { return horny_data[name].cyber; }
    };

    var pair = function (name, func1, func2) {
        var id = _.toArray(arguments).join("-");
        $("body").append($("<div></div>").attr("id", id)
                                         .css({width: "800px",
                                               height: "400px",
                                               margin: "0 auto"}));
        make_chart(id, id, '',
                   'Value', null,
                   [{
                       name: func1,
                       data: data_func[func1](name),
                       lineWidth:1,
                       color:'#8e9ede',
                       type:'spline',
                       zIndex: -5
                   },
                    {
                        name: func2,
                        data: data_func[func2](name),
                        lineWidth:1,
                        color:'#3c3',
                        type:'spline',
                        zIndex: -5
                    }]);
    };

    var person = function (name) {
        // pair everything with everything
        _.map(_.map(_.map(_.range(1, _.size(data_func)),
                          function (i) {
                              return _.zip(_.map(_.range(_.size(data_func)),
                                                 function () {
                                                     return _.keys(data_func)[i-1]; }),
                                           _.rest(_.keys(data_func),
                                                  i));}),
                    function (pairs) {
                        return _.select(pairs, function (pair) {
                            return !_.include(pair, undefined);
                        });
                    }),
              function (pairs) {
                  _.map(pairs,
                        function (funcs) {
                            pair(name, funcs[0], funcs[1]);
                            });
              });
    };

    person('swizec');
    person('masa');

})(jQuery);
