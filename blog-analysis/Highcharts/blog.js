
var chart;

(function ($) {
    chart = new Highcharts.Chart({
	chart: {
	    renderTo: 'container',
	    defaultSeriesType: 'area'
	},
	title: {
	    text: 'Sentence length'
	},
	subtitle: {
	    text: 'Length of sentences in blogposts'
	},
	xAxis: {
	    type: 'datetime',
	    dateTimeLabelFormats: { // don't display the dummy year
		month: '%e. %b',
		year: '%b'
	    }
	},
	yAxis: {
	    title: {
		text: 'Length (N of words)'
	    },
	    min: 0
	},
	tooltip: {
	    formatter: function() {
		return '<b>'+ this.series.name +'</b><br/>'+
		    Highcharts.dateFormat('%e. %b', this.x) +': '+ this.y;
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
                name: 'Max',
                data: [39,28,18,16,12,23,14,15],
                fillOpacity:.2,
                zIndex: -5
            }, {
                name: 'Mean',
                data: [44,43,35,37,34,38,33,34],
                lineWidth:2,
                color:'#3c3',
                type:'line',
                 zIndex: -5
            }, {
                name: 'Min',
                data: [27,30,27,31,29,30,28,29],
                fillColor: 'rgba(255, 255, 255, 0)',
                zIndex: -5
            }]
    });

})(jQuery);
