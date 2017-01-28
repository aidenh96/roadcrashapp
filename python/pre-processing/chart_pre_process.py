################################################################################
# CHART_PRE_PROCESS.PY
# Creates specific CSV files that contain only the data needed for each chart

################################################################################
# IMPORTS

import csv
from collections import defaultdict

################################################################################
# CHART FUNCTIONS

def chart1_data(csvout):
	'''
	Counts the number of crashes in all of Victoria, as well as in Eastern,
	Northern, and Western Victoria separately.
	'''
	yearsCount = defaultdict(int)
	easternCount = defaultdict(int)
	northernCount = defaultdict(int)
	westernCount = defaultdict(int)

	years = ["2010", "2011", "2012", "2013", "2014", "2015"]

	with open(csvout, "w+") as outfile:
		writer = csv.writer(outfile, lineterminator = "\n")
		writer.writerow(["region","2010", "2011", "2012", "2013", "2014", "2015"])

		for year in years:
			with open("../../data/year/crashes_" + year + ".csv", "r") as infile:

				data = csv.reader(infile)
				next(data)

				for row in data:
					yearsCount[row[0][-4:]] += 1

					if row[14] == "WESTERN REGION" or row[14] == "SOUTH WESTERN REGION" or row[14] == "METROPOLITAN NORTH WEST REGION":
						westernCount[row[0][-4:]] += 1
					elif row[14] == "NORTHERN REGION" or row[14] == "NORTH EASTERN REGION":
						northernCount[row[0][-4:]] += 1
					elif row[14] == "EASTERN REGION" or row[14] == "METROPOLITAN SOUTH EAST REGION":
						easternCount[row[0][-4:]] += 1

		writer.writerow(["vic", yearsCount["2010"], yearsCount["2011"], yearsCount["2012"],yearsCount["2013"],yearsCount["2014"],yearsCount["2015"]])
		writer.writerow(["eastern", easternCount["2010"], easternCount["2011"], easternCount["2012"], easternCount["2013"], easternCount["2014"], easternCount["2015"]])
		writer.writerow(["northern", northernCount["2010"], northernCount["2011"], northernCount["2012"], northernCount["2013"], northernCount["2014"], northernCount["2015"]])
		writer.writerow(["western", westernCount["2010"], westernCount["2011"], westernCount["2012"], westernCount["2013"], westernCount["2014"], westernCount["2015"]])

################################################################################

def chart2_data(csvout):
	'''
	Counts the number of hit and runs and alcohol related crashes in each LGA.
	'''
	hrCount = 0
	ddCount = 0
	regions = ['alpine', 'ararat', 'ballarat', 'banyule', 'bass_coast', 'baw_baw', 'bayside', 'benalla', 'boroondara', 'brimbank', 'buloke', 'campaspe', 'cardinia', 'casey', 'central_goldfields', 'colac_otway', 'corangamite', 'darebin', 'east_gippsland', 'falls_creek_alpine_resort_(uninc)', 'frankston', 'gannawarra', 'glen_eira', 'glenelg', 'golden_plains', 'greater_bendigo', 'greater_dandenong', 'greater_geelong', 'greater_shepparton', 'hepburn', 'hindmarsh', 'hobsons_bay', 'horsham', 'hume', 'indigo', 'kingston', 'knox', 'lake_mountain_alpine_resort_(uninc)', 'latrobe', 'loddon', 'macedon_ranges', 'manningham', 'mansfield', 'maribyrnong', 'maroondah', 'melbourne', 'melton', 'mildura', 'mitchell', 'moira', 'monash', 'moonee_valley', 'moorabool', 'moreland', 'mornington_peninsula', 'mount_alexander', 'mount_baw_baw_alpine_resort_(uninc)', 'mount_buller_alpine_resort_(uninc)', 'mount_hotham_alpine_resort_(uninc)', 'moyne', 'murrindindi', 'nillumbik', 'northern_grampians', 'port_phillip', 'pyrenees', 'queenscliffe', 'south_gippsland', 'southern_grampians', 'stonnington', 'strathbogie', 'surf_coast', 'swan_hill', 'towong', 'wangaratta', 'warrnambool', 'wellington', 'west_wimmera', 'whitehorse', 'whittlesea', 'wodonga', 'wyndham', 'yarra', 'yarra_ranges', 'yarriambiack']

	with open(csvout, "w+") as outfile:
		writer = csv.writer(outfile, lineterminator = "\n")
		writer.writerow(["region", "hit_runs", "drunk_drivers"])

		for reg in regions:
			with open("../../data/lga/crashes_" + reg + ".csv", "r") as infile:
				data = csv.reader(infile)
				next(data)
				for row in data:
					if row[5] == "Yes":
						hrCount += 1
					if row[35] == "Yes":
						ddCount += 1

			if row[14] == "WESTERN REGION" or row[14] == "SOUTH WESTERN REGION" or row[14] == "METROPOLITAN NORTH WEST REGION":
				writer.writerow(["Western", hrCount, ddCount])
			elif row[14] == "NORTHERN REGION" or row[14] == "NORTH EASTERN REGION":
				writer.writerow(["Northern", hrCount, ddCount])
			elif row[14] == "EASTERN REGION" or row[14] == "METROPOLITAN SOUTH EAST REGION":
				writer.writerow(["Eastern", hrCount, ddCount])

			hrCount = 0
			ddCount = 0


################################################################################

def chart3_data(csvout):
	'''
	Counts the number of fatalities in each region, depending on the light
	condition.
	'''
	vicCount1 = 0
	easternCount1 = 0
	northernCount1 = 0
	westernCount1 = 0
	vicCount2 = 0
	easternCount2 = 0
	northernCount2 = 0
	westernCount2 = 0
	vicCount3 = 0
	easternCount3 = 0
	northernCount3 = 0
	westernCount3 = 0
	vicCount4 = 0
	easternCount4 = 0
	northernCount4 = 0
	westernCount4 = 0
	vicCount5 = 0
	easternCount5 = 0
	northernCount5 = 0
	westernCount5 = 0
	vicCount6 = 0
	easternCount6 = 0
	northernCount6 = 0
	westernCount6 = 0

	with open(csvout, "w+") as outfile:
		writer = csv.writer(outfile, lineterminator = "\n")
		writer.writerow(["light condition", "vic", "northern", "eastern", "western"])

		with open("../../data/crashes_processed.csv", "r") as infile:

			data = csv.reader(infile)
			next(data)

			for row in data:

				if row[6] == "Dark No street lights":
					vicCount1 += int(row[17])
					if row[14] == "WESTERN REGION" or row[14] == "SOUTH WESTERN REGION" or row[14] == "METROPOLITAN NORTH WEST REGION":
						westernCount1 += int(row[17])
					elif row[14] == "NORTHERN REGION" or row[14] == "NORTH EASTERN REGION":
						northernCount1 += int(row[17])
					elif row[14] == "EASTERN REGION" or row[14] == "METROPOLITAN SOUTH EAST REGION":
						easternCount1 += int(row[17])

				elif row[6] == "Dark Street lights off":
					vicCount2 += int(row[17])
					if row[14] == "WESTERN REGION" or row[14] == "SOUTH WESTERN REGION" or row[14] == "METROPOLITAN NORTH WEST REGION":
						westernCount2 += int(row[17])
					elif row[14] == "NORTHERN REGION" or row[14] == "NORTH EASTERN REGION":
						northernCount2 += int(row[17])
					elif row[14] == "EASTERN REGION" or row[14] == "METROPOLITAN SOUTH EAST REGION":
						easternCount2 += int(row[17])

				elif row[6] == "Dark Street lights on":
					vicCount3 += int(row[17])
					if row[14] == "WESTERN REGION" or row[14] == "SOUTH WESTERN REGION" or row[14] == "METROPOLITAN NORTH WEST REGION":
						westernCount3 += int(row[17])
					elif row[14] == "NORTHERN REGION" or row[14] == "NORTH EASTERN REGION":
						northernCount3 += int(row[17])
					elif row[14] == "EASTERN REGION" or row[14] == "METROPOLITAN SOUTH EAST REGION":
						easternCount3 += int(row[17])

				elif row[6] == "Dark Street lights unknown":
					vicCount4 += int(row[17])
					if row[14] == "WESTERN REGION" or row[14] == "SOUTH WESTERN REGION" or row[14] == "METROPOLITAN NORTH WEST REGION":
						westernCount4 += int(row[17])
					elif row[14] == "NORTHERN REGION" or row[14] == "NORTH EASTERN REGION":
						northernCount4 += int(row[17])
					elif row[14] == "EASTERN REGION" or row[14] == "METROPOLITAN SOUTH EAST REGION":
						easternCount4 += int(row[17])

				elif row[6] == "Day":
					vicCount5 += int(row[17])
					if row[14] == "WESTERN REGION" or row[14] == "SOUTH WESTERN REGION" or row[14] == "METROPOLITAN NORTH WEST REGION":
						westernCount5 += int(row[17])
					elif row[14] == "NORTHERN REGION" or row[14] == "NORTH EASTERN REGION":
						northernCount5 += int(row[17])
					elif row[14] == "EASTERN REGION" or row[14] == "METROPOLITAN SOUTH EAST REGION":
						easternCount5 += int(row[17])

				elif row[6] == "Dusk/Dawn":
					vicCount6 += int(row[17])
					if row[14] == "WESTERN REGION" or row[14] == "SOUTH WESTERN REGION" or row[14] == "METROPOLITAN NORTH WEST REGION":
						westernCount6 += int(row[17])
					elif row[14] == "NORTHERN REGION" or row[14] == "NORTH EASTERN REGION":
						northernCount6 += int(row[17])
					elif row[14] == "EASTERN REGION" or row[14] == "METROPOLITAN SOUTH EAST REGION":
						easternCount6 += int(row[17])


		writer.writerow(["Dark No Street Lights", vicCount1, northernCount1, easternCount1, westernCount1])
		writer.writerow(["Dark Street Lights Off", vicCount2, northernCount2, easternCount2, westernCount2])
		writer.writerow(["Dark Street Lights On", vicCount3, northernCount3, easternCount3, westernCount3])
		writer.writerow(["Dark Street Lights Unknown", vicCount4, northernCount4, easternCount4, westernCount4])
		writer.writerow(["Day", vicCount5, northernCount5, easternCount5, westernCount5])
		writer.writerow(["Dusk/Dawn", vicCount6, northernCount6, easternCount6, westernCount6])

################################################################################

def chart4_data(csvout):
	'''
	Counts the number of crashes for each type of accident and find percentage against total crushes for each region
	'''
	vicCount = 0
	westernCount = 0
	northernCount = 0
	easternCount = 0
	typeCount_v = defaultdict(int)
	typeCount_e = defaultdict(int)
	typeCount_n = defaultdict(int)
	typeCount_w = defaultdict(int)

	typelst = ["Collision with vehicle","Collision with a fixed object","collision with some other object","No collision and no object struck","Vehicle overturned (no collision)","Struck Pedestrian","Struck animal","Fall from or in moving vehicle"]

	with open(csvout, "w+") as outfile:
		writer = csv.writer(outfile, lineterminator = "\n")
		writer.writerow(["region","Collision with vehicle","Collision with a fixed object","collision with some other object","No collision and no object struck","Vehicle overturned (no collision)","Struck Pedestrian","Struck animal","Fall from or in moving vehicle"])

		with open("../../data/crashes_processed.csv", "r") as infile:

			data = csv.reader(infile)
			next(data)

			for row in data:
				vicCount += 1.0
				for types in typelst:
					if row[3] == types:
						typeCount_v[types] += 1.0

				if row[14] == "WESTERN REGION" or row[14] == "SOUTH WESTERN REGION" or row[14] == "METROPOLITAN NORTH WEST REGION":
					westernCount += 1.0
					for types in typelst:
						if row[3] == types:
							typeCount_w[types] += 1.0

				elif row[14] == "NORTHERN REGION" or row[14] == "NORTH EASTERN REGION":
					northernCount += 1.0
					for types in typelst:
						if row[3] == types:
							typeCount_n[types] += 1.0

				elif row[14] == "EASTERN REGION" or row[14] == "METROPOLITAN SOUTH EAST REGION":
					easternCount += 1.0
					for types in typelst:
						if row[3] == types:
							typeCount_e[types] += 1.0

		writer.writerow(["Victoria", typeCount_v[typelst[0]]/vicCount, typeCount_v[typelst[1]]/vicCount, typeCount_v[typelst[2]]/vicCount, typeCount_v[typelst[3]]/vicCount, typeCount_v[typelst[4]]/vicCount, typeCount_v[typelst[5]]/vicCount, typeCount_v[typelst[6]]/vicCount, typeCount_v[typelst[7]]/vicCount])
		writer.writerow(["Eastern", typeCount_e[typelst[0]]/easternCount, typeCount_e[typelst[1]]/easternCount, typeCount_e[typelst[2]]/easternCount, typeCount_e[typelst[3]]/easternCount, typeCount_e[typelst[4]]/easternCount, typeCount_e[typelst[5]]/easternCount, typeCount_e[typelst[6]]/easternCount, typeCount_e[typelst[7]]/easternCount])
		writer.writerow(["Northern", typeCount_n[typelst[0]]/northernCount, typeCount_n[typelst[1]]/northernCount, typeCount_n[typelst[2]]/northernCount, typeCount_n[typelst[3]]/northernCount, typeCount_n[typelst[4]]/northernCount, typeCount_n[typelst[5]]/northernCount, typeCount_n[typelst[6]]/northernCount, typeCount_n[typelst[7]]/northernCount])
		writer.writerow(["Western", typeCount_w[typelst[0]]/westernCount, typeCount_w[typelst[1]]/westernCount, typeCount_w[typelst[2]]/westernCount, typeCount_w[typelst[3]]/westernCount, typeCount_w[typelst[4]]/westernCount, typeCount_w[typelst[5]]/westernCount, typeCount_w[typelst[6]]/westernCount, typeCount_w[typelst[7]]/westernCount])

################################################################################

def chart5_data(csvout):
	'''
	Counts the number of crashes in every hour in each region
	'''
	vicCount = defaultdict(int)
	easternCount = defaultdict(int)
	northernCount = defaultdict(int)
	westernCount = defaultdict(int)

	with open(csvout, "w+") as outfile:
		writer = csv.writer(outfile, lineterminator = "\n")
		writer.writerow(["region","00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"])

		with open("../../data/crashes_processed.csv", "r") as infile:

			data = csv.reader(infile)
			next(data)

			for row in data:
				vicCount[row[1][:2]] += 1

				if row[14] == "WESTERN REGION" or row[14] == "SOUTH WESTERN REGION" or row[14] == "METROPOLITAN NORTH WEST REGION":
					westernCount[row[1][:2]] += 1
				elif row[14] == "NORTHERN REGION" or row[14] == "NORTH EASTERN REGION":
					northernCount[row[1][:2]] += 1
				elif row[14] == "EASTERN REGION" or row[14] == "METROPOLITAN SOUTH EAST REGION":
					easternCount[row[1][:2]] += 1

		writer.writerow(["Victoria", vicCount["00"], vicCount["01"], vicCount["02"], vicCount["03"], vicCount["04"], vicCount["05"], vicCount["06"], vicCount["07"], vicCount["08"], vicCount["09"], vicCount["10"], vicCount["11"], vicCount["12"], vicCount["13"], vicCount["14"], vicCount["15"], vicCount["16"], vicCount["17"], vicCount["18"], vicCount["19"], vicCount["20"], vicCount["21"], vicCount["22"], vicCount["23"]])
		writer.writerow(["Eastern", easternCount["00"], easternCount["01"], easternCount["02"], easternCount["03"], easternCount["04"], easternCount["05"], easternCount["06"], easternCount["07"], easternCount["08"], easternCount["09"], easternCount["10"], easternCount["11"], easternCount["12"], easternCount["13"], easternCount["14"], easternCount["15"], easternCount["16"], easternCount["17"], easternCount["18"], easternCount["19"], easternCount["20"], easternCount["21"], easternCount["22"], easternCount["23"]])
		writer.writerow(["Northern", northernCount["00"], northernCount["01"], northernCount["02"], northernCount["03"], northernCount["04"], northernCount["05"], northernCount["06"], northernCount["07"], northernCount["08"], northernCount["09"], northernCount["10"], northernCount["11"], northernCount["12"], northernCount["13"], northernCount["14"], northernCount["15"], northernCount["16"], northernCount["17"], northernCount["18"], northernCount["19"], northernCount["20"], northernCount["21"], northernCount["22"], northernCount["23"]])
		writer.writerow(["Western", westernCount["00"], westernCount["01"], westernCount["02"], westernCount["03"], westernCount["04"], westernCount["05"], westernCount["06"], westernCount["07"], westernCount["08"], westernCount["09"], westernCount["10"], westernCount["11"], westernCount["12"], westernCount["13"], westernCount["14"], westernCount["15"], westernCount["16"], westernCount["17"], westernCount["18"], westernCount["19"], westernCount["20"], westernCount["21"], westernCount["22"], westernCount["23"]])
################################################################################
# RUN FUNCTIONS

if __name__ == "__main__":
	chart1_data("../../data/charts/chart1_data.csv")
	chart2_data("../../data/charts/chart2_data.csv")
	chart3_data("../../data/charts/chart3_data.csv")
	chart4_data("../../data/charts/chart4_data.csv")
	chart5_data("../../data/charts/chart5_data.csv")
