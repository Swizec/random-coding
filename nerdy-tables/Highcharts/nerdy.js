
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

    var person = function (name) {
        make_chart(name, name, '',
                   'Count/horniness', null,
                   [{
                       name: 'Morning',
                       data: _.map(horny_data[name].horny,
                                   function (day) { return day[0]; }),
                       lineWidth:1,
                       color:'#8e9ede',
                       type:'spline',
                       zIndex: -5
                   },
                    {
                        name: 'Evening',
                        data: _.map(horny_data[name].horny,
                                    function (day) { return day[1]; }),
                        lineWidth:1,
                        color:'#3c3',
                        type:'spline',
                        zIndex: -5
                    },
                    {
                        name: 'NHTD',
                        data: _.map(horny_data[name].horny,
                                    function (day) { return day[2]; }),
                        lineWidth:1,
                        color:'#e84157',
                        type:'spline',
                        zIndex: -5
                    },
                    {
                        name: 'Touchy',
                        data: horny_data[name].touchy,
                        lineWidth:2.2,
                        color:'#f5ebec',
                        type:'spline',
                        zIndex: -5
                    },
                    {
                        name: 'Cyber',
                        data: horny_data[name].cyber,
                        lineWidth:2.2,
                        color:'#c98f97',
                        type:'spline',
                        zIndex: -5
                    }]);
    };

    person('swizec');
    person('masa');

})(jQuery);
