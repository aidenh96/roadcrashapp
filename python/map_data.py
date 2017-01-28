################################################################################
# MAP_DATA.PY
# Creates teh JavaScript needed for HighMaps.

################################################################################
# IMPORTS

import csv
from collections import defaultdict

################################################################################
# MAP DATA GENERATOR

def map_data(dataAttr, rangeAttr, aggType, yearAttr="", yRange1="", yRange2=""):

    years = ["2010", "2011", "2012", "2013", "2014", "2015"]

    if aggType == "total":

        if str(rangeAttr) == "yrSingle":
            jsonOut = []

            with open("./data/map/lga_map_data_" + str(yearAttr) + ".csv", "r") as infile:

                data = csv.reader(infile)
                next(data)

                for row in data:
                    innerDict = {}
                    innerDict["lga"] = (row[0]).upper().replace("_", " ")
                    innerDict["value"] = int(row[dataAttr])

                    jsonOut.append(innerDict)

        if str(rangeAttr) == "yrMulti":
            yr1Index = years.index(yRange1)
            yr2Index = years.index(yRange2)

            jsonOut = []
            lgaCount = defaultdict(int)

            for year in years[yr1Index:yr2Index + 1]:

                with open("./data/map/lga_map_data_" + year + ".csv", "r") as infile:
                    data = csv.reader(infile)
                    next(data)

                    for row in data:
                        lgaCount[(row[0]).upper().replace("_", " ")] += int(row[dataAttr])

            for key, value in lgaCount.iteritems():
                innerDict = {}
                innerDict["lga"] = key
                innerDict["value"] = value

                jsonOut.append(innerDict)

    elif aggType == "percent":
        totalCount = 0.0

        # Single Year Count
        if str(rangeAttr) == "yrSingle":

            with open("./data/map/lga_map_data_" + str(yearAttr) + ".csv", "r") as infile:

                data = csv.reader(infile)
                next(data)

                for row in data:
                    totalCount += float(row[dataAttr])

        # Multi Year Count
        if str(rangeAttr) == "yrMulti":
            totalCount = 0.0
            yr1Index = years.index(yRange1)
            yr2Index = years.index(yRange2)

            for year in years[yr1Index:yr2Index + 1]:

                with open("./data/map/lga_map_data_" + year + ".csv", "r") as infile:
                    data = csv.reader(infile)
                    next(data)

                    for row in data:
                        totalCount += float(row[dataAttr])

        ########################################################################

        # Single Year Data
        if str(rangeAttr) == "yrSingle":
            jsonOut = []

            with open("./data/map/lga_map_data_" + str(yearAttr) + ".csv", "r") as infile:

                data = csv.reader(infile)
                next(data)

                for row in data:
                    innerDict = {}
                    innerDict["lga"] = (row[0]).upper().replace("_", " ")
                    innerDict["value"] = (float(row[dataAttr])/totalCount)*100

                    jsonOut.append(innerDict)

        # Multi Year Data
        if str(rangeAttr) == "yrMulti":
            yr1Index = years.index(yRange1)
            yr2Index = years.index(yRange2)

            jsonOut = []
            lgaCount = defaultdict(int)

            for year in years[yr1Index:yr2Index + 1]:

                with open("./data/map/lga_map_data_" + year + ".csv", "r") as infile:
                    data = csv.reader(infile)
                    next(data)

                    for row in data:
                        lgaCount[(row[0]).upper().replace("_", " ")] += (float(row[dataAttr])/totalCount)*100

            for key, value in lgaCount.iteritems():
                innerDict = {}
                innerDict["lga"] = key
                innerDict["value"] = value

                jsonOut.append(innerDict)

    return(jsonOut)

################################################################################
# HIGHMAPS JAVASCRIPT GENERATOR

def map_JS(dataAttr, rangeAttr, aggType, yearAttr="", yRange1="", yRange2=""):
    headings = ["lga", "All Crashes", "Hit and Runs",
                "Persons Involved in a Crash",
                "Fatalities Due to Car Crashes", "Injuries Due to Car Crashes",
                "Males Involved in a Crash", "Females Involved in a Crash",
                "Old Drivers Involved in a Crash",
                "Young Drivers Involved in a Crash",
                "Alcohol Related Car Crashes"]

    if aggType == "total":
        chartTitlePrefix = "Total Count of"
        tooltip = "{point.lga}: {point.value} " + headings[dataAttr]
    else:
        chartTitlePrefix = "Percentage of"
        tooltip = "{point.lga}: {point.value:.1f} % " + headings[dataAttr]


    if yearAttr is not None:
        chartTitle = str("in " + yearAttr)
    else:
        chartTitle = str("between " + yRange1 + " - " + yRange2)

    js = """ $(function () {

     var data = %s;

    $.getJSON("/static/lga.geo.json", function (geojson) {

        // Initiate the chart
        $('#map').highcharts('Map', {

            title : {
                text : '%s %s in Victoria %s'
            },

            mapNavigation: {
                enabled: true,
                buttonOptions: {
                    verticalAlign: 'top'
                },
                enableMouseWheelZoom: false
            },

            colorAxis: {
                stops: [
                    [0, '#ffc654'],
                    [0.25, '#f2964b'],
                    [0.75, '#ab4683'],
                    [1, '#852294']
                ],
            },
            tooltip: {
                pointFormat: '%s'
            },
            series : [{
                data: data,
                borderColor: '#ffffff',
                mapData: geojson,
                joinBy: ['vic_lga__3', 'lga'],
                name: '%s',
                states: {
                    hover: {
                        color: '#d6694b'
                    }
                },
                dataLabels: {
                    enabled: true,
                    format: '{point.lga}'
                }
            }]
        });
    });
});
"""
    return js % (map_data(dataAttr, rangeAttr, aggType, yearAttr, yRange1,
                          yRange2), chartTitlePrefix, headings[dataAttr],
                          chartTitle, tooltip, headings[dataAttr])
