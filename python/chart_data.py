################################################################################
# CHART_DATA.PY
# Generates all the highcarts JavaScript needed

################################################################################
# IMPORTS

import csv

################################################################################
# CHART 1

def chart1_data():
    '''
    Writes out data in highcharts format for Chart 1.
    '''
    seriesData = [[], [], [], [], []]
    regions = []
    years = []

    with open("./data/charts/chart1_data.csv", "r") as infile:
        data = csv.reader(infile)
        years = next(data)[1:]

        for i in seriesData:
            for row in data:
                i += [int(j) for j in row[1:]]
                regions.append(row[0].title())
                break

    return((seriesData, regions, years))

def gen_chart1_JS():
    '''
    Generates highcharts JavaScript for Chart 1.
    '''
    headings = [
    "Total Crashes By Year",
    "Number of Crashes",
    "Crashes",
     "Regions"]
    data = chart1_data()
    colors = ["852294", "ab4683", "f2964b", "ffc654"]
    js = """$(function () {
    $('#chart1').highcharts({
        title: {
            text: '%s',
        },
        xAxis: {
            categories: %s
        },
        yAxis: {
            title: {
                text: '%s'
            }
        },
        tooltip: {
            valueSuffix: ' %s',
            pointFormat: '<span style="color:{point.color}">\u25CF</span> {series.name} Suburbs: <b>{point.y}</b>'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0,
            title: {
                text: '%s'
            }
        },
        series: [{
            name: '%s',
            color: '#%s',
            data: %s,
            lineWidth: 3,
            marker: {
                radius: 5
            },
            tooltip: {
                pointFormat: '<span style="color:{point.color}">\u25CF</span> {series.name}: <b>{point.y}</b>'
            }
        },{
            name: '%s',
            color: '#%s',
            data: %s
        },{
            name: '%s',
            color: '#%s',
            data: %s
        },{
            name: '%s',
            color: '#%s',
            data: %s
        }]
    });
});
"""
    return js % (headings[0], data[2], headings[1], headings[2], headings[3],
                 data[1][0], colors[0], data[0][0], data[1][1], colors[1],
                 data[0][1], data[1][2], colors[2], data[0][2], data[1][3],
                 colors[3], data[0][3])

################################################################################
# CHART 2

def chart2_data():
    '''
    Writes out data in highcharts format for Chart 2.
    '''
    wPoints = []
    nPoints = []
    ePoints = []

    with open("./data/charts/chart2_data.csv", "r") as infile:
        data = csv.reader(infile)
        next(data)

        for row in data:
            if row[0] == "Western":
                wPoints.append([int(row[2]), int(row[1])])
            elif row[0] == "Northern":
                nPoints.append([int(row[2]), int(row[1])])
            elif row[0] == "Eastern":
                ePoints.append([int(row[2]), int(row[1])])

    return (["Northern", "Eastern", "Western"], [nPoints, ePoints, wPoints])

def gen_chart2_JS():
    '''
    Generates highcharts JavaScript for Chart 2.
    '''
    headings = [
    "Drunk Drivers vs Hit and Runs By Region",
    "Each point represents a Local Government Area (LGA)",
    "Hit and Runs",
    "Drunk Drivers",
     "Regions"]
    data = chart2_data()
    colors = [
    "rgba(133,34,148, 0.7)",
    "rgba(242,150,75,0.7)",
     "rgba(255,198,84,0.7)"]
    js = """$(function () {
    $('#chart2').highcharts({
        chart: {
            type: 'scatter',
            zoomType: 'xy'
        },
        title: {
            text: '%s',
        },
        subtitle: {
            text: '%s'
        },
        xAxis: {
            title: {
                enabled: true,
                text: '%s'
            }
        },
        yAxis: {
            title: {
                text: '%s'
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0,
            title: {
                text: '%s'
            }
        },
        plotOptions: {
            scatter: {
                marker: {
                    radius: 5,
                    states: {
                        hover: {
                            enabled : true,
                            lineColor: '#3f3f3f'
                        }
                    }
                },
                states: {
                    hover: {
                        marker: {
                            enabled: false
                        }
                    }
                },
                tooltip: {
                        headerFormat: '{series.name} Suburbs<br/>',
                        pointFormat: '<span style="color:{point.color}">\u25CF</span> <b> {point.x}</b> drunk drivers, <b>{point.y}</b> hit & runs'
                }
            }
        },
        series: [{
            name: '%s',
            color: '%s',
            data: %s
        },{
            name: '%s',
            color: '%s',
            data: %s
        },{
            name: '%s',
            color: '%s',
            data: %s
        }]
    });
});
"""
    return js % (headings[0], headings[1], headings[3], headings[2],
                 headings[4], data[0][0], colors[0], data[1][0],
                 data[0][1], colors[1], data[1][1], data[0][2],
                 colors[2], data[1][2])

################################################################################
# CHART 3

def chart3_data():
    '''
    Writes out data in highcharts format for Chart 3.
    '''
    vPoints = []
    wPoints = []
    nPoints = []
    ePoints = []
    xAxisLables = []

    with open("./data/charts/chart3_data.csv", "r") as infile:
        data = csv.reader(infile)
        next(data)

        for row in data:
            xAxisLables.append(row[0])
            vPoints.append(int(row[1]))
            nPoints.append(int(row[2]))
            ePoints.append(int(row[3]))
            wPoints.append(int(row[4]))

    return (xAxisLables, ["Victoria", "Northern", "Eastern",
            "Western"], vPoints, nPoints, ePoints, wPoints)

def gen_chart3_JS():
    '''
    Generates highcharts JavaScript for Chart 3.
    '''
    headings = [
    "Light Condition vs Fatalities",
    "Light Condition",
    "Number of Fatalities",
     "Regions"]
    data = chart3_data()
    colors = ["852294", "ab4683", "f2964b", "ffc654", "rgba(255,198,84,0.4)"]
    js = """$(function () {
    $('#chart3').highcharts({
        chart: {
            type: 'column',
            zoomType: 'xy'
        },
        title: {
            text: '%s'
        },
        xAxis: {
            categories: %s,
            crosshair: {
                color: '%s'
            },
            title: {
                text: '%s'
            }
        },
        yAxis: {
            title: {
                text: '%s'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table class="tt-table">',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y} fatalities</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
		legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0,
            title: {
                text: '%s'
            }
        },
        series: [{
            name: '%s',
            data: %s,
            color: '#%s'

        }, {
            name: '%s',
            data: %s,
            color: '#%s'

        }, {
            name: '%s',
            data: %s,
            color: '#%s'

        }, {
            name: '%s',
            data: %s,
            color: '#%s'
        }]
    });
});
"""
    return js % (headings[0], data[0], colors[4], headings[1], headings[2],
                 headings[3], data[1][0], data[2], colors[0], data[1][1],
                 data[3], colors[1], data[1][2], data[4], colors[2], data[1][3],
                 data[5], colors[3])

################################################################################
# CHART 4

def chart4_data():
    '''
    Writes out data in highcharts format for Chart 4.
    '''
    type1Points = []
    type2Points = []
    type3Points = []
    type4Points = []
    type5Points = []
    type6Points = []
    type7Points = []
    type8Points = []

    xAxisLables = []

    with open("./data/charts/chart4_data.csv", "r") as infile:
        data = csv.reader(infile)
        next(data)

        for row in data:
            xAxisLables.append(row[0])
            type1Points.append(float(row[1])*100)
            type2Points.append(float(row[2])*100)
            type3Points.append(float(row[3])*100)
            type4Points.append(float(row[4])*100)
            type5Points.append(float(row[5])*100)
            type6Points.append(float(row[6])*100)
            type7Points.append(float(row[7])*100)
            type8Points.append(float(row[8])*100)

    return (xAxisLables, ["Collision with vehicle",
                          "Collision with a fixed object",
                          "Collision with some other object",
                          "No collision and no object struck",
                          "Vehicle overturned (no collision)",
                          "Struck pedestrian", "Struck animal",
                          "Fall from or in moving vehicle"],
            type1Points, type2Points, type3Points, type4Points, type5Points,
            type6Points, type7Points, type8Points)

def gen_chart4_JS():
    '''
    Generates highcharts JavaScript for Chart 4.
    '''
    headings = [
    "Percenatge of Accident Type in Each Region",
    "Percenatge of Accident Type",
    "Accident Types", "Regions"]
    data = chart4_data()
    colors = ["852294", "AB4683", "C2343D", "AC4C47","D6694B", "F2964B", "FFC654", "FFE747", "rgba(255,198,84,0.4)"]

    for i, item in zip(range(1,4), data[0][1:]):
        data[0][i] = str(item + " Region")

    js = """$(function () {
    $('#chart4').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: '%s'
        },
        xAxis: {
            categories: %s,
            crosshair: {
                color: '%s'
            },
            title: {
                text: '%s'
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: '%s'
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0,
            title: {
                text: '%s'
            }
        },
        tooltip: {
            pointFormat: '<span style="color:{point.color}">\u25CF</span> {series.name}: <b>{point.y:.1f}%%</b>'
        },
        plotOptions: {
            column: {
                stacking: 'normal'
            }
        },
        series: [{
            name: '%s',
            data: %s,
            color: '#%s'
        }, {
            name: '%s',
            data: %s,
            color: '#%s'
        }, {
            name: '%s',
            data: %s,
            color: '#%s'
        }, {
            name: '%s',
            data: %s,
            color: '#%s'
        }, {
            name: '%s',
            data: %s,
            color: '#%s'
        }, {
            name: '%s',
            data: %s,
            color: '#%s'
        }, {
            name: '%s',
            data: %s,
            color: '#%s'
        }, {
            name: '%s',
            data: %s,
            color: '#%s'
        }]
    });
});
"""
    return js % (headings[0], data[0], colors[8], headings[3], headings[1],
                 headings[2], data[1][0], data[2], colors[0], data[1][1],
                 data[3], colors[1], data[1][2], data[4], colors[2], data[1][3],
                 data[5], colors[3], data[1][4], data[6], colors[4], data[1][5],
                 data[7], colors[5], data[1][6], data[8], colors[6], data[1][7],
                 data[9], colors[7])

################################################################################
# CHART 5

def chart5_data():
    '''
    Writes out data in highcharts format for Chart 5.
    '''
    xAxisLables = []
    vicdata = []
    ndata = []
    edata = []
    wdata = []

    with open("./data/charts/chart5_data.csv", "r") as infile:
        data = csv.reader(infile)
        next(data)

        for row in data:
            xAxisLables.append(row[0])
            if row[0] == "Victoria":
            	for i in range(1, len(row)):
            		vicdata.append(int(row[i]))
            elif row[0] == "Northern":
            	for i in range(1, len(row)):
            		ndata.append(int(row[i]))
            elif row[0] == "Eastern":
            	for i in range(1, len(row)):
            		edata.append(int(row[i]))
            if row[0] == "Western":
            	for i in range(1, len(row)):
            		wdata.append(int(row[i]))

    return (xAxisLables, vicdata, ndata, edata, wdata)

def gen_chart5_JS():
    '''
    Generates highcharts JavaScript for Chart 5.
    '''
    headings = [
    "Total Crashes On The Roads Each Hour Between 2010 - 2015",
    "Number of Crashes",
    " Crashes",
    "Time (Hours)",
    "Region",
    ['00:00','01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00',
     '08:00','09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00',
     '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']]
    colors = ["852294", "ab4683", "f2964b", "ffc654"]
    data = chart5_data()
    js = """$(function () {
    $('#chart5').highcharts({
        title: {
            text: '%s',
        },
        xAxis: {
            categories: %s,
            labels: {
                rotation: -45,
            },
            title : {
                text: '%s'
            }
        },
        yAxis: {
            title: {
                text: '%s'
            }
        },
        tooltip: {
            valueSuffix: '%s'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0,
            title: {
                text: '%s'
            }
        },
        series: [{
            name: '%s',
            data: %s,
            color: '#%s',
            lineWidth: 3,
            marker: {
                radius: 5
            }
        }, {
            name: '%s',
            data: %s,
            color: '#%s',
        }, {
            name: '%s',
            data: %s,
            color: '#%s',
        }, {
            name: '%s',
            data: %s,
            color: '#%s',
        }]
    });
});
"""
    return js % (headings[0], headings[5], headings[3], headings[1],
                 headings[2], headings[4], data[0][0], data[1], colors[0],
                 data[0][1], data[2], colors[1], data[0][2], data[3], colors[2],
                 data[0][3], data[4], colors[3])
