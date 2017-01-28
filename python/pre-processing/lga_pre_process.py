################################################################################
# LGA_PRE_PROCESS.PY
# Reads in each LGA crash dataset and writes out a new dataset based on the
# counts, by region, of 10 most interesting features

################################################################################
# IMPORTS

import csv

################################################################################
# MAIN FUNCTIONS

def main(csvout, year):
    '''
    Counts relevant features from each LGA crash dataset and add them to a new
    collective dataset based on region.
    '''
    lgas = ['ALPINE', 'ARARAT', 'BALLARAT', 'BANYULE', 'BASS COAST', 'BAW BAW',
            'BAYSIDE', 'BENALLA', 'BOROONDARA', 'BRIMBANK', 'BULOKE', 'CAMPASPE',
            'CARDINIA', 'CASEY', 'CENTRAL GOLDFIELDS', 'COLAC OTWAY',
            'CORANGAMITE', 'DAREBIN', 'EAST GIPPSLAND',
            'FALLS CREEK ALPINE RESORT (UNINC)', 'FRANKSTON', 'GANNAWARRA',
            'GLEN EIRA', 'GLENELG', 'GOLDEN PLAINS', 'GREATER BENDIGO',
            'GREATER DANDENONG', 'GREATER GEELONG', 'GREATER SHEPPARTON',
            'HEPBURN', 'HINDMARSH', 'HOBSONS BAY', 'HORSHAM', 'HUME', 'INDIGO',
            'KINGSTON', 'KNOX', 'LAKE MOUNTAIN ALPINE RESORT (UNINC)', 'LATROBE',
            'LODDON', 'MACEDON RANGES', 'MANNINGHAM', 'MANSFIELD', 'MARIBYRNONG',
            'MAROONDAH', 'MELBOURNE', 'MELTON', 'MILDURA', 'MITCHELL', 'MOIRA',
            'MONASH', 'MOONEE VALLEY', 'MOORABOOL', 'MORELAND',
            'MORNINGTON PENINSULA', 'MOUNT ALEXANDER',
            'MOUNT BAW BAW ALPINE RESORT (UNINC)',
            'MOUNT BULLER ALPINE RESORT (UNINC)',
            'MOUNT HOTHAM ALPINE RESORT (UNINC)', 'MOYNE', 'MURRINDINDI',
            'NILLUMBIK', 'NORTHERN GRAMPIANS', 'PORT PHILLIP', 'PYRENEES',
            'QUEENSCLIFFE', 'SOUTH GIPPSLAND', 'SOUTHERN GRAMPIANS',
            'STONNINGTON', 'STRATHBOGIE', 'SURF COAST', 'SWAN HILL', 'TOWONG',
            'WANGARATTA', 'WARRNAMBOOL', 'WELLINGTON', 'WEST WIMMERA',
            'WHITEHORSE', 'WHITTLESEA', 'WODONGA', 'WYNDHAM', 'YARRA',
            'YARRA RANGES', 'YARRIAMBIACK']

    with open("../../data/map/lga_map_data_" + year + ".csv", "w") as outfile:

        writer = csv.writer(outfile, lineterminator = "\n")
        writer.writerow(["lga", "amount", "hit_run", "total_persons", "fatality", "injury", "males", "females", "old_driver", "young_driver", "alcohol_related"])

        for lga in lgas:
            aCount = 0
            hrCount = 0
            tpCount = 0
            fCount = 0
            iCount = 0
            mCount = 0
            feCount = 0
            odCount = 0
            ydCount = 0
            arCount = 0

            with open("../../data/lga/crashes_" + lga.lower().replace(" ", "_") + ".csv", "r") as infile:

                data = csv.reader(infile)
                next(data)

                for row in data:

                    if year == "all":
                        aCount += 1
                        tpCount += intC(row[15])
                        fCount += intC(row[17])
                        iCount += (intC(row[18]) + intC(row[19]))
                        mCount += intC(row[21])
                        feCount += intC(row[22])
                        odCount += intC(row[33])
                        ydCount += intC(row[34])

                        if row[5] == "Yes":
                            hrCount +=1

                        if row[35] == "Yes":
                            arCount +=1

                    elif row[0][-4:] == year:
                        aCount += 1
                        tpCount += intC(row[15])
                        fCount += intC(row[17])
                        iCount += (intC(row[18]) + intC(row[19]))
                        mCount += intC(row[21])
                        feCount += intC(row[22])
                        odCount += intC(row[33])
                        ydCount += intC(row[34])

                        if row[5] == "Yes":
                            hrCount +=1

                        if row[35] == "Yes":
                            arCount +=1

                writer.writerow([lga, aCount, hrCount, tpCount, fCount, iCount, mCount, feCount, odCount, ydCount, arCount])

def select_infile():
    years = ["2010", "2011", "2012", "2013", "2014", "2015", "all"]

    for year in years:
        infile = "../../data/year/crashes_" + year + ".csv"
        main(infile, year)

################################################################################
# HELPER FUNCTIONS

def intC(numb):
    '''
    Converts a string into an integer ignoring any exceptions.
    '''
    try:
        n = int(numb)
    except:
        n = 0
    return(n)

################################################################################
# RUN FUNCTIONS

if __name__ == "__main__":
    select_infile()
