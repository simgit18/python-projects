from dis import dis
from click import option
import justpy as jp
from matplotlib.pyplot import figure
import pandas as pd
from datetime import datetime
from pytz import utc
from requests import options
import matplotlib.pyplot as plt


df = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
df['week'] = df['Timestamp'].dt.strftime('%Y-%U')
week_average = df.groupby(["week"]).mean()

df['month'] = df['Timestamp'].dt.strftime('%Y-%m')
month_average = df.groupby(["month", 'Course Name'])['Rating'].mean().unstack()

# month_average.plot(figsize=(25, 3))
# plt.show()

# print(week_average.head())

# SPLINE CHART"
spline_chart = """
     {
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

multi_spline_chart = """
    {
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Multi Data Spline'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

size = 12


def charts():

    wp = jp.WebPage()
    d = jp.Div(a=wp, text="SPLINE CHART",
               classes='text-center text-h3 q-pa-md')

    spline_charts = jp.HighCharts(a=wp, options=spline_chart)
    spline_charts.options.xAxis.categories = list(week_average.index)
    spline_charts.options.series[0].data = list(week_average['Rating'])

    d2 = jp.Div(a=wp, text="MULTI SPLINE CHART",
                classes='text-center text-h3 q-pa-md')
    multi_data_spline = jp.HighCharts(a=wp, options=multi_spline_chart)
    multi_data_spline.options.xAxis.categories = list(month_average.index)

    multi_spline_data = [{"name": v1, "data": [
        v2 for v2 in month_average[v1]]} for v1 in month_average.columns]

    multi_data_spline.options.series = multi_spline_data

    return wp


jp.justpy(charts)
