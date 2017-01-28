###############################################################################
# PIVOT_TABLE.PY
# This file generates both the selection form for the pivot table , and the
# pivot table itself

################################################################################
# IMPORTS
import pandas as pd
import numpy as np

################################################################################
# Make the dataframe

df = pd.read_csv('data/crashes_processed.csv')

# Create index for yearly data
df["ACCIDENT_DATE"]=pd.to_datetime(df["ACCIDENT_DATE"], dayfirst=True)
df.index=df["ACCIDENT_DATE"]
df["YEAR"] = pd.DatetimeIndex(df['ACCIDENT_DATE']).year

name = list(df.columns.values)

################################################################################
################################################################################
# FORM FUNCTIONS

def drop():
    '''
    Creates the drop down list of index/columns.
    '''
    small_names = ['YEAR', 'ACCIDENT_TYPE', 'SEVERITY', 'SPEED_ZONE',
                   'POLICE_ATTEND', 'HIT_RUN_FLAG', 'LGA_NAME','REGION_NAME',
                   'ALCOHOL_RELATED','LIGHT_CONDITION', 'ROAD_GEOMETRY',]

    string = ""

    string +="<option selected disabled hidden>Select...</option>"

    for x in small_names:
        if x == "LGA_NAME":
            string +="<option value='LGA_NAME'>LGA Name</option>"
        elif x == "HIT_RUN_FLAG":
            string +="<option value='HIT_RUN_FLAG'>Hit & Runs</option>"
        else:
            string +="<option value=%s>%s</option>" %(x, x.title().replace("_", " "))

    return string

def drop_agg_func():
    '''
    Creates the drop down list of aggregate functions.
    '''
    string = ""
    string +="<option selected disabled hidden>Select...</option>"
    string += '<option value="np.count_nonzero">Count of </option>'
    string += '<option value="np.sum">Sum of</option>'
    string += '<option value="np.mean">Mean of</option>'

    return string

def drop_agg():
    '''
    Creates drop down list of aggregate columns.
    '''
    aggVals = ['TOTAL_PERSONS', 'INJ_OR_FATAL', 'FATALITY', 'MALES', 'FEMALES']
    string = ""

    for val in aggVals:
        string +='<option value=%s>%s</option>' %(val, val.title().replace("_", " "))

    return string

def gen_pivot_form():
    '''
    Generates the main HTML selection form for the pivot table.
    '''
    outStr = """
        <form name="pivot_select" action="/pivot" method="GET">
        <div class="row uniform">
        <div class="6u 12u$(xsmall) main-select">
        <label for="pt_row">Row Label</label>
        <div class="select-wrapper">
        <select name="row" id="pt_row">"""

    outStr += drop()
    outStr +=  """

        </select>
        </div>
        </div>

    <div class="6u 12u$(xsmall) main-select">
    <label for="column">Column Label</label>
    <div class="select-wrapper">
    <select name="column" id="column">"""

    outStr += drop()
    outStr +=  """
    </select>
    </div>
    </div>

    <div class="4u 12u$(xsmall)">
    <label for="aggregateType">Aggregation</label>
    <div class="select-wrapper">
    <select name="aggregateType" id="aggregateType">"""

    outStr += drop_agg_func()
    outStr +=  """
    </select>
    </div>
    </div>

    <div class="8u 12u$(xsmall)">
    <label for="aggregateVal">Aggregation Values</label>
    <div class="select-wrapper">
    <select name="aggregateVal" id="aggregateVal">"""
    outStr += drop_agg()
    outStr +=  """
    </select>
    </div>
    </div>

    <div class="12u$">
    <ul class="actions">
    <li><input type="submit" value="Generate Pivot Table" class="special" /></li>
    <li><input type="reset" id="pivotReset" value="Reset" /></li></ul>
    </div>

</div>
</form>
"""
    return  outStr

################################################################################
################################################################################
# PIVOT TABLE GENERATION FUNCTIONS

def gen_pivot_table(index_input, columns_input, values_input, aggfunc_input):
    outStr = ""

    # Dict for converting strings into functions
    aggFuncs = {"np.sum": np.sum, "np.mean": np.mean,\
    "np.count_nonzero": np.count_nonzero}

    ######################################################################
    # Validation
    if index_input == 'Select':
        outStr +='<p>Please enter a valid Index</p>'
        return outStr

    if columns_input == 'Select':
        outStr +='<p>Please enter a valid Column</p>'
        return outStr

    if index_input == columns_input:
        outStr +='<p>Please enter a 2D table</p>'
        return outStr

    if aggfunc_input == 'Select':
        outStr +='<p>Please enter a valid Aggregation Function</p>'

    ######################################################################
    # Generates Pivot Table
    dm = pd.pivot_table(df,index=[index_input], columns=[columns_input],\
    values=[values_input], aggfunc=aggFuncs[aggfunc_input])

    dm.fillna(value=0,  inplace=True) #Replace all null data with 0

    # Convert Pivot Table to HTML
    dm = dm.to_html()

    # Text Styling Fixes for Titles
    dm = dm.replace(columns_input, "")
    dm = dm.replace(values_input, columns_input.replace("_", " "))
    dm = dm.replace(index_input, index_input.replace("_", " "))

    return dm
