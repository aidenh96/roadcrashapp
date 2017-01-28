################################################################################
# APP.PY
# This is the main flask app the links all other files and scripts for the
# webapp to function correctly

################################################################################
# IMPORTS

from flask import Flask, render_template, request

# Other Python Files
from python.map_data import *
from python.chart_data import *
from python.pivot_table import *

################################################################################
# FLASK APP

# Create the app
app = Flask(__name__)

# Create each web page
@app.route("/")
def main():
    return render_template('index.html')

@app.route("/data")
def data():
    return render_template('data.html')

@app.route("/credits")
def credits():
    return render_template('credits.html')

@app.route("/pivotselect")
def pivotselect():
    return render_template('pivotselect.html', pivot_form = gen_pivot_form())

@app.route("/pivot", methods = ["GET"])
def pivot():

    # Dict for converting strings into functions
    aggFuncs = {"np.sum": "sum of", "np.mean": "mean of",
                "np.count_nonzero": "count of"}

    index_input = request.args.get("row")
    columns_input = request.args.get("column")
    values_input = request.args.get("aggregateVal")
    aggfunc_input = request.args.get("aggregateType")

    link = "pivot?row=" + columns_input + "&column=" + index_input \
    + "&aggregateType=" + aggfunc_input + "&aggregateVal=" + values_input

    return render_template('pivot.html', pt_swap_link = link,
                           pt_row = index_input.lower().replace("_", " "),
                           pt_col = columns_input.lower().replace("_", " "),
                           pt_agg_type = aggFuncs[aggfunc_input.lower()],
                           pt_agg_val = values_input.lower().replace("_", " "),
                           pt_HTML = gen_pivot_table(index_input,
                                                     columns_input,
                                                     values_input,
                                                     aggfunc_input))

@app.route("/charts")
def charts():
    return render_template('charts.html', chart1_js = gen_chart1_JS(),
                           chart2_js = gen_chart2_JS(),
                           chart3_js = gen_chart3_JS(),
                           chart4_js = gen_chart4_JS(),
                           chart5_js = gen_chart5_JS())

@app.route("/mapselect")
def mapselect():
    return render_template('mapselect.html')

@app.route("/map", methods = ["GET"])
def map():
    dataAttr = request.args.get("dataAttr")
    yearAttr = request.args.get("yearAttr")
    rangeAttr = request.args.get("yearRange")
    aggType = request.args.get("aggType")
    yRange1 = request.args.get("yRange1")
    yRange2 = request.args.get("yRange2")

    return render_template('map.html', hm_JS = map_JS(int(dataAttr), rangeAttr,
                                                      aggType, yearAttr,
                                                      yRange1, yRange2))

################################################################################
# RUN THE APP

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)
