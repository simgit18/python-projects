from dis import dis
from click import option
import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc


df = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
df['week'] = df['Timestamp'].dt.strftime('%Y-%U')
week_average = df.groupby(["week"]).mean()

# print(week_average.head())

chart = """
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

size = 12


def charts():

    wp = jp.WebPage()
    d = jp.Div(text="HIGH CHARTS",
               style=f'font-size: {size}px; color: red text-align:center')

    disp_chart = jp.HighCharts(a=wp, options=chart)
    disp_chart.options.xAxis.categories = list(week_average.index)
    disp_chart.options.series[0].data = list(week_average['Rating'])
    wp.add(d)
    return wp


jp.justpy(charts)
