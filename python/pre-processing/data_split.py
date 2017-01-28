################################################################################
# DATA_SPLIT.PY
# Creates specific CSV files by splitting data by each year and each LGA

################################################################################
# IMPORTS

import csv

################################################################################
# YEAR SPLIT

def split_years():
    '''
    Splits the data in separate year CSV files.
    '''
    years = ["2010", "2011", "2012", "2013", "2014", "2015"]

    for year in years:
        with open("../../data/crashes_processed.csv", "r") as infile:

            data = csv.reader(infile)
            header = next(data)

            with open("../../data/year/crashes_" + year + ".csv", "w") as outfile:

                 writer = csv.writer(outfile, lineterminator = "\n")
                 writer.writerow(header)

                 for row in data:
                     if row[0][-4:] == year:
                         writer.writerow(row)

################################################################################
# LGA SPLIT

def split_lgas():
    '''
    Splits the data in separate LGA CSV files.
    '''
    print("WARNING: This script takes a long time to complete")

    allLGAs = ['ALPINE', 'ARARAT', 'BALLARAT', 'BANYULE', 'BASS COAST',
               'BASS COAST', 'BASS COAST', 'BAW BAW', 'BAYSIDE', 'BENALLA',
               'BOROONDARA', 'BRIMBANK', 'BULOKE', 'CAMPASPE', 'CARDINIA',
               'CASEY', 'CENTRAL GOLDFIELDS', 'COLAC OTWAY', 'CORANGAMITE',
               'DAREBIN', 'EAST GIPPSLAND', 'FALLS CREEK ALPINE RESORT (UNINC)',
               'FRANKSTON', 'FRENCH-ELIZABETH-SANDSTONE ISLANDS (UNINC)',
               'FRENCH-ELIZABETH-SANDSTONE ISLANDS (UNINC)',
               'FRENCH-ELIZABETH-SANDSTONE ISLANDS (UNINC)',
               'GABO ISLAND (UNINC)', 'GANNAWARRA', 'GLEN EIRA', 'GLENELG',
               'GOLDEN PLAINS', 'GREATER BENDIGO', 'GREATER DANDENONG',
               'GREATER GEELONG', 'GREATER SHEPPARTON', 'HEPBURN', 'HINDMARSH',
               'HOBSONS BAY', 'HORSHAM', 'HUME', 'INDIGO', 'KINGSTON', 'KNOX',
               'LAKE MOUNTAIN ALPINE RESORT (UNINC)', 'LATROBE', 'LODDON',
               'MACEDON RANGES', 'MANNINGHAM', 'MANSFIELD', 'MARIBYRNONG',
               'MAROONDAH', 'MELBOURNE', 'MELTON', 'MILDURA', 'MITCHELL',
               'MOIRA', 'MONASH', 'MOONEE VALLEY', 'MOORABOOL', 'MORELAND',
               'MORNINGTON PENINSULA', 'MOUNT ALEXANDER',
               'MOUNT BAW BAW ALPINE RESORT (UNINC)',
               'MOUNT BULLER ALPINE RESORT (UNINC)',
               'MOUNT HOTHAM ALPINE RESORT (UNINC)',
               'MOUNT STIRLING ALPINE RESORT (UNINC)', 'MOYNE', 'MURRINDINDI',
               'MURRINDINDI', 'NILLUMBIK', 'NORTHERN GRAMPIANS', 'PORT PHILLIP',
               'PYRENEES', 'QUEENSCLIFFE', 'SOUTH GIPPSLAND', 'SOUTHERN GRAMPIANS',
               'STONNINGTON', 'STRATHBOGIE', 'SURF COAST', 'SWAN HILL', 'TOWONG',
               'WANGARATTA', 'WARRNAMBOOL', 'WELLINGTON', 'WEST WIMMERA',
               'WHITEHORSE', 'WHITTLESEA', 'WODONGA', 'WYNDHAM', 'YARRA',
               'YARRA RANGES', 'YARRIAMBIACK']

    for lga in allLGAs:
        with open("../../data/crashes_processed.csv", "r") as infile:

            data = csv.reader(infile)
            header = next(data)

            with open("../../data/lga/crashes_" + lga.lower().replace(" ", "_") + ".csv", "w") as outfile:
                print("Doning LGA:", lga, "...")
                writer = csv.writer(outfile, lineterminator = "\n")
                writer.writerow(header)

                for row in data:
                    if row[13] == lga:
                        writer.writerow(row)


if __name__ == "__main__":
    split_years()
    split_lgas()
