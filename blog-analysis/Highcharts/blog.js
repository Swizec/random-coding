
var chart;

(function ($) {
    var get_date = function (i) {
        var d = analysis_data[i].date.split("-");
        return (new Date(d[0],
                         d[1]-1,
                         d[2])).toLocaleDateString();
    };

    var make_data = function (value) {
        var data = [], d;
        for (var i=0; i<analysis_data.length; i++) {
            //d = analysis_data[i].date.split("-");
            //data.push([Date.UTC(parseInt(d[0]), parseInt(d[1]), parseInt(d[2])),
            //           value(analysis_data[i])]);
            data.push([i, value(analysis_data[i])]);
        }
        return data;
    };

    chart = new Highcharts.Chart({
	chart: {
	    renderTo: 'container',
	    defaultSeriesType: 'area'
	},
	title: {
	    text: 'Word length'
	},
	subtitle: {
	    text: 'Length of words measured in syllables'
	},
	xAxis: {
	    type: 'linear'
	},
	yAxis: {
	    title: {
		text: 'Length (N of syllables)'
	    },
	    min: 0
	},
	tooltip: {
	    formatter: function() {
		return '<b>'+ this.series.name +'</b><br/>'+
		    get_date(this.x)+' --> '+ this.y;
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
                stacking:'normal'
            }
        },
	series: [{
                name: '+stand. dev.',
                data: make_data(function (item) {
                    return item.word_len[0]+item.word_len[1];
                }),
                fillOpacity:.2,
                zIndex: -5
            }, {
                name: 'Mean',
                data: make_data(function (item) {
                    return item.word_len[0];
                }),
                lineWidth:2,
                color:'#3c3',
                type:'line',
                 zIndex: -5
            }, {
                name: '-stand.dev',
                data: make_data(function (item) {
                    return item.word_len[0]-item.word_len[1];
                }),
                fillColor: 'rgba(255, 255, 255, 0)',
                zIndex: -5
            }]
    });

})(jQuery);
