# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 09:27:31 2018

@author: Ahsan, Muzammil, Leena
"""

######### This file is for 10g test ##############


# import the necessary packages

from __future__ import division
import globals
from reportlab.pdfgen import canvas
from reportlab.platypus import *
from reportlab.rl_config import defaultPageSize
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from bidi.algorithm import get_display
from rtl import reshaper
from reportlab.platypus import SimpleDocTemplate, Paragraph
from textwrap3 import wrap
from reportlab.graphics.charts.legends import Legend
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.lib.styles import black, white
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib.colors import HexColor
from PIL import Image, ImageTk, ImageEnhance
import os
import tensorflow as tf
from win32api import GetSystemMetrics

# leena
screen_width, screen_height = GetSystemMetrics(0), GetSystemMetrics(1)
###


# ---------------------------------------------------------------------------
# Report Writing
# Report Writing
# ---------------------------------------------------------------------------
def calculate_no_of_grains(objects):
    print("Checking number of grains")
    print("The number of grains are:", len(objects))
    calculate_no_of_grains.no_of_grains = len(objects)
    return(calculate_no_of_grains.no_of_grains)


# Getting user input (in mm) for broken size calculation
def get_user_input(x1):
    if x1 is "":
        #global no_user_input
        globals.no_user_input = 0
        print("The user input is: empty")
    else:
        #global no_user_input
        globals.no_user_input = 1
        print("The user input is:", x1, "mm")
        get_user_input.result1 = x1


# leena
# these functions to get user input
# for long broken maximum and minimum
def get_input_LongBroken(x3_longBrokenMax, x4_longBrokenMin):
    get_input_LongBroken.Max = x3_longBrokenMax
    get_input_LongBroken.Min = x4_longBrokenMin
    #print("long broken")

# for medium broken max and min


def get_input_MediumBroken(x5_MediumBrokenMax, x6_MediumBrokenMin):
    get_input_MediumBroken.Max = x5_MediumBrokenMax
    get_input_MediumBroken.Min = x6_MediumBrokenMin
    #print("Medium broken")

# for small broken max and min


def get_input_SmallBroken(x7_SmallBrokenMax, x8_SmallBrokenMin):
    get_input_SmallBroken.Max = x7_SmallBrokenMax
    get_input_SmallBroken.Min = x8_SmallBrokenMin
    #print("Small broken")

#######


# leena
# to get user desired data to be add on report
def get_sampleNo(sampleNo):
    globals.called = 1
    if sampleNo is "":
        get_sampleNo.input = "-"
    else:
        get_sampleNo.input = sampleNo


def get_date(date):
    globals.called = 1
    if date is "":
        get_date.input = "-"
    else:
        get_date.input = date


def get_day(day):
    globals.called = 1
    if day is "":
        get_day.input = "-"
    else:
        get_day.input = day


def get_arrivalNo(arrivalNo):
    globals.called = 1
    if arrivalNo is "":
        get_arrivalNo.input = "-"
    else:
        get_arrivalNo.input = arrivalNo


def get_partyName(partyName):
    globals.called = 1
    if partyName is "":
        get_partyName.input = "-"
    else:
        get_partyName.input = partyName


def get_vehicleNo(vehicleNo):
    globals.called = 1
    if vehicleNo is "":
        get_vehicleNo.input = "-"
    else:
        get_vehicleNo.input = vehicleNo


def get_riceType(riceType):
    globals.called = 1
    if riceType is "":
        get_riceType.input = "-"
    else:
        get_riceType.input = riceType


def get_moisture(moisture):
    globals.called = 1
    if moisture is "":
        get_moisture.input = "-"
    else:
        get_moisture.input = moisture


def get_look(look):
    globals.called = 1
    if look is "":
        get_look.input = "-"
    else:
        get_look.input = look

model = tf.keras.models.load_model('w.h5')
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -----------------------------Irri-6 Report------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


def gen_report_irri6(objects, S_Report):
    #print(">>>>>>>>>> Sumarize report for irri-6 >>>>>>>>>>>>>")
    import time

    gtype = [0, 0, 0, 0]
    global ldata, cdata, tdata, Date, Time
    head = 0
    long = 0
    med = 0
    small = 0

    ## Making the logic of weighted average for head rice & broken rice ##
    ## Initializing variables ##
    #global broken_weight, final_weight

    head_weight = []
    broken_rice_weight = []
    yellow_weight = []
    damage_weight = []
    chalky_weight = []
    paddy_weight = []
    head_rice = []
    broken_rice = []

    # leena
    long_broken = []
    med_broken = []
    small_broken = []

    long_broken_list = []
    medium_broken_list = []
    small_broken_list = []

    long_broken_weight = []
    medium_broken_weight = []
    small_broken_weight = []

    total_long_broken_weight = 0
    total_medium_broken_weight = 0
    total_small_broken_weight = 0

    #Muzammil adding 1mm to 10mm analysis
    _1mm_2mm = 0
    _2mm_3mm = 0
    _3mm_4mm = 0
    _4mm_5mm = 0
    _5mm_6mm = 0
    _6mm_7mm = 0
    _7mm_8mm = 0
    _8mm_9mm = 0
    _9mm_10mm = 0


    _1mm_2mm_weight = []
    _2mm_3mm_weight = []
    _3mm_4mm_weight = []
    _4mm_5mm_weight = []
    _5mm_6mm_weight = []
    _6mm_7mm_weight = []
    _7mm_8mm_weight = []
    _8mm_9mm_weight = []
    _9mm_10mm_weight = []


    _1mm_2mm_rice = []
    _2mm_3mm_rice = []
    _3mm_4mm_rice = []
    _4mm_5mm_rice = []
    _5mm_6mm_rice = []
    _6mm_7mm_rice = []
    _7mm_8mm_rice = []
    _8mm_9mm_rice = []
    _9mm_10mm_rice = []


    total_1mm_2mm_weight = 0
    total_2mm_3mm_weight = 0
    total_3mm_4mm_weight = 0
    total_4mm_5mm_weight = 0
    total_5mm_6mm_weight = 0
    total_6mm_7mm_weight = 0
    total_7mm_8mm_weight = 0
    total_8mm_9mm_weight = 0
    total_9mm_10mm_weight = 0


    _1mm_2mm_agl = 0
    _2mm_3mm_agl = 0
    _3mm_4mm_agl = 0
    _4mm_5mm_agl = 0
    _5mm_6mm_agl = 0
    _6mm_7mm_agl = 0
    _7mm_8mm_agl = 0
    _8mm_9mm_agl = 0
    _9mm_10mm_agl = 0


    if globals.called is not 1:
        # if values are empty in that case
        get_sampleNo.input = "-"
        get_date.input = "-"
        get_day.input = "-"
        get_arrivalNo.input = "-"
        get_partyName.input = "-"
        get_vehicleNo.input = "-"
        get_riceType.input = "-"
        get_moisture.input = "-"
        get_look.input = "-"
        ##

    whole_kernel = []
    PAGE_HEIGHT = defaultPageSize[0]
    PAGE_WIDTH = defaultPageSize[0]
    DefaultPageSize = letter
    c = canvas.Canvas(S_Report, DefaultPageSize)

    # leena
    img = "img/header.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    ##

    form = c.acroForm
    import datetime
    now = datetime.datetime.now()
    now.strftime("%A")
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")
    c.setFont("Helvetica", 12)
    Time = "Test time : %s" % time
    c.setFont("Helvetica", 12)
    Date = "Test date : %s" % date
    c.setFont("Helvetica-Bold", 14)
    c.drawString(360, 620, "USER INFORMATION FORM")

    global total_grains
    total_grains = len(objects)

    avg_length = float(round(sum(x['Length12']
                       for x in objects)/len(objects), 3))
    avg_width = float(round(sum(x['Width'] for x in objects)/len(objects), 2))
    #avg_area = round(sum(x['Area'] for x in objects)/len(objects),2)

    for i in objects:

        # Calculations for whole/broken ratio

        # (calculate_value.result3 == 'No-AGL') and
        if (len(get_user_input.result1) != 0):

            #print("The user input for mm field exists. Not taking AGL as reference")
            #print("The input variable is: ",get_user_input.result1)
            #print("The length of variable is: ",len(get_user_input.result1))
            global x
            x = get_user_input.result1
            # print("\n\n\n")
            if (float(i['Length12']) >= float((x))):
                #print( "{} >= {}".format(float(i['Length']), float((x))) )
                head_rice.append(i)
            elif(float(i['Length12']) < float((x))):
                #print( "{} < {}".format(float(i['Length']), float((x))) )
                broken_rice.append(i)
            # print("\n\n\n")

##
# (calculate_value.result3 == 'AGL') and len(get_user_input2.result2) != 0
# elif ( (get_user_input.result1) == "" ):
##
# print("The user input for % field exists. Taking AGL as reference")
##
##            from reportnew import AGL
##
##            temp_AGL = AGL
# print("100 Grain test ran",temp_AGL)
##
##
##            x = float(get_user_input2.result2)/float(100)
# print("The percentage is:", x)
# j = (float(avg_length)*float(x))
##            j = (float(temp_AGL)*float(x))
##
# if (float((i['Length'])) >= (j)):
# head_rice.append(i)
# elif(float((i['Length'])) < (j)):
# broken_rice.append(i)

            # and (get_user_input2.result2) == ""
        elif ((get_user_input.result1) == ""):

            #print("The user inputs for both fields do not exist. By defaul input is 75%")

            x = 3/4
            y = 1/2
            z = 1/4

            # print(x,y,z)

            if (i['Length12'] >= avg_length*(x)):
                head_rice.append(i)
            elif((i['Length12'] < avg_length*(x)) and (i['Length12'] > avg_length*(y))):
                broken_rice.append(i)
            elif((i['Length12'] <= avg_length*(y)) and (i['Length12'] > avg_length*(z))):
                broken_rice.append(i)
            elif(i['Length12'] <= (z)):
                broken_rice.append(i)

    ## Making the logic of weighted average for head rice & broken rice ##
                ##   Start  ##

    #final_weight = 0

    #print("This is head rice array items",head_rice)
    #print("This is broken rice array items",broken_rice)

    # leena
    if broken_rice:
        #print("broken rice list here")
        # print(broken_rice)
        for brokenRice_element in broken_rice:
            if not get_input_LongBroken.Max is "" or not get_input_LongBroken.Min is "":
                if(float(get_input_LongBroken.Max) >= brokenRice_element["Length12"] >= float(get_input_LongBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_LongBroken.Max), brokenRice_element["Length"] ,float(get_input_LongBroken.Min)))
                    #print("long broken rice detected")
                    long_broken_list.append(brokenRice_element)

            if not get_input_MediumBroken.Max is "" or not get_input_MediumBroken.Min is "":
                if(float(get_input_MediumBroken.Max) >= brokenRice_element["Length12"] >= float(get_input_MediumBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_MediumBroken.Max), brokenRice_element["Length"] ,float(get_input_MediumBroken.Min)))
                    #print(" Medium broken rice detected")
                    # if particular item need to be added then brokenRice_element["Length"]
                    medium_broken_list.append(brokenRice_element)

            if not get_input_SmallBroken.Max is "" or not get_input_SmallBroken.Min is "":
                if(float(get_input_SmallBroken.Max) >= brokenRice_element["Length12"] >= float(get_input_SmallBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_SmallBroken.Max), brokenRice_element["Length"] ,float(get_input_SmallBroken.Min)))
                    #print(" Small broken rice detected")
                    small_broken_list.append(brokenRice_element)
    ##############
    #Muzammil adding 1mm to 10mm analysis

    for i in objects:
        if i["Length12"] >= 1 and i["Length12"] <= 2:
            _1mm_2mm = _1mm_2mm + 1
            _1mm_2mm_rice.append(i)
        
        elif i["Length12"] >= 2 and i["Length12"] <= 3:
            _2mm_3mm = _2mm_3mm + 1
            _2mm_3mm_rice.append(i)

        elif i["Length12"] >= 3 and i["Length12"] <= 4:
            _3mm_4mm = _3mm_4mm +1
            _3mm_4mm_rice.append(i)

        elif i["Length12"] >= 4 and i["Length12"] <= 5:
            _4mm_5mm = _4mm_5mm +1
            _4mm_5mm_rice.append(i)

        elif i["Length12"] >= 5 and i["Length12"] <= 6:
            _5mm_6mm = _5mm_6mm +1
            _5mm_6mm_rice.append(i)

        elif i["Length12"] >= 6 and i["Length12"] <= 7:
            _6mm_7mm = _6mm_7mm + 1
            _6mm_7mm_rice.append(i)
        
        elif i["Length12"] >= 7 and i["Length12"] <= 8:
            _7mm_8mm = _7mm_8mm + 1
            _7mm_8mm_rice.append(i)
        
        elif i["Length12"] >= 8 and i["Length12"] <= 9:
            _8mm_9mm = _8mm_9mm + 1
            _8mm_9mm_rice.append(i)

        elif i["Length12"] >= 9 and i["Length12"] <= 10:
            _9mm_10mm = _9mm_10mm + 1
            _9mm_10mm_rice.append(i)



    if _1mm_2mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_1mm_2mm_rice)-1):
            _1mm_2mm_weight.append(model.predict([[float(_1mm_2mm_rice[i]["Length"]),float(_1mm_2mm_rice[i]["Width"])]]))
            
        total_1mm_2mm_weight = float(sum(_1mm_2mm_weight))

    if _2mm_3mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_2mm_3mm_rice)-1):
            _2mm_3mm_weight.append(model.predict([[float(_2mm_3mm_rice[i]["Length"]),float(_2mm_3mm_rice[i]["Width"])]]))
            
        total_2mm_3mm_weight = float(sum(_2mm_3mm_weight))

    if _3mm_4mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_3mm_4mm_rice)-1):
            _3mm_4mm_weight.append(model.predict([[float(_3mm_4mm_rice[i]["Length"]),float(_3mm_4mm_rice[i]["Width"])]]))
            
        total_3mm_4mm_weight = float(sum(_3mm_4mm_weight))
    
    if _4mm_5mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_4mm_5mm_rice)-1):
            _4mm_5mm_weight.append(model.predict([[float(_4mm_5mm_rice[i]["Length"]),float(_4mm_5mm_rice[i]["Width"])]]))
            
        total_4mm_5mm_weight = float(sum(_4mm_5mm_weight))
    
    if _5mm_6mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_5mm_6mm_rice)-1):
            _5mm_6mm_weight.append(model.predict([[float(_5mm_6mm_rice[i]["Length"]),float(_5mm_6mm_rice[i]["Width"])]]))
            
        total_5mm_6mm_weight = float(sum(_5mm_6mm_weight))

    if _6mm_7mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_6mm_7mm_rice)-1):
            _6mm_7mm_weight.append(model.predict([[float(_6mm_7mm_rice[i]["Length"]),float(_6mm_7mm_rice[i]["Width"])]]))
            
        total_6mm_7mm_weight = float(sum(_6mm_7mm_weight))

    if _7mm_8mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_7mm_8mm_rice)-1):
            _7mm_8mm_weight.append(model.predict([[float(_7mm_8mm_rice[i]["Length"]),float(_7mm_8mm_rice[i]["Width"])]]))
            
        total_7mm_8mm_weight = float(sum(_7mm_8mm_weight))

    if _8mm_9mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_8mm_9mm_rice)-1):
            _8mm_9mm_weight.append(model.predict([[float(_8mm_9mm_rice[i]["Length"]),float(_8mm_9mm_rice[i]["Width"])]]))
            
        total_8mm_9mm_weight = float(sum(_8mm_9mm_weight))

    if _9mm_10mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_9mm_10mm_rice)-1):
            _9mm_10mm_weight.append(model.predict([[float(_9mm_10mm_rice[i]["Length"]),float(_9mm_10mm_rice[i]["Width"])]]))
            
        total_9mm_10mm_weight = float(sum(_9mm_10mm_weight))

    if _1mm_2mm_rice:
        _1mm_2mm_agl = float(round(sum(x['Length12']for x in _1mm_2mm_rice)/len(_1mm_2mm_rice), 3))
    if _2mm_3mm_rice:
        _2mm_3mm_agl = float(round(sum(x['Length12']for x in _2mm_3mm_rice)/len(_2mm_3mm_rice), 3))
    if _3mm_4mm_rice:
        _3mm_4mm_agl = float(round(sum(x['Length12']for x in _3mm_4mm_rice)/len(_3mm_4mm_rice), 3))
    if _4mm_5mm_rice:
        _4mm_5mm_agl = float(round(sum(x['Length12']for x in _4mm_5mm_rice)/len(_4mm_5mm_rice), 3))
    if _5mm_6mm_rice:
        _5mm_6mm_agl = float(round(sum(x['Length12']for x in _5mm_6mm_rice)/len(_5mm_6mm_rice), 3))
    if _6mm_7mm_rice:
        _6mm_7mm_agl = float(round(sum(x['Length12']for x in _6mm_7mm_rice)/len(_6mm_7mm_rice), 3))
    if _7mm_8mm_rice:
        _7mm_8mm_agl = float(round(sum(x['Length12']for x in _7mm_8mm_rice)/len(_7mm_8mm_rice), 3))
    if _8mm_9mm_rice:
        _8mm_9mm_agl = float(round(sum(x['Length12']for x in _8mm_9mm_rice)/len(_8mm_9mm_rice), 3))
    if _9mm_10mm_rice:
        _9mm_10mm_agl = float(round(sum(x['Length12']for x in _9mm_10mm_rice)/len(_9mm_10mm_rice), 3))

    # Ahsan adding head_rice AGL in report

    head_rice_AGL = float(round(sum(x['Length12']for x in head_rice)/len(head_rice), 3))
    head_rice_AGL = head_rice_AGL
    print("This is head_rice AGL", head_rice_AGL)
    

    for i in range(0, len(head_rice)-1):
        #print("\n\n\nThis is first element's Length & Width of head_rice",head_rice[i]["Length"],head_rice[i]["Width"])
        #global head_weight

        nm = model.predict(
            [[float(head_rice[i]["Length"]), float(head_rice[i]["Width"])]])
        head_weight.append(nm)
    # head_weight.append(round((((-0.00860)+(0.00167*head_rice[i]["Length"]))+(0.00663*head_rice[i]["Width"])),5)) Muzammil commented
    # head_weight.append(round((((-0.00860)+(0.00188*head_rice[i]["Length"]))+(0.00680*head_rice[i]["Width"])),5))old

    #total_head_weight = float(round(sum(head_weight),3))
    total_head_weight = float(sum(head_weight))
    #print("\n\nThis is total weight of head_rice",total_head_weight)

    for i in range(0, len(broken_rice)-1):

        nm1 = model.predict(
            [[float(broken_rice[i]["Length"]), float(broken_rice[i]["Width"])]])
        broken_rice_weight.append(nm1)
        # broken_rice_weight.append(round((((-0.00860)+(0.00167*broken_rice[i]["Length"]))+(0.00663*broken_rice[i]["Width"])),5))

    total_brokenRice_weight = float(sum(broken_rice_weight))
    #print("\n\nThis is total weight of long_broken_rice",total_brokenRice_weight)

    global Total_new_weight
    Total_new_weight = float(total_head_weight + total_brokenRice_weight)
    #print("This is total_new_weight",Total_new_weight)

    # leena
    if long_broken_list:  # if the list is not empty then do following
        for i in range(0, len(long_broken_list)-1):
            long_broken_weight.append(model.predict(
                [[float(long_broken_list[i]["Length"]), float(long_broken_list[i]["Width"])]]))
            # long_broken_weight.append(round((((-0.00994)+(0.00167*long_broken_list[i]["Length"]))+(0.00663*long_broken_list[i]["Width"])),5))

        total_long_broken_weight = float(sum(long_broken_weight))
        #print("This is total_new_weight of long broken ",total_long_broken_weight)

    if medium_broken_list:
        for i in range(0, len(medium_broken_list)-1):
            medium_broken_weight.append(model.predict(
                [[float(medium_broken_list[i]["Length"]), float(medium_broken_list[i]["Width"])]]))
            # medium_broken_weight.append(round((((-0.00994)+(0.00167*medium_broken_list[i]["Length"]))+(0.00663*medium_broken_list[i]["Width"])),5))

        total_medium_broken_weight = float(sum(medium_broken_weight))
        #print("This is total_new_weight of medium broken",total_medium_broken_weight)

    if small_broken_list:
        for i in range(0, len(small_broken_list)-1):
            small_broken_weight.append(model.predict(
                [[float(small_broken_list[i]["Length"]), float(small_broken_list[i]["Width"])]]))
            # small_broken_weight.append(round((((-0.00994)+(0.00167*small_broken_list[i]["Length"]))+(0.00663*small_broken_list[i]["Width"])),5))

        total_small_broken_weight = float(sum(small_broken_weight))
        #print("This is total_new_weight of small broken",total_small_broken_weight)
#####

    #print("\n\n\nEnd of for loop")

    ## Making the logic of weighted average for head rice & broken rice ##
        ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
        ##   Start  ##

    from analysis_irri6 import yellow_length, yellow_width
    for i, j in zip(yellow_length, yellow_width):
        yellow_weight.append(model.predict([[float(i), float(j)]]))
        # yellow_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    #total_yellow_weight = round(sum(yellow_weight),3)
    global total_yellow_weight
    total_yellow_weight = round(float(sum(yellow_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    ## Making the logic of weighted average for damage rice ##
    ##   Start  ##

    from analysis_irri6 import damage_length, damage_width
    for i, j in zip(damage_length, damage_width):
        damage_weight.append(model.predict([[float(i), float(j)]]))
        # damage_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_damage_weight
    total_damage_weight = round(float(sum(damage_weight)), 3)
    #print("\n\nThis is total weight of damage",total_damage_weight)

    ## Making the logic of weighted average for damage rice ##
    ##   End  ##

    ## Making the logic of weighted average for chalky rice ##
    ##   Start  ##

    from analysis_irri6 import chalky_length, chalky_width
    for i, j in zip(chalky_length, chalky_width):
        chalky_weight.append(model.predict([[float(i), float(j)]]))
        # chalky_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_chalky_weight
    total_chalky_weight = round(float(sum(chalky_weight)), 3)
    #print("\n\nThis is total weight of chalky",total_chalky_weight)

    ## Making the logic of weighted average for chalky rice ##
    ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
    ##   Start  ##

    from analysis_irri6 import paddy_length, paddy_width
    for i, j in zip(paddy_length, paddy_width):
        paddy_weight.append(model.predict([[float(i), float(j)]]))
        # paddy_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    total_paddy_weight = round(float(sum(paddy_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    head = round(len(head_rice))

    long = round(len(broken_rice))

    # Report generation with mm Reference

    # (calculate_value.result3 == 'No-AGL') and
    if (len(get_user_input.result1) != 0):

        from analysis_irri6 import yellow_count, chalky_count, new_damage1_count, paddy_count
        global paddy_percentage, yellow_percentage, chalky_percentage, damage_percentage, _1mm_2mm_percentage,_2mm_3mm_percentage,_3mm_4mm_percentage,_4mm_5mm_percentage
        global _5mm_6mm_percentage, _6mm_7mm_percentage,_7mm_8mm_percentage, _8mm_9mm_percentage, _9mm_10mm_percentage
        yellow_percentage = round(
            float(total_yellow_weight/Total_new_weight), 2)
        chalky_percentage = round(
            float(total_chalky_weight/Total_new_weight), 2)
        damage_percentage = round(
            float(total_damage_weight/Total_new_weight), 2)
        paddy_percentage = round(float(total_paddy_weight/Total_new_weight), 2)
        #Muzammil adding
        _1mm_2mm_percentage = round(float(total_1mm_2mm_weight/Total_new_weight),2)
        _2mm_3mm_percentage = round(float(total_2mm_3mm_weight/Total_new_weight),2)
        _3mm_4mm_percentage = round(float(total_3mm_4mm_weight/Total_new_weight),2)
        _4mm_5mm_percentage = round(float(total_4mm_5mm_weight/Total_new_weight),2)
        _5mm_6mm_percentage = round(float(total_5mm_6mm_weight/Total_new_weight),2)
        _6mm_7mm_percentage = round(float(total_6mm_7mm_weight/Total_new_weight),2)
        _7mm_8mm_percentage = round(float(total_7mm_8mm_weight/Total_new_weight),2)
        _8mm_9mm_percentage = round(float(total_8mm_9mm_weight/Total_new_weight),2)
        _9mm_10mm_percentage = round(float(total_9mm_10mm_weight/Total_new_weight),2)

        # leena
        data3 = [['Sample No', get_sampleNo.input],
                 ['Date', get_date.input],
                 ['Time', get_day.input],
                 ['Arrival No', get_arrivalNo.input],
                 ['Party Name', get_partyName.input],
                 ['Vehicle No', get_vehicleNo.input],
                 ['Rice Type', get_riceType.input],
                 ['Moisture', get_moisture.input],
                 ['Look', get_look.input]
                 ]
        ###
        # removing 0.14 in agl
        data2 = [[Time, Date], [' Variables        ', ' Values  '], ['Average Length (10g) (mm)      ', round(avg_length, 3)],
                 ['Average Width (10g) (mm)        ', round(avg_width, 3)],
                 ['Head Rice AGL       ', round(head_rice_AGL, 3)],
                 ['Whole Grain (qty)      ', head],
                 ['Whole Grain Weight (gm)     ', round(total_head_weight, 3)],
                 ['Broken Grain   (qty)      ', long],
                 ['Broken Grain Weight (gm)     ', round(
                     total_brokenRice_weight, 3)],
                 ['Total Grains (qty)    ', total_grains],
                 ['Reference Value (100g) (mm)',    x],
                 ['Yellow Grains (qty)    ', yellow_count],
                 ['Yellow Grains Weight (gm)    ', total_yellow_weight],
                 ['Yellow Percengate (%)    ', round(
                     (yellow_percentage*100), 3)],
                 ['Chalky Grains (qty)    ', chalky_count],
                 ['Chalky Grains Weight (gm)    ', total_chalky_weight],
                 ['Chalky Percengate (%)    ', round(
                     (chalky_percentage*100), 3)],
                 ['Damage Grains (qty)    ', new_damage1_count],
                 ['Damage Grains Weight (gm)    ', total_damage_weight],
                 ['Damage Percengate (%)    ', round(
                     (damage_percentage*100), 3)],
                 ['Paddy Grains (qty)    ', paddy_count],
                 ['Paddy Grains Weight (gm)    ', total_paddy_weight],
                 ['Paddy Percengate (%)    ', (paddy_percentage*100)],
                 ['Total Weight (gm)',    round(Total_new_weight, 3)],
                 ['Broken Rice Percengate',    round(
                     ((total_brokenRice_weight/Total_new_weight)*100), 3)],
                 ['Long Broken Weight', round(total_long_broken_weight, 3)],
                 ['Medium Broken Weight', round(
                     total_medium_broken_weight, 3)],
                 ['Small Broken Weight', round(total_small_broken_weight, 3)]
                 ]


        data4 = [['Range', "Count", "Average Length(AGL)", "Percent by Weight %"],
                 ["1mm to 2mm", _1mm_2mm, _1mm_2mm_agl, (_1mm_2mm_percentage*100)],
                 ["2mm to 3mm", _2mm_3mm, _2mm_3mm_agl, (_2mm_3mm_percentage*100)],
                 ["3mm to 4mm", _3mm_4mm, _3mm_4mm_agl, (_3mm_4mm_percentage*100)],
                 ["4mm to 5mm", _4mm_5mm, _4mm_5mm_agl, (_4mm_5mm_percentage*100)],
                 ["5mm to 6mm", _5mm_6mm, _5mm_6mm_agl, (_5mm_6mm_percentage*100)],
                 ["6mm to 7mm", _6mm_7mm, _6mm_7mm_agl, (_6mm_7mm_percentage*100)],
                 ["7mm to 8mm", _7mm_8mm, _7mm_8mm_agl, (_7mm_8mm_percentage*100)],
                 ["8mm to 9mm", _8mm_9mm, _8mm_9mm_agl, (_8mm_9mm_percentage*100)],
                 ["9mm to 10mm", _9mm_10mm, _9mm_10mm_agl, (_9mm_10mm_percentage*100)],
                 ]

    table2 = Table(data2, colWidths=[170, 150],
                   rowHeights=22.1)  # rowHeights=24.2
    table2.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    # leena
    ldata = (len(head_rice), len(broken_rice),
             len(med_broken), len(small_broken))
    ####

    cdata = (0, 1, 2, 3)
    tdata = (gtype[0], gtype[1], gtype[2], gtype[3])

    table2.wrapOn(c, 20, 400)  # 20,400, to set
    # c,20,15,,, to set report alignment increase or decrease the last value
    table2.drawOn(c, 20, 15)

    # leena
    # for user defined values
    table3 = Table(data3, colWidths=[100, 130], rowHeights=30)
    table3.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    table3.wrapOn(c, 20, 400)  # 20,400
    table3.drawOn(c, 360, 330)  # c,360,360
    ##

    c.showPage()

    # leena
    # for user defined values
    img = "img/header2.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    table4 = Table(data4, colWidths=[100, 130], rowHeights=30)
    table4.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BACKGROUND',(0,0),(4,0),colors.lightskyblue) # (row start, column end), (row start, coulmn end)
    ]))

    table4.wrapOn(c, 20, 400)  # 20,400
    table4.drawOn(c, 70, 350)  # c,x,y
    ##

    c.save()


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -----------------------------1121 Report------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def gen_report_1121(objects, S_Report):
    #print(">>>>>>>>>> Sumarize report for 1121 >>>>>>>>>>>>>")
    import time

    gtype = [0, 0, 0, 0]
    global ldata, cdata, tdata, Date, Time
    head = 0
    long = 0
    med = 0
    small = 0

    ## Making the logic of weighted average for head rice & broken rice ##
    ## Initializing variables ##
    #global broken_weight, final_weight

    head_weight = []
    broken_rice_weight = []
    yellow_weight = []
    damage_weight = []
    chalky_weight = []
    paddy_weight = []
    head_rice = []
    broken_rice = []

    # leena
    long_broken = []
    med_broken = []
    small_broken = []

    long_broken_list = []
    medium_broken_list = []
    small_broken_list = []

    long_broken_weight = []
    medium_broken_weight = []
    small_broken_weight = []

    total_long_broken_weight = 0
    total_medium_broken_weight = 0
    total_small_broken_weight = 0

    #Muzammil adding 1mm to 10mm analysis
    _1mm_2mm = 0
    _2mm_3mm = 0
    _3mm_4mm = 0
    _4mm_5mm = 0
    _5mm_6mm = 0
    _6mm_7mm = 0
    _7mm_8mm = 0
    _8mm_9mm = 0
    _9mm_10mm = 0


    _1mm_2mm_weight = []
    _2mm_3mm_weight = []
    _3mm_4mm_weight = []
    _4mm_5mm_weight = []
    _5mm_6mm_weight = []
    _6mm_7mm_weight = []
    _7mm_8mm_weight = []
    _8mm_9mm_weight = []
    _9mm_10mm_weight = []


    _1mm_2mm_rice = []
    _2mm_3mm_rice = []
    _3mm_4mm_rice = []
    _4mm_5mm_rice = []
    _5mm_6mm_rice = []
    _6mm_7mm_rice = []
    _7mm_8mm_rice = []
    _8mm_9mm_rice = []
    _9mm_10mm_rice = []


    total_1mm_2mm_weight = 0
    total_2mm_3mm_weight = 0
    total_3mm_4mm_weight = 0
    total_4mm_5mm_weight = 0
    total_5mm_6mm_weight = 0
    total_6mm_7mm_weight = 0
    total_7mm_8mm_weight = 0
    total_8mm_9mm_weight = 0
    total_9mm_10mm_weight = 0


    _1mm_2mm_agl = 0
    _2mm_3mm_agl = 0
    _3mm_4mm_agl = 0
    _4mm_5mm_agl = 0
    _5mm_6mm_agl = 0
    _6mm_7mm_agl = 0
    _7mm_8mm_agl = 0
    _8mm_9mm_agl = 0
    _9mm_10mm_agl = 0

    if globals.called is not 1:
        # if values are empty in that case
        get_sampleNo.input = "-"
        get_date.input = "-"
        get_day.input = "-"
        get_arrivalNo.input = "-"
        get_partyName.input = "-"
        get_vehicleNo.input = "-"
        get_riceType.input = "-"
        get_moisture.input = "-"
        get_look.input = "-"
        ##

    whole_kernel = []
    PAGE_HEIGHT = defaultPageSize[0]
    PAGE_WIDTH = defaultPageSize[0]
    DefaultPageSize = letter
    c = canvas.Canvas(S_Report, DefaultPageSize)

    # leena
    img = "img/header.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    ##

    form = c.acroForm
    import datetime
    now = datetime.datetime.now()
    now.strftime("%A")
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")
    c.setFont("Helvetica", 12)
    Time = "Test time : %s" % time
    c.setFont("Helvetica", 12)
    Date = "Test date : %s" % date

    global total_grains
    total_grains = len(objects)

    avg_length = float(round(sum(x['Length1']
                       for x in objects)/len(objects), 3))
    avg_width = float(round(sum(x['Width'] for x in objects)/len(objects), 2))
    #avg_area = round(sum(x['Area'] for x in objects)/len(objects),2)

    for i in objects:

        # Calculations for whole/broken ratio

        # (calculate_value.result3 == 'No-AGL') and
        if (len(get_user_input.result1) != 0):

            #print("The user input for mm field exists. Not taking AGL as reference")
            #print("The input variable is: ",get_user_input.result1)
            #print("The length of variable is: ",len(get_user_input.result1))
            global x
            x = get_user_input.result1
            # print("\n\n\n")
            if (float(i['Length1']) >= float((x))):
                #print( "{} >= {}".format(float(i['Length']), float((x))) )
                head_rice.append(i)
            elif(float(i['Length1']) < float((x))):
                #print( "{} < {}".format(float(i['Length']), float((x))) )
                broken_rice.append(i)
            # print("\n\n\n")

##
# (calculate_value.result3 == 'AGL') and len(get_user_input2.result2) != 0
# elif ( (get_user_input.result1) == "" ):
##
# print("The user input for % field exists. Taking AGL as reference")
##
##            from reportnew import AGL
##
##            temp_AGL = AGL
# print("100 Grain test ran",temp_AGL)
##
##
##            x = float(get_user_input2.result2)/float(100)
# print("The percentage is:", x)
# j = (float(avg_length)*float(x))
##            j = (float(temp_AGL)*float(x))
##
# if (float((i['Length'])) >= (j)):
# head_rice.append(i)
# elif(float((i['Length'])) < (j)):
# broken_rice.append(i)

            # and (get_user_input2.result2) == ""
        elif ((get_user_input.result1) == ""):

            #print("The user inputs for both fields do not exist. By defaul input is 75%")

            x = 3/4
            y = 1/2
            z = 1/4

            # print(x,y,z)

            if (i['Length1'] >= avg_length*(x)):
                head_rice.append(i)
            elif((i['Length1'] < avg_length*(x)) and (i['Length1'] > avg_length*(y))):
                broken_rice.append(i)
            elif((i['Length1'] <= avg_length*(y)) and (i['Length1'] > avg_length*(z))):
                broken_rice.append(i)
            elif(i['Length1'] <= (z)):
                broken_rice.append(i)

    ## Making the logic of weighted average for head rice & broken rice ##
                ##   Start  ##

    #final_weight = 0

    #print("This is head rice array items",head_rice)
    #print("This is broken rice array items",broken_rice)

    # leena
    if broken_rice:
        #print("broken rice list here")
        # print(broken_rice)
        for brokenRice_element in broken_rice:
            if not get_input_LongBroken.Max is "" or not get_input_LongBroken.Min is "":
                if(float(get_input_LongBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_LongBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_LongBroken.Max), brokenRice_element["Length"] ,float(get_input_LongBroken.Min)))
                    #print("long broken rice detected")
                    long_broken_list.append(brokenRice_element)

            if not get_input_MediumBroken.Max is "" or not get_input_MediumBroken.Min is "":
                if(float(get_input_MediumBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_MediumBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_MediumBroken.Max), brokenRice_element["Length"] ,float(get_input_MediumBroken.Min)))
                    #print(" Medium broken rice detected")
                    # if particular item need to be added then brokenRice_element["Length"]
                    medium_broken_list.append(brokenRice_element)

            if not get_input_SmallBroken.Max is "" or not get_input_SmallBroken.Min is "":
                if(float(get_input_SmallBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_SmallBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_SmallBroken.Max), brokenRice_element["Length"] ,float(get_input_SmallBroken.Min)))
                    #print(" Small broken rice detected")
                    small_broken_list.append(brokenRice_element)
    ##############
    #Muzammil adding 1mm to 10mm analysis

    for i in objects:
        if i["Length1"] >= 1 and i["Length1"] <= 2:
            _1mm_2mm = _1mm_2mm + 1
            _1mm_2mm_rice.append(i)
        
        elif i["Length1"] >= 2 and i["Length1"] <= 3:
            _2mm_3mm = _2mm_3mm + 1
            _2mm_3mm_rice.append(i)

        elif i["Length1"] >= 3 and i["Length1"] <= 4:
            _3mm_4mm = _3mm_4mm +1
            _3mm_4mm_rice.append(i)

        elif i["Length1"] >= 4 and i["Length1"] <= 5:
            _4mm_5mm = _4mm_5mm +1
            _4mm_5mm_rice.append(i)

        elif i["Length1"] >= 5 and i["Length1"] <= 6:
            _5mm_6mm = _5mm_6mm +1
            _5mm_6mm_rice.append(i)

        elif i["Length1"] >= 6 and i["Length1"] <= 7:
            _6mm_7mm = _6mm_7mm + 1
            _6mm_7mm_rice.append(i)
        
        elif i["Length1"] >= 7 and i["Length1"] <= 8:
            _7mm_8mm = _7mm_8mm + 1
            _7mm_8mm_rice.append(i)
        
        elif i["Length1"] >= 8 and i["Length1"] <= 9:
            _8mm_9mm = _8mm_9mm + 1
            _8mm_9mm_rice.append(i)

        elif i["Length1"] >= 9 and i["Length1"] <= 10:
            _9mm_10mm = _9mm_10mm + 1
            _9mm_10mm_rice.append(i)



    if _1mm_2mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_1mm_2mm_rice)-1):
            _1mm_2mm_weight.append(model.predict([[float(_1mm_2mm_rice[i]["Length"]),float(_1mm_2mm_rice[i]["Width"])]]))
            
        total_1mm_2mm_weight = float(sum(_1mm_2mm_weight))

    if _2mm_3mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_2mm_3mm_rice)-1):
            _2mm_3mm_weight.append(model.predict([[float(_2mm_3mm_rice[i]["Length"]),float(_2mm_3mm_rice[i]["Width"])]]))
            
        total_2mm_3mm_weight = float(sum(_2mm_3mm_weight))

    if _3mm_4mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_3mm_4mm_rice)-1):
            _3mm_4mm_weight.append(model.predict([[float(_3mm_4mm_rice[i]["Length"]),float(_3mm_4mm_rice[i]["Width"])]]))
            
        total_3mm_4mm_weight = float(sum(_3mm_4mm_weight))
    
    if _4mm_5mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_4mm_5mm_rice)-1):
            _4mm_5mm_weight.append(model.predict([[float(_4mm_5mm_rice[i]["Length"]),float(_4mm_5mm_rice[i]["Width"])]]))
            
        total_4mm_5mm_weight = float(sum(_4mm_5mm_weight))
    
    if _5mm_6mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_5mm_6mm_rice)-1):
            _5mm_6mm_weight.append(model.predict([[float(_5mm_6mm_rice[i]["Length"]),float(_5mm_6mm_rice[i]["Width"])]]))
            
        total_5mm_6mm_weight = float(sum(_5mm_6mm_weight))

    if _6mm_7mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_6mm_7mm_rice)-1):
            _6mm_7mm_weight.append(model.predict([[float(_6mm_7mm_rice[i]["Length"]),float(_6mm_7mm_rice[i]["Width"])]]))
            
        total_6mm_7mm_weight = float(sum(_6mm_7mm_weight))

    if _7mm_8mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_7mm_8mm_rice)-1):
            _7mm_8mm_weight.append(model.predict([[float(_7mm_8mm_rice[i]["Length"]),float(_7mm_8mm_rice[i]["Width"])]]))
            
        total_7mm_8mm_weight = float(sum(_7mm_8mm_weight))

    if _8mm_9mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_8mm_9mm_rice)-1):
            _8mm_9mm_weight.append(model.predict([[float(_8mm_9mm_rice[i]["Length"]),float(_8mm_9mm_rice[i]["Width"])]]))
            
        total_8mm_9mm_weight = float(sum(_8mm_9mm_weight))

    if _9mm_10mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_9mm_10mm_rice)-1):
            _9mm_10mm_weight.append(model.predict([[float(_9mm_10mm_rice[i]["Length"]),float(_9mm_10mm_rice[i]["Width"])]]))
            
        total_9mm_10mm_weight = float(sum(_9mm_10mm_weight))

    if _1mm_2mm_rice:
        _1mm_2mm_agl = float(round(sum(x['Length1']for x in _1mm_2mm_rice)/len(_1mm_2mm_rice), 3))
    if _2mm_3mm_rice:
        _2mm_3mm_agl = float(round(sum(x['Length1']for x in _2mm_3mm_rice)/len(_2mm_3mm_rice), 3))
    if _3mm_4mm_rice:
        _3mm_4mm_agl = float(round(sum(x['Length1']for x in _3mm_4mm_rice)/len(_3mm_4mm_rice), 3))
    if _4mm_5mm_rice:
        _4mm_5mm_agl = float(round(sum(x['Length1']for x in _4mm_5mm_rice)/len(_4mm_5mm_rice), 3))
    if _5mm_6mm_rice:
        _5mm_6mm_agl = float(round(sum(x['Length1']for x in _5mm_6mm_rice)/len(_5mm_6mm_rice), 3))
    if _6mm_7mm_rice:
        _6mm_7mm_agl = float(round(sum(x['Length1']for x in _6mm_7mm_rice)/len(_6mm_7mm_rice), 3))
    if _7mm_8mm_rice:
        _7mm_8mm_agl = float(round(sum(x['Length1']for x in _7mm_8mm_rice)/len(_7mm_8mm_rice), 3))
    if _8mm_9mm_rice:
        _8mm_9mm_agl = float(round(sum(x['Length1']for x in _8mm_9mm_rice)/len(_8mm_9mm_rice), 3))
    if _9mm_10mm_rice:
        _9mm_10mm_agl = float(round(sum(x['Length1']for x in _9mm_10mm_rice)/len(_9mm_10mm_rice), 3))

    # Ahsan adding head_rice AGL in report

    head_rice_AGL = float(round(sum(x['Length1']
                          for x in head_rice)/len(head_rice), 3))
    head_rice_AGL = head_rice_AGL
    print("This is head_rice AGL", head_rice_AGL)
    #model = tf.keras.models.load_model('w.h5')

    for i in range(0, len(head_rice)-1):
        #print("\n\n\nThis is first element's Length & Width of head_rice",head_rice[i]["Length"],head_rice[i]["Width"])
        #global head_weight

        nm = model.predict(
            [[float(head_rice[i]["Length"]), float(head_rice[i]["Width"])]])
        head_weight.append(nm)
    # head_weight.append(round((((-0.00860)+(0.00167*head_rice[i]["Length"]))+(0.00663*head_rice[i]["Width"])),5)) Muzammil commented
    # head_weight.append(round((((-0.00860)+(0.00188*head_rice[i]["Length"]))+(0.00680*head_rice[i]["Width"])),5))old

    #total_head_weight = float(round(sum(head_weight),3))
    total_head_weight = float(sum(head_weight))
    #print("\n\nThis is total weight of head_rice",total_head_weight)

    for i in range(0, len(broken_rice)-1):

        nm1 = model.predict(
            [[float(broken_rice[i]["Length"]), float(broken_rice[i]["Width"])]])
        broken_rice_weight.append(nm1)
        # broken_rice_weight.append(round((((-0.00860)+(0.00167*broken_rice[i]["Length"]))+(0.00663*broken_rice[i]["Width"])),5))

    total_brokenRice_weight = float(sum(broken_rice_weight))
    #print("\n\nThis is total weight of long_broken_rice",total_brokenRice_weight)

    global Total_new_weight
    Total_new_weight = float(total_head_weight + total_brokenRice_weight)
    #print("This is total_new_weight",Total_new_weight)

    # leena
    if long_broken_list:  # if the list is not empty then do following
        for i in range(0, len(long_broken_list)-1):
            long_broken_weight.append(model.predict(
                [[float(long_broken_list[i]["Length"]), float(long_broken_list[i]["Width"])]]))
            # long_broken_weight.append(round((((-0.00994)+(0.00167*long_broken_list[i]["Length"]))+(0.00663*long_broken_list[i]["Width"])),5))

        total_long_broken_weight = float(sum(long_broken_weight))
        #print("This is total_new_weight of long broken ",total_long_broken_weight)

    if medium_broken_list:
        for i in range(0, len(medium_broken_list)-1):
            medium_broken_weight.append(model.predict(
                [[float(medium_broken_list[i]["Length"]), float(medium_broken_list[i]["Width"])]]))
            # medium_broken_weight.append(round((((-0.00994)+(0.00167*medium_broken_list[i]["Length"]))+(0.00663*medium_broken_list[i]["Width"])),5))

        total_medium_broken_weight = float(sum(medium_broken_weight))
        #print("This is total_new_weight of medium broken",total_medium_broken_weight)

    if small_broken_list:
        for i in range(0, len(small_broken_list)-1):
            small_broken_weight.append(model.predict(
                [[float(small_broken_list[i]["Length"]), float(small_broken_list[i]["Width"])]]))
            # small_broken_weight.append(round((((-0.00994)+(0.00167*small_broken_list[i]["Length"]))+(0.00663*small_broken_list[i]["Width"])),5))

        total_small_broken_weight = float(sum(small_broken_weight))
        #print("This is total_new_weight of small broken",total_small_broken_weight)
#####

    #print("\n\n\nEnd of for loop")

    ## Making the logic of weighted average for head rice & broken rice ##
        ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
        ##   Start  ##

    from analysis_1121 import yellow_length, yellow_width
    for i, j in zip(yellow_length, yellow_width):
        yellow_weight.append(model.predict([[float(i), float(j)]]))
        # yellow_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    #total_yellow_weight = round(sum(yellow_weight),3)
    global total_yellow_weight
    total_yellow_weight = round(float(sum(yellow_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    ## Making the logic of weighted average for damage rice ##
    ##   Start  ##

    from analysis_1121 import damage_length, damage_width
    for i, j in zip(damage_length, damage_width):
        damage_weight.append(model.predict([[float(i), float(j)]]))
        # damage_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_damage_weight
    total_damage_weight = round(float(sum(damage_weight)), 3)
    #print("\n\nThis is total weight of damage",total_damage_weight)

    ## Making the logic of weighted average for damage rice ##
    ##   End  ##

    ## Making the logic of weighted average for chalky rice ##
    ##   Start  ##

    from analysis_1121 import chalky_length, chalky_width
    for i, j in zip(chalky_length, chalky_width):
        chalky_weight.append(model.predict([[float(i), float(j)]]))
        # chalky_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_chalky_weight
    total_chalky_weight = round(float(sum(chalky_weight)), 3)
    #print("\n\nThis is total weight of chalky",total_chalky_weight)

    ## Making the logic of weighted average for chalky rice ##
    ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
    ##   Start  ##

    from analysis_1121 import paddy_length, paddy_width
    for i, j in zip(paddy_length, paddy_width):
        paddy_weight.append(model.predict([[float(i), float(j)]]))
        # paddy_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    total_paddy_weight = round(float(sum(paddy_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    head = round(len(head_rice))

    long = round(len(broken_rice))

    # Report generation with mm Reference

    # (calculate_value.result3 == 'No-AGL') and
    if (len(get_user_input.result1) != 0):

        from analysis_1121 import yellow_count, chalky_count, new_damage1_count, paddy_count
        global paddy_percentage, yellow_percentage, chalky_percentage, damage_percentage
        yellow_percentage = round(
            float(total_yellow_weight/Total_new_weight), 2)
        chalky_percentage = round(
            float(total_chalky_weight/Total_new_weight), 2)
        damage_percentage = round(
            float(total_damage_weight/Total_new_weight), 2)
        paddy_percentage = round(float(total_paddy_weight/Total_new_weight), 2)

        #Muzammil adding
        #Muzammil adding
        _1mm_2mm_percentage = round(float(total_1mm_2mm_weight/Total_new_weight),2)
        _2mm_3mm_percentage = round(float(total_2mm_3mm_weight/Total_new_weight),2)
        _3mm_4mm_percentage = round(float(total_3mm_4mm_weight/Total_new_weight),2)
        _4mm_5mm_percentage = round(float(total_4mm_5mm_weight/Total_new_weight),2)
        _5mm_6mm_percentage = round(float(total_5mm_6mm_weight/Total_new_weight),2)
        _6mm_7mm_percentage = round(float(total_6mm_7mm_weight/Total_new_weight),2)
        _7mm_8mm_percentage = round(float(total_7mm_8mm_weight/Total_new_weight),2)
        _8mm_9mm_percentage = round(float(total_8mm_9mm_weight/Total_new_weight),2)
        _9mm_10mm_percentage = round(float(total_9mm_10mm_weight/Total_new_weight),2)

        # leena
        data3 = [['Sample No', get_sampleNo.input],
                 ['Date', get_date.input],
                 ['Time', get_day.input],
                 ['Arrival No', get_arrivalNo.input],
                 ['Party Name', get_partyName.input],
                 ['Vehicle No', get_vehicleNo.input],
                 ['Rice Type', get_riceType.input],
                 ['Moisture', get_moisture.input],
                 ['Look', get_look.input]
                 ]
        ###
        # removing 0.14 in agl
        data2 = [[Time, Date], [' Variables        ', ' Values  '], ['Average Length (10g) (mm)      ', round(avg_length, 3)],
                 ['Average Width (10g) (mm)        ', round(avg_width, 3)],
                 ['Head Rice AGL       ', round(head_rice_AGL, 3)],
                 ['Whole Grain (qty)      ', head],
                 ['Whole Grain Weight (gm)     ', round(total_head_weight, 3)],
                 ['Broken Grain   (qty)      ', long],
                 ['Broken Grain Weight (gm)     ', round(
                     total_brokenRice_weight, 3)],
                 ['Total Grains (qty)    ', total_grains],
                 ['Reference Value (100g) (mm)',    x],
                 ['Yellow Grains (qty)    ', yellow_count],
                 ['Yellow Grains Weight (gm)    ', total_yellow_weight],
                 ['Yellow Percengate (%)    ', round(
                     (yellow_percentage*100), 3)],
                 ['Chalky Grains (qty)    ', chalky_count],
                 ['Chalky Grains Weight (gm)    ', total_chalky_weight],
                 ['Chalky Percengate (%)    ', round(
                     (chalky_percentage*100), 3)],
                 ['Damage Grains (qty)    ', new_damage1_count],
                 ['Damage Grains Weight (gm)    ', total_damage_weight],
                 ['Damage Percengate (%)    ', round(
                     (damage_percentage*100), 3)],
                 ['Paddy Grains (qty)    ', paddy_count],
                 ['Paddy Grains Weight (gm)    ', total_paddy_weight],
                 ['Paddy Percengate (%)    ', (paddy_percentage*100)],
                 ['Total Weight (gm)',    round(Total_new_weight, 3)],
                 ['Broken Rice Percengate',    round(
                     ((total_brokenRice_weight/Total_new_weight)*100), 3)],
                 ['Long Broken Weight', round(total_long_broken_weight, 3)],
                 ['Medium Broken Weight', round(
                     total_medium_broken_weight, 3)],
                 ['Small Broken Weight', round(total_small_broken_weight, 3)]
                 ]

        data4 = [['Range', "Count", "Average Length(AGL)", "Percent by Weight %"],
                 ["1mm to 2mm", _1mm_2mm, _1mm_2mm_agl, (_1mm_2mm_percentage*100)],
                 ["2mm to 3mm", _2mm_3mm, _2mm_3mm_agl, (_2mm_3mm_percentage*100)],
                 ["3mm to 4mm", _3mm_4mm, _3mm_4mm_agl, (_3mm_4mm_percentage*100)],
                 ["4mm to 5mm", _4mm_5mm, _4mm_5mm_agl, (_4mm_5mm_percentage*100)],
                 ["5mm to 6mm", _5mm_6mm, _5mm_6mm_agl, (_5mm_6mm_percentage*100)],
                 ["6mm to 7mm", _6mm_7mm, _6mm_7mm_agl, (_6mm_7mm_percentage*100)],
                 ["7mm to 8mm", _7mm_8mm, _7mm_8mm_agl, (_7mm_8mm_percentage*100)],
                 ["8mm to 9mm", _8mm_9mm, _8mm_9mm_agl, (_8mm_9mm_percentage*100)],
                 ["9mm to 10mm", _9mm_10mm, _9mm_10mm_agl, (_9mm_10mm_percentage*100)],
                 ]

    table2 = Table(data2, colWidths=[170, 150],
                   rowHeights=22.1)  # rowHeights=24.2
    table2.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    # leena
    ldata = (len(head_rice), len(broken_rice),
             len(med_broken), len(small_broken))
    ####

    cdata = (0, 1, 2, 3)
    tdata = (gtype[0], gtype[1], gtype[2], gtype[3])

    table2.wrapOn(c, 20, 400)  # 20,400, to set
    # c,20,25,,, to set report alignment increase or decrease the last value
    table2.drawOn(c, 20, 15)

    # leena
    # for user defined values
    table3 = Table(data3, colWidths=[100, 130], rowHeights=30)
    table3.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    table3.wrapOn(c, 20, 400)  # 20,400
    table3.drawOn(c, 360, 360)  # c,160,260


    c.showPage()

    # leena
    # for user defined values
    img = "img/header2.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    table4 = Table(data4, colWidths=[100, 130], rowHeights=30)
    table4.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BACKGROUND',(0,0),(4,0),colors.lightskyblue) # (row start, column end), (row start, coulmn end)
    ]))

    table4.wrapOn(c, 20, 400)  # 20,400
    table4.drawOn(c, 70, 350)  # c,x,y
    ##

    ##

    c.save()


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -----------------------------PK-386 Report------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


def gen_report_pk386(objects, S_Report):
    print(">>>>>>>>>> Sumarize report for pk386 >>>>>>>>>>>>>")
    import time

    gtype = [0, 0, 0, 0]
    global ldata, cdata, tdata, Date, Time
    head = 0
    long = 0
    med = 0
    small = 0

    ## Making the logic of weighted average for head rice & broken rice ##
    ## Initializing variables ##
    #global broken_weight, final_weight

    head_weight = []
    broken_rice_weight = []
    yellow_weight = []
    damage_weight = []
    chalky_weight = []
    paddy_weight = []
    head_rice = []
    broken_rice = []

    # leena
    long_broken = []
    med_broken = []
    small_broken = []

    long_broken_list = []
    medium_broken_list = []
    small_broken_list = []

    long_broken_weight = []
    medium_broken_weight = []
    small_broken_weight = []

    total_long_broken_weight = 0
    total_medium_broken_weight = 0
    total_small_broken_weight = 0


    #Muzammil adding 1mm to 10mm analysis
    _1mm_2mm = 0
    _2mm_3mm = 0
    _3mm_4mm = 0
    _4mm_5mm = 0
    _5mm_6mm = 0
    _6mm_7mm = 0
    _7mm_8mm = 0
    _8mm_9mm = 0
    _9mm_10mm = 0


    _1mm_2mm_weight = []
    _2mm_3mm_weight = []
    _3mm_4mm_weight = []
    _4mm_5mm_weight = []
    _5mm_6mm_weight = []
    _6mm_7mm_weight = []
    _7mm_8mm_weight = []
    _8mm_9mm_weight = []
    _9mm_10mm_weight = []


    _1mm_2mm_rice = []
    _2mm_3mm_rice = []
    _3mm_4mm_rice = []
    _4mm_5mm_rice = []
    _5mm_6mm_rice = []
    _6mm_7mm_rice = []
    _7mm_8mm_rice = []
    _8mm_9mm_rice = []
    _9mm_10mm_rice = []


    total_1mm_2mm_weight = 0
    total_2mm_3mm_weight = 0
    total_3mm_4mm_weight = 0
    total_4mm_5mm_weight = 0
    total_5mm_6mm_weight = 0
    total_6mm_7mm_weight = 0
    total_7mm_8mm_weight = 0
    total_8mm_9mm_weight = 0
    total_9mm_10mm_weight = 0


    _1mm_2mm_agl = 0
    _2mm_3mm_agl = 0
    _3mm_4mm_agl = 0
    _4mm_5mm_agl = 0
    _5mm_6mm_agl = 0
    _6mm_7mm_agl = 0
    _7mm_8mm_agl = 0
    _8mm_9mm_agl = 0
    _9mm_10mm_agl = 0

    if globals.called is not 1:
        # if values are empty in that case
        get_sampleNo.input = "-"
        get_date.input = "-"
        get_day.input = "-"
        get_arrivalNo.input = "-"
        get_partyName.input = "-"
        get_vehicleNo.input = "-"
        get_riceType.input = "-"
        get_moisture.input = "-"
        get_look.input = "-"
        ##

    whole_kernel = []
    PAGE_HEIGHT = defaultPageSize[0]
    PAGE_WIDTH = defaultPageSize[0]
    DefaultPageSize = letter
    c = canvas.Canvas(S_Report, DefaultPageSize)

    # leena
    img = "img/header.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    ##

    form = c.acroForm
    import datetime
    now = datetime.datetime.now()
    now.strftime("%A")
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")
    c.setFont("Helvetica", 12)
    Time = "Test time : %s" % time
    c.setFont("Helvetica", 12)
    Date = "Test date : %s" % date

    global total_grains
    total_grains = len(objects)

    avg_length = float(round(sum(x['Length1']
                       for x in objects)/len(objects), 3))
    avg_width = float(round(sum(x['Width'] for x in objects)/len(objects), 2))
    #avg_area = round(sum(x['Area'] for x in objects)/len(objects),2)

    for i in objects:

        # Calculations for whole/broken ratio

        # (calculate_value.result3 == 'No-AGL') and
        if (len(get_user_input.result1) != 0):

            #print("The user input for mm field exists. Not taking AGL as reference")
            #print("The input variable is: ",get_user_input.result1)
            #print("The length of variable is: ",len(get_user_input.result1))
            global x
            x = get_user_input.result1
            # print("\n\n\n")
            if (float(i['Length1']) >= float((x))):
                #print( "{} >= {}".format(float(i['Length']), float((x))) )
                head_rice.append(i)
            elif(float(i['Length1']) < float((x))):
                #print( "{} < {}".format(float(i['Length']), float((x))) )
                broken_rice.append(i)
            # print("\n\n\n")

##
# (calculate_value.result3 == 'AGL') and len(get_user_input2.result2) != 0
# elif ( (get_user_input.result1) == "" ):
##
# print("The user input for % field exists. Taking AGL as reference")
##
##            from reportnew import AGL
##
##            temp_AGL = AGL
# print("100 Grain test ran",temp_AGL)
##
##
##            x = float(get_user_input2.result2)/float(100)
# print("The percentage is:", x)
# j = (float(avg_length)*float(x))
##            j = (float(temp_AGL)*float(x))
##
# if (float((i['Length'])) >= (j)):
# head_rice.append(i)
# elif(float((i['Length'])) < (j)):
# broken_rice.append(i)

            # and (get_user_input2.result2) == ""
        elif ((get_user_input.result1) == ""):

            #print("The user inputs for both fields do not exist. By defaul input is 75%")

            x = 3/4
            y = 1/2
            z = 1/4

            # print(x,y,z)

            if (i['Length1'] >= avg_length*(x)):
                head_rice.append(i)
            elif((i['Length1'] < avg_length*(x)) and (i['Length1'] > avg_length*(y))):
                broken_rice.append(i)
            elif((i['Length1'] <= avg_length*(y)) and (i['Length1'] > avg_length*(z))):
                broken_rice.append(i)
            elif(i['Length1'] <= (z)):
                broken_rice.append(i)

    ## Making the logic of weighted average for head rice & broken rice ##
                ##   Start  ##

    #final_weight = 0

    #print("This is head rice array items",head_rice)
    #print("This is broken rice array items",broken_rice)

    # leena
    if broken_rice:
        #print("broken rice list here")
        # print(broken_rice)
        for brokenRice_element in broken_rice:
            if not get_input_LongBroken.Max is "" or not get_input_LongBroken.Min is "":
                if(float(get_input_LongBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_LongBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_LongBroken.Max), brokenRice_element["Length"] ,float(get_input_LongBroken.Min)))
                    #print("long broken rice detected")
                    long_broken_list.append(brokenRice_element)

            if not get_input_MediumBroken.Max is "" or not get_input_MediumBroken.Min is "":
                if(float(get_input_MediumBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_MediumBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_MediumBroken.Max), brokenRice_element["Length"] ,float(get_input_MediumBroken.Min)))
                    #print(" Medium broken rice detected")
                    # if particular item need to be added then brokenRice_element["Length"]
                    medium_broken_list.append(brokenRice_element)

            if not get_input_SmallBroken.Max is "" or not get_input_SmallBroken.Min is "":
                if(float(get_input_SmallBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_SmallBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_SmallBroken.Max), brokenRice_element["Length"] ,float(get_input_SmallBroken.Min)))
                    #print(" Small broken rice detected")
                    small_broken_list.append(brokenRice_element)
    ##############

    #Muzammil adding 1mm to 10mm analysis

    for i in objects:
        if i["Length1"] >= 1 and i["Length1"] <= 2:
            _1mm_2mm = _1mm_2mm + 1
            _1mm_2mm_rice.append(i)
        
        elif i["Length1"] >= 2 and i["Length1"] <= 3:
            _2mm_3mm = _2mm_3mm + 1
            _2mm_3mm_rice.append(i)

        elif i["Length1"] >= 3 and i["Length1"] <= 4:
            _3mm_4mm = _3mm_4mm +1
            _3mm_4mm_rice.append(i)

        elif i["Length1"] >= 4 and i["Length1"] <= 5:
            _4mm_5mm = _4mm_5mm +1
            _4mm_5mm_rice.append(i)

        elif i["Length1"] >= 5 and i["Length1"] <= 6:
            _5mm_6mm = _5mm_6mm +1
            _5mm_6mm_rice.append(i)

        elif i["Length1"] >= 6 and i["Length1"] <= 7:
            _6mm_7mm = _6mm_7mm + 1
            _6mm_7mm_rice.append(i)
        
        elif i["Length1"] >= 7 and i["Length1"] <= 8:
            _7mm_8mm = _7mm_8mm + 1
            _7mm_8mm_rice.append(i)
        
        elif i["Length1"] >= 8 and i["Length1"] <= 9:
            _8mm_9mm = _8mm_9mm + 1
            _8mm_9mm_rice.append(i)

        elif i["Length1"] >= 9 and i["Length1"] <= 10:
            _9mm_10mm = _9mm_10mm + 1
            _9mm_10mm_rice.append(i)



    if _1mm_2mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_1mm_2mm_rice)-1):
            _1mm_2mm_weight.append(model.predict([[float(_1mm_2mm_rice[i]["Length"]),float(_1mm_2mm_rice[i]["Width"])]]))
            
        total_1mm_2mm_weight = float(sum(_1mm_2mm_weight))

    if _2mm_3mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_2mm_3mm_rice)-1):
            _2mm_3mm_weight.append(model.predict([[float(_2mm_3mm_rice[i]["Length"]),float(_2mm_3mm_rice[i]["Width"])]]))
            
        total_2mm_3mm_weight = float(sum(_2mm_3mm_weight))

    if _3mm_4mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_3mm_4mm_rice)-1):
            _3mm_4mm_weight.append(model.predict([[float(_3mm_4mm_rice[i]["Length"]),float(_3mm_4mm_rice[i]["Width"])]]))
            
        total_3mm_4mm_weight = float(sum(_3mm_4mm_weight))
    
    if _4mm_5mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_4mm_5mm_rice)-1):
            _4mm_5mm_weight.append(model.predict([[float(_4mm_5mm_rice[i]["Length"]),float(_4mm_5mm_rice[i]["Width"])]]))
            
        total_4mm_5mm_weight = float(sum(_4mm_5mm_weight))
    
    if _5mm_6mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_5mm_6mm_rice)-1):
            _5mm_6mm_weight.append(model.predict([[float(_5mm_6mm_rice[i]["Length"]),float(_5mm_6mm_rice[i]["Width"])]]))
            
        total_5mm_6mm_weight = float(sum(_5mm_6mm_weight))

    if _6mm_7mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_6mm_7mm_rice)-1):
            _6mm_7mm_weight.append(model.predict([[float(_6mm_7mm_rice[i]["Length"]),float(_6mm_7mm_rice[i]["Width"])]]))
            
        total_6mm_7mm_weight = float(sum(_6mm_7mm_weight))

    if _7mm_8mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_7mm_8mm_rice)-1):
            _7mm_8mm_weight.append(model.predict([[float(_7mm_8mm_rice[i]["Length"]),float(_7mm_8mm_rice[i]["Width"])]]))
            
        total_7mm_8mm_weight = float(sum(_7mm_8mm_weight))

    if _8mm_9mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_8mm_9mm_rice)-1):
            _8mm_9mm_weight.append(model.predict([[float(_8mm_9mm_rice[i]["Length"]),float(_8mm_9mm_rice[i]["Width"])]]))
            
        total_8mm_9mm_weight = float(sum(_8mm_9mm_weight))

    if _9mm_10mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_9mm_10mm_rice)-1):
            _9mm_10mm_weight.append(model.predict([[float(_9mm_10mm_rice[i]["Length"]),float(_9mm_10mm_rice[i]["Width"])]]))
            
        total_9mm_10mm_weight = float(sum(_9mm_10mm_weight))



    if _1mm_2mm_rice:
        _1mm_2mm_agl = float(round(sum(x['Length1']for x in _1mm_2mm_rice)/len(_1mm_2mm_rice), 3))
    if _2mm_3mm_rice:
        _2mm_3mm_agl = float(round(sum(x['Length1']for x in _2mm_3mm_rice)/len(_2mm_3mm_rice), 3))
    if _3mm_4mm_rice:
        _3mm_4mm_agl = float(round(sum(x['Length1']for x in _3mm_4mm_rice)/len(_3mm_4mm_rice), 3))
    if _4mm_5mm_rice:
        _4mm_5mm_agl = float(round(sum(x['Length1']for x in _4mm_5mm_rice)/len(_4mm_5mm_rice), 3))
    if _5mm_6mm_rice:
        _5mm_6mm_agl = float(round(sum(x['Length1']for x in _5mm_6mm_rice)/len(_5mm_6mm_rice), 3))
    if _6mm_7mm_rice:
        _6mm_7mm_agl = float(round(sum(x['Length1']for x in _6mm_7mm_rice)/len(_6mm_7mm_rice), 3))
    if _7mm_8mm_rice:
        _7mm_8mm_agl = float(round(sum(x['Length1']for x in _7mm_8mm_rice)/len(_7mm_8mm_rice), 3))
    if _8mm_9mm_rice:
        _8mm_9mm_agl = float(round(sum(x['Length1']for x in _8mm_9mm_rice)/len(_8mm_9mm_rice), 3))
    if _9mm_10mm_rice:
        _9mm_10mm_agl = float(round(sum(x['Length1']for x in _9mm_10mm_rice)/len(_9mm_10mm_rice), 3))

    # Ahsan adding head_rice AGL in report

    head_rice_AGL = float(round(sum(x['Length1']
                          for x in head_rice)/len(head_rice), 3))
    head_rice_AGL = head_rice_AGL
    print("This is head_rice AGL", head_rice_AGL)
    #model = tf.keras.models.load_model('w.h5')

    for i in range(0, len(head_rice)-1):
        #print("\n\n\nThis is first element's Length & Width of head_rice",head_rice[i]["Length"],head_rice[i]["Width"])
        #global head_weight

        nm = model.predict(
            [[float(head_rice[i]["Length"]), float(head_rice[i]["Width"])]])
        head_weight.append(nm)
    # head_weight.append(round((((-0.00860)+(0.00167*head_rice[i]["Length"]))+(0.00663*head_rice[i]["Width"])),5)) Muzammil commented
    # head_weight.append(round((((-0.00860)+(0.00188*head_rice[i]["Length"]))+(0.00680*head_rice[i]["Width"])),5))old

    #total_head_weight = float(round(sum(head_weight),3))
    total_head_weight = float(sum(head_weight))
    #print("\n\nThis is total weight of head_rice",total_head_weight)

    for i in range(0, len(broken_rice)-1):

        nm1 = model.predict(
            [[float(broken_rice[i]["Length"]), float(broken_rice[i]["Width"])]])
        broken_rice_weight.append(nm1)
        # broken_rice_weight.append(round((((-0.00860)+(0.00167*broken_rice[i]["Length"]))+(0.00663*broken_rice[i]["Width"])),5))

    total_brokenRice_weight = float(sum(broken_rice_weight))
    #print("\n\nThis is total weight of long_broken_rice",total_brokenRice_weight)

    global Total_new_weight
    Total_new_weight = float(total_head_weight + total_brokenRice_weight)
    #print("This is total_new_weight",Total_new_weight)

    # leena
    if long_broken_list:  # if the list is not empty then do following
        for i in range(0, len(long_broken_list)-1):
            long_broken_weight.append(model.predict(
                [[float(long_broken_list[i]["Length"]), float(long_broken_list[i]["Width"])]]))
            # long_broken_weight.append(round((((-0.00994)+(0.00167*long_broken_list[i]["Length"]))+(0.00663*long_broken_list[i]["Width"])),5))

        total_long_broken_weight = float(sum(long_broken_weight))
        #print("This is total_new_weight of long broken ",total_long_broken_weight)

    if medium_broken_list:
        for i in range(0, len(medium_broken_list)-1):
            medium_broken_weight.append(model.predict(
                [[float(medium_broken_list[i]["Length"]), float(medium_broken_list[i]["Width"])]]))
            # medium_broken_weight.append(round((((-0.00994)+(0.00167*medium_broken_list[i]["Length"]))+(0.00663*medium_broken_list[i]["Width"])),5))

        total_medium_broken_weight = float(sum(medium_broken_weight))
        #print("This is total_new_weight of medium broken",total_medium_broken_weight)

    if small_broken_list:
        for i in range(0, len(small_broken_list)-1):
            small_broken_weight.append(model.predict(
                [[float(small_broken_list[i]["Length"]), float(small_broken_list[i]["Width"])]]))
            # small_broken_weight.append(round((((-0.00994)+(0.00167*small_broken_list[i]["Length"]))+(0.00663*small_broken_list[i]["Width"])),5))

        total_small_broken_weight = float(sum(small_broken_weight))
        #print("This is total_new_weight of small broken",total_small_broken_weight)
#####

    #print("\n\n\nEnd of for loop")

    ## Making the logic of weighted average for head rice & broken rice ##
        ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
        ##   Start  ##

    from analysis_pk386 import yellow_length, yellow_width
    for i, j in zip(yellow_length, yellow_width):
        yellow_weight.append(model.predict([[float(i), float(j)]]))
        # yellow_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    #total_yellow_weight = round(sum(yellow_weight),3)
    global total_yellow_weight
    total_yellow_weight = round(float(sum(yellow_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    ## Making the logic of weighted average for damage rice ##
    ##   Start  ##

    from analysis_pk386 import damage_length, damage_width
    for i, j in zip(damage_length, damage_width):
        damage_weight.append(model.predict([[float(i), float(j)]]))
        # damage_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_damage_weight
    total_damage_weight = round(float(sum(damage_weight)), 3)
    #print("\n\nThis is total weight of damage",total_damage_weight)

    ## Making the logic of weighted average for damage rice ##
    ##   End  ##

    ## Making the logic of weighted average for chalky rice ##
    ##   Start  ##

    from analysis_pk386 import chalky_length, chalky_width
    for i, j in zip(chalky_length, chalky_width):
        chalky_weight.append(model.predict([[float(i), float(j)]]))
        # chalky_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_chalky_weight
    total_chalky_weight = round(float(sum(chalky_weight)), 3)
    #print("\n\nThis is total weight of chalky",total_chalky_weight)

    ## Making the logic of weighted average for chalky rice ##
    ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
    ##   Start  ##

    from analysis_pk386 import paddy_length, paddy_width
    for i, j in zip(paddy_length, paddy_width):
        paddy_weight.append(model.predict([[float(i), float(j)]]))
        # paddy_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    total_paddy_weight = round(float(sum(paddy_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    head = round(len(head_rice))

    long = round(len(broken_rice))

    # Report generation with mm Reference

    # (calculate_value.result3 == 'No-AGL') and
    if (len(get_user_input.result1) != 0):

        from analysis_pk386 import yellow_count, chalky_count, new_damage1_count, paddy_count
        global paddy_percentage, yellow_percentage, chalky_percentage, damage_percentage
        yellow_percentage = round(
            float(total_yellow_weight/Total_new_weight), 2)
        chalky_percentage = round(
            float(total_chalky_weight/Total_new_weight), 2)
        damage_percentage = round(
            float(total_damage_weight/Total_new_weight), 2)
        paddy_percentage = round(float(total_paddy_weight/Total_new_weight), 2)

        #Muzammil adding
        #Muzammil adding
        _1mm_2mm_percentage = round(float(total_1mm_2mm_weight/Total_new_weight),2)
        _2mm_3mm_percentage = round(float(total_2mm_3mm_weight/Total_new_weight),2)
        _3mm_4mm_percentage = round(float(total_3mm_4mm_weight/Total_new_weight),2)
        _4mm_5mm_percentage = round(float(total_4mm_5mm_weight/Total_new_weight),2)
        _5mm_6mm_percentage = round(float(total_5mm_6mm_weight/Total_new_weight),2)
        _6mm_7mm_percentage = round(float(total_6mm_7mm_weight/Total_new_weight),2)
        _7mm_8mm_percentage = round(float(total_7mm_8mm_weight/Total_new_weight),2)
        _8mm_9mm_percentage = round(float(total_8mm_9mm_weight/Total_new_weight),2)
        _9mm_10mm_percentage = round(float(total_9mm_10mm_weight/Total_new_weight),2)

        # leena
        data3 = [['Sample No', get_sampleNo.input],
                 ['Date', get_date.input],
                 ['Time', get_day.input],
                 ['Arrival No', get_arrivalNo.input],
                 ['Party Name', get_partyName.input],
                 ['Vehicle No', get_vehicleNo.input],
                 ['Rice Type', get_riceType.input],
                 ['Moisture', get_moisture.input],
                 ['Look', get_look.input]
                 ]
        ###
        # removing 0.14 in agl
        data2 = [[Time, Date], [' Variables        ', ' Values  '], ['Average Length (10g) (mm)      ', round(avg_length, 3)],
                 ['Average Width (10g) (mm)        ', round(avg_width, 3)],
                 ['Head Rice AGL       ', round(head_rice_AGL, 3)],
                 ['Whole Grain (qty)      ', head],
                 ['Whole Grain Weight (gm)     ', round(total_head_weight, 3)],
                 ['Broken Grain   (qty)      ', long],
                 ['Broken Grain Weight (gm)     ', round(
                     total_brokenRice_weight, 3)],
                 ['Total Grains (qty)    ', total_grains],
                 ['Reference Value (100g) (mm)',    x],
                 ['Yellow Grains (qty)    ', yellow_count],
                 ['Yellow Grains Weight (gm)    ', total_yellow_weight],
                 ['Yellow Percengate (%)    ', round(
                     (yellow_percentage*100), 3)],
                 ['Chalky Grains (qty)    ', chalky_count],
                 ['Chalky Grains Weight (gm)    ', total_chalky_weight],
                 ['Chalky Percengate (%)    ', round(
                     (chalky_percentage*100), 3)],
                 ['Damage Grains (qty)    ', new_damage1_count],
                 ['Damage Grains Weight (gm)    ', total_damage_weight],
                 ['Damage Percengate (%)    ', round(
                     (damage_percentage*100), 3)],
                 ['Paddy Grains (qty)    ', paddy_count],
                 ['Paddy Grains Weight (gm)    ', total_paddy_weight],
                 ['Paddy Percengate (%)    ', (paddy_percentage*100)],
                 ['Total Weight (gm)',    round(Total_new_weight, 3)],
                 ['Broken Rice Percengate',    round(
                     ((total_brokenRice_weight/Total_new_weight)*100), 3)],
                 ['Long Broken Weight', round(total_long_broken_weight, 3)],
                 ['Medium Broken Weight', round(
                     total_medium_broken_weight, 3)],
                 ['Small Broken Weight', round(total_small_broken_weight, 3)]
                 ]

        data4 = [['Range', "Count", "Average Length(AGL)", "Percent by Weight %"],
                 ["1mm to 2mm", _1mm_2mm, _1mm_2mm_agl, (_1mm_2mm_percentage*100)],
                 ["2mm to 3mm", _2mm_3mm, _2mm_3mm_agl, (_2mm_3mm_percentage*100)],
                 ["3mm to 4mm", _3mm_4mm, _3mm_4mm_agl, (_3mm_4mm_percentage*100)],
                 ["4mm to 5mm", _4mm_5mm, _4mm_5mm_agl, (_4mm_5mm_percentage*100)],
                 ["5mm to 6mm", _5mm_6mm, _5mm_6mm_agl, (_5mm_6mm_percentage*100)],
                 ["6mm to 7mm", _6mm_7mm, _6mm_7mm_agl, (_6mm_7mm_percentage*100)],
                 ["7mm to 8mm", _7mm_8mm, _7mm_8mm_agl, (_7mm_8mm_percentage*100)],
                 ["8mm to 9mm", _8mm_9mm, _8mm_9mm_agl, (_8mm_9mm_percentage*100)],
                 ["9mm to 10mm", _9mm_10mm, _9mm_10mm_agl, (_9mm_10mm_percentage*100)],
                 ]

    table2 = Table(data2, colWidths=[170, 150],
                   rowHeights=22.1)  # rowHeights=24.2
    table2.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    # leena
    ldata = (len(head_rice), len(broken_rice),
             len(med_broken), len(small_broken))
    ####

    cdata = (0, 1, 2, 3)
    tdata = (gtype[0], gtype[1], gtype[2], gtype[3])

    table2.wrapOn(c, 20, 400)  # 20,400, to set
    # c,20,25,,, to set report alignment increase or decrease the last value
    table2.drawOn(c, 20, 15)

    # leena
    # for user defined values
    table3 = Table(data3, colWidths=[100, 130], rowHeights=30)
    table3.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    table3.wrapOn(c, 20, 400)  # 20,400
    table3.drawOn(c, 360, 360)  # c,160,260
    ##

    c.showPage()

    # leena
    # for user defined values
    img = "img/header2.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    table4 = Table(data4, colWidths=[100, 130], rowHeights=30)
    table4.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BACKGROUND',(0,0),(4,0),colors.lightskyblue) # (row start, column end), (row start, coulmn end)
    ]))

    table4.wrapOn(c, 20, 400)  # 20,400
    table4.drawOn(c, 70, 350)  # c,x,y
    ##

    c.save()


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -----------------------------Brown Report------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


def gen_report_brown(objects, S_Report):
    print(">>>>>>>>>> Sumarize report for brown >>>>>>>>>>>>>")
    import time

    gtype = [0, 0, 0, 0]
    global ldata, cdata, tdata, Date, Time
    head = 0
    long = 0
    med = 0
    small = 0

    ## Making the logic of weighted average for head rice & broken rice ##
    ## Initializing variables ##
    #global broken_weight, final_weight

    head_weight = []
    broken_rice_weight = []
    yellow_weight = []
    damage_weight = []
    chalky_weight = []
    paddy_weight = []
    head_rice = []
    broken_rice = []

    # leena
    long_broken = []
    med_broken = []
    small_broken = []

    long_broken_list = []
    medium_broken_list = []
    small_broken_list = []

    long_broken_weight = []
    medium_broken_weight = []
    small_broken_weight = []

    total_long_broken_weight = 0
    total_medium_broken_weight = 0
    total_small_broken_weight = 0



    #Muzammil adding 1mm to 10mm analysis
    _1mm_2mm = 0
    _2mm_3mm = 0
    _3mm_4mm = 0
    _4mm_5mm = 0
    _5mm_6mm = 0
    _6mm_7mm = 0
    _7mm_8mm = 0
    _8mm_9mm = 0
    _9mm_10mm = 0


    _1mm_2mm_weight = []
    _2mm_3mm_weight = []
    _3mm_4mm_weight = []
    _4mm_5mm_weight = []
    _5mm_6mm_weight = []
    _6mm_7mm_weight = []
    _7mm_8mm_weight = []
    _8mm_9mm_weight = []
    _9mm_10mm_weight = []


    _1mm_2mm_rice = []
    _2mm_3mm_rice = []
    _3mm_4mm_rice = []
    _4mm_5mm_rice = []
    _5mm_6mm_rice = []
    _6mm_7mm_rice = []
    _7mm_8mm_rice = []
    _8mm_9mm_rice = []
    _9mm_10mm_rice = []


    total_1mm_2mm_weight = 0
    total_2mm_3mm_weight = 0
    total_3mm_4mm_weight = 0
    total_4mm_5mm_weight = 0
    total_5mm_6mm_weight = 0
    total_6mm_7mm_weight = 0
    total_7mm_8mm_weight = 0
    total_8mm_9mm_weight = 0
    total_9mm_10mm_weight = 0


    _1mm_2mm_agl = 0
    _2mm_3mm_agl = 0
    _3mm_4mm_agl = 0
    _4mm_5mm_agl = 0
    _5mm_6mm_agl = 0
    _6mm_7mm_agl = 0
    _7mm_8mm_agl = 0
    _8mm_9mm_agl = 0
    _9mm_10mm_agl = 0


    if globals.called is not 1:
        # if values are empty in that case
        get_sampleNo.input = "-"
        get_date.input = "-"
        get_day.input = "-"
        get_arrivalNo.input = "-"
        get_partyName.input = "-"
        get_vehicleNo.input = "-"
        get_riceType.input = "-"
        get_moisture.input = "-"
        get_look.input = "-"
        ##

    whole_kernel = []
    PAGE_HEIGHT = defaultPageSize[0]
    PAGE_WIDTH = defaultPageSize[0]
    DefaultPageSize = letter
    c = canvas.Canvas(S_Report, DefaultPageSize)

    # leena
    img = "img/header.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    ##

    form = c.acroForm
    import datetime
    now = datetime.datetime.now()
    now.strftime("%A")
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")
    c.setFont("Helvetica", 12)
    Time = "Test time : %s" % time
    c.setFont("Helvetica", 12)
    Date = "Test date : %s" % date

    global total_grains
    total_grains = len(objects)

    avg_length = float(round(sum(x['Length1']
                       for x in objects)/len(objects), 3))
    avg_width = float(round(sum(x['Width'] for x in objects)/len(objects), 2))
    #avg_area = round(sum(x['Area'] for x in objects)/len(objects),2)

    for i in objects:

        # Calculations for whole/broken ratio

        # (calculate_value.result3 == 'No-AGL') and
        if (len(get_user_input.result1) != 0):

            #print("The user input for mm field exists. Not taking AGL as reference")
            #print("The input variable is: ",get_user_input.result1)
            #print("The length of variable is: ",len(get_user_input.result1))
            global x
            x = get_user_input.result1
            # print("\n\n\n")
            if (float(i['Length1']) >= float((x))):
                #print( "{} >= {}".format(float(i['Length']), float((x))) )
                head_rice.append(i)
            elif(float(i['Length1']) < float((x))):
                #print( "{} < {}".format(float(i['Length']), float((x))) )
                broken_rice.append(i)
            # print("\n\n\n")

##
# (calculate_value.result3 == 'AGL') and len(get_user_input2.result2) != 0
# elif ( (get_user_input.result1) == "" ):
##
# print("The user input for % field exists. Taking AGL as reference")
##
##            from reportnew import AGL
##
##            temp_AGL = AGL
# print("100 Grain test ran",temp_AGL)
##
##
##            x = float(get_user_input2.result2)/float(100)
# print("The percentage is:", x)
# j = (float(avg_length)*float(x))
##            j = (float(temp_AGL)*float(x))
##
# if (float((i['Length'])) >= (j)):
# head_rice.append(i)
# elif(float((i['Length'])) < (j)):
# broken_rice.append(i)

            # and (get_user_input2.result2) == ""
        elif ((get_user_input.result1) == ""):

            #print("The user inputs for both fields do not exist. By defaul input is 75%")

            x = 3/4
            y = 1/2
            z = 1/4

            # print(x,y,z)

            if (i['Length1'] >= avg_length*(x)):
                head_rice.append(i)
            elif((i['Length1'] < avg_length*(x)) and (i['Length1'] > avg_length*(y))):
                broken_rice.append(i)
            elif((i['Length1'] <= avg_length*(y)) and (i['Length1'] > avg_length*(z))):
                broken_rice.append(i)
            elif(i['Length1'] <= (z)):
                broken_rice.append(i)

    ## Making the logic of weighted average for head rice & broken rice ##
                ##   Start  ##

    #final_weight = 0

    #print("This is head rice array items",head_rice)
    #print("This is broken rice array items",broken_rice)

    # leena
    if broken_rice:
        #print("broken rice list here")
        # print(broken_rice)
        for brokenRice_element in broken_rice:
            if not get_input_LongBroken.Max is "" or not get_input_LongBroken.Min is "":
                if(float(get_input_LongBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_LongBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_LongBroken.Max), brokenRice_element["Length"] ,float(get_input_LongBroken.Min)))
                    #print("long broken rice detected")
                    long_broken_list.append(brokenRice_element)

            if not get_input_MediumBroken.Max is "" or not get_input_MediumBroken.Min is "":
                if(float(get_input_MediumBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_MediumBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_MediumBroken.Max), brokenRice_element["Length"] ,float(get_input_MediumBroken.Min)))
                    #print(" Medium broken rice detected")
                    # if particular item need to be added then brokenRice_element["Length"]
                    medium_broken_list.append(brokenRice_element)

            if not get_input_SmallBroken.Max is "" or not get_input_SmallBroken.Min is "":
                if(float(get_input_SmallBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_SmallBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_SmallBroken.Max), brokenRice_element["Length"] ,float(get_input_SmallBroken.Min)))
                    #print(" Small broken rice detected")
                    small_broken_list.append(brokenRice_element)
    ##############

    #Muzammil adding 1mm to 10mm analysis

    for i in objects:
        if i["Length1"] >= 1 and i["Length1"] <= 2:
            _1mm_2mm = _1mm_2mm + 1
            _1mm_2mm_rice.append(i)
        
        elif i["Length1"] >= 2 and i["Length1"] <= 3:
            _2mm_3mm = _2mm_3mm + 1
            _2mm_3mm_rice.append(i)

        elif i["Length1"] >= 3 and i["Length1"] <= 4:
            _3mm_4mm = _3mm_4mm +1
            _3mm_4mm_rice.append(i)

        elif i["Length1"] >= 4 and i["Length1"] <= 5:
            _4mm_5mm = _4mm_5mm +1
            _4mm_5mm_rice.append(i)

        elif i["Length1"] >= 5 and i["Length1"] <= 6:
            _5mm_6mm = _5mm_6mm +1
            _5mm_6mm_rice.append(i)

        elif i["Length1"] >= 6 and i["Length1"] <= 7:
            _6mm_7mm = _6mm_7mm + 1
            _6mm_7mm_rice.append(i)
        
        elif i["Length1"] >= 7 and i["Length1"] <= 8:
            _7mm_8mm = _7mm_8mm + 1
            _7mm_8mm_rice.append(i)
        
        elif i["Length1"] >= 8 and i["Length1"] <= 9:
            _8mm_9mm = _8mm_9mm + 1
            _8mm_9mm_rice.append(i)

        elif i["Length1"] >= 9 and i["Length1"] <= 10:
            _9mm_10mm = _9mm_10mm + 1
            _9mm_10mm_rice.append(i)



    if _1mm_2mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_1mm_2mm_rice)-1):
            _1mm_2mm_weight.append(model.predict([[float(_1mm_2mm_rice[i]["Length"]),float(_1mm_2mm_rice[i]["Width"])]]))
            
        total_1mm_2mm_weight = float(sum(_1mm_2mm_weight))

    if _2mm_3mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_2mm_3mm_rice)-1):
            _2mm_3mm_weight.append(model.predict([[float(_2mm_3mm_rice[i]["Length"]),float(_2mm_3mm_rice[i]["Width"])]]))
            
        total_2mm_3mm_weight = float(sum(_2mm_3mm_weight))

    if _3mm_4mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_3mm_4mm_rice)-1):
            _3mm_4mm_weight.append(model.predict([[float(_3mm_4mm_rice[i]["Length"]),float(_3mm_4mm_rice[i]["Width"])]]))
            
        total_3mm_4mm_weight = float(sum(_3mm_4mm_weight))
    
    if _4mm_5mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_4mm_5mm_rice)-1):
            _4mm_5mm_weight.append(model.predict([[float(_4mm_5mm_rice[i]["Length"]),float(_4mm_5mm_rice[i]["Width"])]]))
            
        total_4mm_5mm_weight = float(sum(_4mm_5mm_weight))
    
    if _5mm_6mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_5mm_6mm_rice)-1):
            _5mm_6mm_weight.append(model.predict([[float(_5mm_6mm_rice[i]["Length"]),float(_5mm_6mm_rice[i]["Width"])]]))
            
        total_5mm_6mm_weight = float(sum(_5mm_6mm_weight))

    if _6mm_7mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_6mm_7mm_rice)-1):
            _6mm_7mm_weight.append(model.predict([[float(_6mm_7mm_rice[i]["Length"]),float(_6mm_7mm_rice[i]["Width"])]]))
            
        total_6mm_7mm_weight = float(sum(_6mm_7mm_weight))

    if _7mm_8mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_7mm_8mm_rice)-1):
            _7mm_8mm_weight.append(model.predict([[float(_7mm_8mm_rice[i]["Length"]),float(_7mm_8mm_rice[i]["Width"])]]))
            
        total_7mm_8mm_weight = float(sum(_7mm_8mm_weight))

    if _8mm_9mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_8mm_9mm_rice)-1):
            _8mm_9mm_weight.append(model.predict([[float(_8mm_9mm_rice[i]["Length"]),float(_8mm_9mm_rice[i]["Width"])]]))
            
        total_8mm_9mm_weight = float(sum(_8mm_9mm_weight))

    if _9mm_10mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_9mm_10mm_rice)-1):
            _9mm_10mm_weight.append(model.predict([[float(_9mm_10mm_rice[i]["Length"]),float(_9mm_10mm_rice[i]["Width"])]]))
            
        total_9mm_10mm_weight = float(sum(_9mm_10mm_weight))



    if _1mm_2mm_rice:
        _1mm_2mm_agl = float(round(sum(x['Length1']for x in _1mm_2mm_rice)/len(_1mm_2mm_rice), 3))
    if _2mm_3mm_rice:
        _2mm_3mm_agl = float(round(sum(x['Length1']for x in _2mm_3mm_rice)/len(_2mm_3mm_rice), 3))
    if _3mm_4mm_rice:
        _3mm_4mm_agl = float(round(sum(x['Length1']for x in _3mm_4mm_rice)/len(_3mm_4mm_rice), 3))
    if _4mm_5mm_rice:
        _4mm_5mm_agl = float(round(sum(x['Length1']for x in _4mm_5mm_rice)/len(_4mm_5mm_rice), 3))
    if _5mm_6mm_rice:
        _5mm_6mm_agl = float(round(sum(x['Length1']for x in _5mm_6mm_rice)/len(_5mm_6mm_rice), 3))
    if _6mm_7mm_rice:
        _6mm_7mm_agl = float(round(sum(x['Length1']for x in _6mm_7mm_rice)/len(_6mm_7mm_rice), 3))
    if _7mm_8mm_rice:
        _7mm_8mm_agl = float(round(sum(x['Length1']for x in _7mm_8mm_rice)/len(_7mm_8mm_rice), 3))
    if _8mm_9mm_rice:
        _8mm_9mm_agl = float(round(sum(x['Length1']for x in _8mm_9mm_rice)/len(_8mm_9mm_rice), 3))
    if _9mm_10mm_rice:
        _9mm_10mm_agl = float(round(sum(x['Length1']for x in _9mm_10mm_rice)/len(_9mm_10mm_rice), 3))



    # Ahsan adding head_rice AGL in report

    head_rice_AGL = float(round(sum(x['Length1']
                          for x in head_rice)/len(head_rice), 3))
    head_rice_AGL = head_rice_AGL
    print("This is head_rice AGL", head_rice_AGL)
    #model = tf.keras.models.load_model('w.h5')

    for i in range(0, len(head_rice)-1):
        #print("\n\n\nThis is first element's Length & Width of head_rice",head_rice[i]["Length"],head_rice[i]["Width"])
        #global head_weight

        nm = model.predict(
            [[float(head_rice[i]["Length"]), float(head_rice[i]["Width"])]])
        head_weight.append(nm)
    # head_weight.append(round((((-0.00860)+(0.00167*head_rice[i]["Length"]))+(0.00663*head_rice[i]["Width"])),5)) Muzammil commented
    # head_weight.append(round((((-0.00860)+(0.00188*head_rice[i]["Length"]))+(0.00680*head_rice[i]["Width"])),5))old

    #total_head_weight = float(round(sum(head_weight),3))
    total_head_weight = float(sum(head_weight))
    #print("\n\nThis is total weight of head_rice",total_head_weight)

    for i in range(0, len(broken_rice)-1):

        nm1 = model.predict(
            [[float(broken_rice[i]["Length"]), float(broken_rice[i]["Width"])]])
        broken_rice_weight.append(nm1)
        # broken_rice_weight.append(round((((-0.00860)+(0.00167*broken_rice[i]["Length"]))+(0.00663*broken_rice[i]["Width"])),5))

    total_brokenRice_weight = float(sum(broken_rice_weight))
    #print("\n\nThis is total weight of long_broken_rice",total_brokenRice_weight)

    global Total_new_weight
    Total_new_weight = float(total_head_weight + total_brokenRice_weight)
    #print("This is total_new_weight",Total_new_weight)

    # leena
    if long_broken_list:  # if the list is not empty then do following
        for i in range(0, len(long_broken_list)-1):
            long_broken_weight.append(model.predict(
                [[float(long_broken_list[i]["Length"]), float(long_broken_list[i]["Width"])]]))
            # long_broken_weight.append(round((((-0.00994)+(0.00167*long_broken_list[i]["Length"]))+(0.00663*long_broken_list[i]["Width"])),5))

        total_long_broken_weight = float(sum(long_broken_weight))
        #print("This is total_new_weight of long broken ",total_long_broken_weight)

    if medium_broken_list:
        for i in range(0, len(medium_broken_list)-1):
            medium_broken_weight.append(model.predict(
                [[float(medium_broken_list[i]["Length"]), float(medium_broken_list[i]["Width"])]]))
            # medium_broken_weight.append(round((((-0.00994)+(0.00167*medium_broken_list[i]["Length"]))+(0.00663*medium_broken_list[i]["Width"])),5))

        total_medium_broken_weight = float(sum(medium_broken_weight))
        #print("This is total_new_weight of medium broken",total_medium_broken_weight)

    if small_broken_list:
        for i in range(0, len(small_broken_list)-1):
            small_broken_weight.append(model.predict(
                [[float(small_broken_list[i]["Length"]), float(small_broken_list[i]["Width"])]]))
            # small_broken_weight.append(round((((-0.00994)+(0.00167*small_broken_list[i]["Length"]))+(0.00663*small_broken_list[i]["Width"])),5))

        total_small_broken_weight = float(sum(small_broken_weight))
        #print("This is total_new_weight of small broken",total_small_broken_weight)
#####

    #print("\n\n\nEnd of for loop")

    ## Making the logic of weighted average for head rice & broken rice ##
        ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
        ##   Start  ##

    from analysis_brown import yellow_length, yellow_width
    for i, j in zip(yellow_length, yellow_width):
        yellow_weight.append(model.predict([[float(i), float(j)]]))
        # yellow_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    #total_yellow_weight = round(sum(yellow_weight),3)
    global total_yellow_weight
    total_yellow_weight = round(float(sum(yellow_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    ## Making the logic of weighted average for damage rice ##
    ##   Start  ##

    from analysis_brown import damage_length, damage_width
    for i, j in zip(damage_length, damage_width):
        damage_weight.append(model.predict([[float(i), float(j)]]))
        # damage_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_damage_weight
    total_damage_weight = round(float(sum(damage_weight)), 3)
    #print("\n\nThis is total weight of damage",total_damage_weight)

    ## Making the logic of weighted average for damage rice ##
    ##   End  ##

    ## Making the logic of weighted average for chalky rice ##
    ##   Start  ##

    from analysis_brown import chalky_length, chalky_width
    for i, j in zip(chalky_length, chalky_width):
        chalky_weight.append(model.predict([[float(i), float(j)]]))
        # chalky_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_chalky_weight
    total_chalky_weight = round(float(sum(chalky_weight)), 3)
    #print("\n\nThis is total weight of chalky",total_chalky_weight)

    ## Making the logic of weighted average for chalky rice ##
    ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
    ##   Start  ##

    from analysis_brown import paddy_length, paddy_width
    for i, j in zip(paddy_length, paddy_width):
        paddy_weight.append(model.predict([[float(i), float(j)]]))
        # paddy_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    total_paddy_weight = round(float(sum(paddy_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    head = round(len(head_rice))

    long = round(len(broken_rice))

    # Report generation with mm Reference

    # (calculate_value.result3 == 'No-AGL') and
    if (len(get_user_input.result1) != 0):

        from analysis_brown import yellow_count, chalky_count, new_damage1_count, paddy_count
        global paddy_percentage, yellow_percentage, chalky_percentage, damage_percentage
        yellow_percentage = round(
            float(total_yellow_weight/Total_new_weight), 2)
        chalky_percentage = round(
            float(total_chalky_weight/Total_new_weight), 2)
        damage_percentage = round(
            float(total_damage_weight/Total_new_weight), 2)
        paddy_percentage = round(float(total_paddy_weight/Total_new_weight), 2)

        #Muzammil adding
        #Muzammil adding
        _1mm_2mm_percentage = round(float(total_1mm_2mm_weight/Total_new_weight),2)
        _2mm_3mm_percentage = round(float(total_2mm_3mm_weight/Total_new_weight),2)
        _3mm_4mm_percentage = round(float(total_3mm_4mm_weight/Total_new_weight),2)
        _4mm_5mm_percentage = round(float(total_4mm_5mm_weight/Total_new_weight),2)
        _5mm_6mm_percentage = round(float(total_5mm_6mm_weight/Total_new_weight),2)
        _6mm_7mm_percentage = round(float(total_6mm_7mm_weight/Total_new_weight),2)
        _7mm_8mm_percentage = round(float(total_7mm_8mm_weight/Total_new_weight),2)
        _8mm_9mm_percentage = round(float(total_8mm_9mm_weight/Total_new_weight),2)
        _9mm_10mm_percentage = round(float(total_9mm_10mm_weight/Total_new_weight),2)

        # leena
        data3 = [['Sample No', get_sampleNo.input],
                 ['Date', get_date.input],
                 ['Time', get_day.input],
                 ['Arrival No', get_arrivalNo.input],
                 ['Party Name', get_partyName.input],
                 ['Vehicle No', get_vehicleNo.input],
                 ['Rice Type', get_riceType.input],
                 ['Moisture', get_moisture.input],
                 ['Look', get_look.input]
                 ]
        ###
        # removing 0.14 in agl
        data2 = [[Time, Date], [' Variables        ', ' Values  '], ['Average Length (10g) (mm)      ', round(avg_length, 3)],
                 ['Average Width (10g) (mm)        ', round(avg_width, 3)],
                 ['Head Rice AGL       ', round(head_rice_AGL, 3)],
                 ['Whole Grain (qty)      ', head],
                 ['Whole Grain Weight (gm)     ', round(total_head_weight, 3)],
                 ['Broken Grain   (qty)      ', long],
                 ['Broken Grain Weight (gm)     ', round(
                     total_brokenRice_weight, 3)],
                 ['Total Grains (qty)    ', total_grains],
                 ['Reference Value (100g) (mm)',    x],
                 ['Yellow Grains (qty)    ', yellow_count],
                 ['Yellow Grains Weight (gm)    ', total_yellow_weight],
                 ['Yellow Percengate (%)    ', round(
                     (yellow_percentage*100), 3)],
                 ['Chalky Grains (qty)    ', chalky_count],
                 ['Chalky Grains Weight (gm)    ', total_chalky_weight],
                 ['Chalky Percengate (%)    ', round(
                     (chalky_percentage*100), 3)],
                 ['Damage Grains (qty)    ', new_damage1_count],
                 ['Damage Grains Weight (gm)    ', total_damage_weight],
                 ['Damage Percengate (%)    ', round(
                     (damage_percentage*100), 3)],
                 ['Paddy Grains (qty)    ', paddy_count],
                 ['Paddy Grains Weight (gm)    ', total_paddy_weight],
                 ['Paddy Percengate (%)    ', (paddy_percentage*100)],
                 ['Total Weight (gm)',    round(Total_new_weight, 3)],
                 ['Broken Rice Percengate',    round(
                     ((total_brokenRice_weight/Total_new_weight)*100), 3)],
                 ['Long Broken Weight', round(total_long_broken_weight, 3)],
                 ['Medium Broken Weight', round(
                     total_medium_broken_weight, 3)],
                 ['Small Broken Weight', round(total_small_broken_weight, 3)]
                 ]

        data4 = [['Range', "Count", "Average Length(AGL)", "Percent by Weight %"],
                 ["1mm to 2mm", _1mm_2mm, _1mm_2mm_agl, (_1mm_2mm_percentage*100)],
                 ["2mm to 3mm", _2mm_3mm, _2mm_3mm_agl, (_2mm_3mm_percentage*100)],
                 ["3mm to 4mm", _3mm_4mm, _3mm_4mm_agl, (_3mm_4mm_percentage*100)],
                 ["4mm to 5mm", _4mm_5mm, _4mm_5mm_agl, (_4mm_5mm_percentage*100)],
                 ["5mm to 6mm", _5mm_6mm, _5mm_6mm_agl, (_5mm_6mm_percentage*100)],
                 ["6mm to 7mm", _6mm_7mm, _6mm_7mm_agl, (_6mm_7mm_percentage*100)],
                 ["7mm to 8mm", _7mm_8mm, _7mm_8mm_agl, (_7mm_8mm_percentage*100)],
                 ["8mm to 9mm", _8mm_9mm, _8mm_9mm_agl, (_8mm_9mm_percentage*100)],
                 ["9mm to 10mm", _9mm_10mm, _9mm_10mm_agl, (_9mm_10mm_percentage*100)],
                 ]


    table2 = Table(data2, colWidths=[170, 150],
                   rowHeights=22.1)  # rowHeights=24.2
    table2.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    # leena
    ldata = (len(head_rice), len(broken_rice),
             len(med_broken), len(small_broken))
    ####

    cdata = (0, 1, 2, 3)
    tdata = (gtype[0], gtype[1], gtype[2], gtype[3])

    table2.wrapOn(c, 20, 400)  # 20,400, to set
    # c,20,25,,, to set report alignment increase or decrease the last value
    table2.drawOn(c, 20, 15)

    # leena
    # for user defined values
    table3 = Table(data3, colWidths=[100, 130], rowHeights=30)
    table3.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    table3.wrapOn(c, 20, 400)  # 20,400
    table3.drawOn(c, 360, 360)  # c,160,260
    ##

    c.showPage()

    # leena
    # for user defined values
    img = "img/header2.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    table4 = Table(data4, colWidths=[100, 130], rowHeights=30)
    table4.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BACKGROUND',(0,0),(4,0),colors.lightskyblue) # (row start, column end), (row start, coulmn end)
    ]))

    table4.wrapOn(c, 20, 400)  # 20,400
    table4.drawOn(c, 70, 350)  # c,x,y
    ##

    c.save()


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -----------------------------Super kernel basmati white Report------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


def gen_report_super_kernel_basmati_white(objects, S_Report):
    print(">>>>>>>>>> Sumarize report for brown >>>>>>>>>>>>>")
    import time

    gtype = [0, 0, 0, 0]
    global ldata, cdata, tdata, Date, Time
    head = 0
    long = 0
    med = 0
    small = 0

    ## Making the logic of weighted average for head rice & broken rice ##
    ## Initializing variables ##
    #global broken_weight, final_weight

    head_weight = []
    broken_rice_weight = []
    yellow_weight = []
    damage_weight = []
    chalky_weight = []
    paddy_weight = []
    head_rice = []
    broken_rice = []

    # leena
    long_broken = []
    med_broken = []
    small_broken = []

    long_broken_list = []
    medium_broken_list = []
    small_broken_list = []

    long_broken_weight = []
    medium_broken_weight = []
    small_broken_weight = []

    total_long_broken_weight = 0
    total_medium_broken_weight = 0
    total_small_broken_weight = 0


    #Muzammil adding 1mm to 10mm analysis
    _1mm_2mm = 0
    _2mm_3mm = 0
    _3mm_4mm = 0
    _4mm_5mm = 0
    _5mm_6mm = 0
    _6mm_7mm = 0
    _7mm_8mm = 0
    _8mm_9mm = 0
    _9mm_10mm = 0


    _1mm_2mm_weight = []
    _2mm_3mm_weight = []
    _3mm_4mm_weight = []
    _4mm_5mm_weight = []
    _5mm_6mm_weight = []
    _6mm_7mm_weight = []
    _7mm_8mm_weight = []
    _8mm_9mm_weight = []
    _9mm_10mm_weight = []


    _1mm_2mm_rice = []
    _2mm_3mm_rice = []
    _3mm_4mm_rice = []
    _4mm_5mm_rice = []
    _5mm_6mm_rice = []
    _6mm_7mm_rice = []
    _7mm_8mm_rice = []
    _8mm_9mm_rice = []
    _9mm_10mm_rice = []


    total_1mm_2mm_weight = 0
    total_2mm_3mm_weight = 0
    total_3mm_4mm_weight = 0
    total_4mm_5mm_weight = 0
    total_5mm_6mm_weight = 0
    total_6mm_7mm_weight = 0
    total_7mm_8mm_weight = 0
    total_8mm_9mm_weight = 0
    total_9mm_10mm_weight = 0


    _1mm_2mm_agl = 0
    _2mm_3mm_agl = 0
    _3mm_4mm_agl = 0
    _4mm_5mm_agl = 0
    _5mm_6mm_agl = 0
    _6mm_7mm_agl = 0
    _7mm_8mm_agl = 0
    _8mm_9mm_agl = 0
    _9mm_10mm_agl = 0

    if globals.called is not 1:
        # if values are empty in that case
        get_sampleNo.input = "-"
        get_date.input = "-"
        get_day.input = "-"
        get_arrivalNo.input = "-"
        get_partyName.input = "-"
        get_vehicleNo.input = "-"
        get_riceType.input = "-"
        get_moisture.input = "-"
        get_look.input = "-"
        ##

    whole_kernel = []
    PAGE_HEIGHT = defaultPageSize[0]
    PAGE_WIDTH = defaultPageSize[0]
    DefaultPageSize = letter
    c = canvas.Canvas(S_Report, DefaultPageSize)

    # leena
    img = "img/header.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    ##

    form = c.acroForm
    import datetime
    now = datetime.datetime.now()
    now.strftime("%A")
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")
    c.setFont("Helvetica", 12)
    Time = "Test time : %s" % time
    c.setFont("Helvetica", 12)
    Date = "Test date : %s" % date

    global total_grains
    total_grains = len(objects)

    avg_length = float(round(sum(x['Length1']
                       for x in objects)/len(objects), 3))
    avg_width = float(round(sum(x['Width'] for x in objects)/len(objects), 2))
    #avg_area = round(sum(x['Area'] for x in objects)/len(objects),2)

    for i in objects:

        # Calculations for whole/broken ratio

        # (calculate_value.result3 == 'No-AGL') and
        if (len(get_user_input.result1) != 0):

            #print("The user input for mm field exists. Not taking AGL as reference")
            #print("The input variable is: ",get_user_input.result1)
            #print("The length of variable is: ",len(get_user_input.result1))
            global x
            x = get_user_input.result1
            # print("\n\n\n")
            if (float(i['Length1']) >= float((x))):
                #print( "{} >= {}".format(float(i['Length']), float((x))) )
                head_rice.append(i)
            elif(float(i['Length1']) < float((x))):
                #print( "{} < {}".format(float(i['Length']), float((x))) )
                broken_rice.append(i)
            # print("\n\n\n")

##
# (calculate_value.result3 == 'AGL') and len(get_user_input2.result2) != 0
# elif ( (get_user_input.result1) == "" ):
##
# print("The user input for % field exists. Taking AGL as reference")
##
##            from reportnew import AGL
##
##            temp_AGL = AGL
# print("100 Grain test ran",temp_AGL)
##
##
##            x = float(get_user_input2.result2)/float(100)
# print("The percentage is:", x)
# j = (float(avg_length)*float(x))
##            j = (float(temp_AGL)*float(x))
##
# if (float((i['Length'])) >= (j)):
# head_rice.append(i)
# elif(float((i['Length'])) < (j)):
# broken_rice.append(i)

            # and (get_user_input2.result2) == ""
        elif ((get_user_input.result1) == ""):

            #print("The user inputs for both fields do not exist. By defaul input is 75%")

            x = 3/4
            y = 1/2
            z = 1/4

            # print(x,y,z)

            if (i['Length1'] >= avg_length*(x)):
                head_rice.append(i)
            elif((i['Length1'] < avg_length*(x)) and (i['Length1'] > avg_length*(y))):
                broken_rice.append(i)
            elif((i['Length1'] <= avg_length*(y)) and (i['Length1'] > avg_length*(z))):
                broken_rice.append(i)
            elif(i['Length1'] <= (z)):
                broken_rice.append(i)

    ## Making the logic of weighted average for head rice & broken rice ##
                ##   Start  ##

    #final_weight = 0

    #print("This is head rice array items",head_rice)
    #print("This is broken rice array items",broken_rice)

    # leena
    if broken_rice:
        #print("broken rice list here")
        # print(broken_rice)
        for brokenRice_element in broken_rice:
            if not get_input_LongBroken.Max is "" or not get_input_LongBroken.Min is "":
                if(float(get_input_LongBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_LongBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_LongBroken.Max), brokenRice_element["Length"] ,float(get_input_LongBroken.Min)))
                    #print("long broken rice detected")
                    long_broken_list.append(brokenRice_element)

            if not get_input_MediumBroken.Max is "" or not get_input_MediumBroken.Min is "":
                if(float(get_input_MediumBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_MediumBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_MediumBroken.Max), brokenRice_element["Length"] ,float(get_input_MediumBroken.Min)))
                    #print(" Medium broken rice detected")
                    # if particular item need to be added then brokenRice_element["Length"]
                    medium_broken_list.append(brokenRice_element)

            if not get_input_SmallBroken.Max is "" or not get_input_SmallBroken.Min is "":
                if(float(get_input_SmallBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_SmallBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_SmallBroken.Max), brokenRice_element["Length"] ,float(get_input_SmallBroken.Min)))
                    #print(" Small broken rice detected")
                    small_broken_list.append(brokenRice_element)
    ##############

    #Muzammil adding 1mm to 10mm analysis

    for i in objects:
        if i["Length1"] >= 1 and i["Length1"] <= 2:
            _1mm_2mm = _1mm_2mm + 1
            _1mm_2mm_rice.append(i)
        
        elif i["Length1"] >= 2 and i["Length1"] <= 3:
            _2mm_3mm = _2mm_3mm + 1
            _2mm_3mm_rice.append(i)

        elif i["Length1"] >= 3 and i["Length1"] <= 4:
            _3mm_4mm = _3mm_4mm +1
            _3mm_4mm_rice.append(i)

        elif i["Length1"] >= 4 and i["Length1"] <= 5:
            _4mm_5mm = _4mm_5mm +1
            _4mm_5mm_rice.append(i)

        elif i["Length1"] >= 5 and i["Length1"] <= 6:
            _5mm_6mm = _5mm_6mm +1
            _5mm_6mm_rice.append(i)

        elif i["Length1"] >= 6 and i["Length1"] <= 7:
            _6mm_7mm = _6mm_7mm + 1
            _6mm_7mm_rice.append(i)
        
        elif i["Length1"] >= 7 and i["Length1"] <= 8:
            _7mm_8mm = _7mm_8mm + 1
            _7mm_8mm_rice.append(i)
        
        elif i["Length1"] >= 8 and i["Length1"] <= 9:
            _8mm_9mm = _8mm_9mm + 1
            _8mm_9mm_rice.append(i)

        elif i["Length1"] >= 9 and i["Length1"] <= 10:
            _9mm_10mm = _9mm_10mm + 1
            _9mm_10mm_rice.append(i)



    if _1mm_2mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_1mm_2mm_rice)-1):
            _1mm_2mm_weight.append(model.predict([[float(_1mm_2mm_rice[i]["Length"]),float(_1mm_2mm_rice[i]["Width"])]]))
            
        total_1mm_2mm_weight = float(sum(_1mm_2mm_weight))

    if _2mm_3mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_2mm_3mm_rice)-1):
            _2mm_3mm_weight.append(model.predict([[float(_2mm_3mm_rice[i]["Length"]),float(_2mm_3mm_rice[i]["Width"])]]))
            
        total_2mm_3mm_weight = float(sum(_2mm_3mm_weight))

    if _3mm_4mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_3mm_4mm_rice)-1):
            _3mm_4mm_weight.append(model.predict([[float(_3mm_4mm_rice[i]["Length"]),float(_3mm_4mm_rice[i]["Width"])]]))
            
        total_3mm_4mm_weight = float(sum(_3mm_4mm_weight))
    
    if _4mm_5mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_4mm_5mm_rice)-1):
            _4mm_5mm_weight.append(model.predict([[float(_4mm_5mm_rice[i]["Length"]),float(_4mm_5mm_rice[i]["Width"])]]))
            
        total_4mm_5mm_weight = float(sum(_4mm_5mm_weight))
    
    if _5mm_6mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_5mm_6mm_rice)-1):
            _5mm_6mm_weight.append(model.predict([[float(_5mm_6mm_rice[i]["Length"]),float(_5mm_6mm_rice[i]["Width"])]]))
            
        total_5mm_6mm_weight = float(sum(_5mm_6mm_weight))

    if _6mm_7mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_6mm_7mm_rice)-1):
            _6mm_7mm_weight.append(model.predict([[float(_6mm_7mm_rice[i]["Length"]),float(_6mm_7mm_rice[i]["Width"])]]))
            
        total_6mm_7mm_weight = float(sum(_6mm_7mm_weight))

    if _7mm_8mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_7mm_8mm_rice)-1):
            _7mm_8mm_weight.append(model.predict([[float(_7mm_8mm_rice[i]["Length"]),float(_7mm_8mm_rice[i]["Width"])]]))
            
        total_7mm_8mm_weight = float(sum(_7mm_8mm_weight))

    if _8mm_9mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_8mm_9mm_rice)-1):
            _8mm_9mm_weight.append(model.predict([[float(_8mm_9mm_rice[i]["Length"]),float(_8mm_9mm_rice[i]["Width"])]]))
            
        total_8mm_9mm_weight = float(sum(_8mm_9mm_weight))

    if _9mm_10mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_9mm_10mm_rice)-1):
            _9mm_10mm_weight.append(model.predict([[float(_9mm_10mm_rice[i]["Length"]),float(_9mm_10mm_rice[i]["Width"])]]))
            
        total_9mm_10mm_weight = float(sum(_9mm_10mm_weight))



    if _1mm_2mm_rice:
        _1mm_2mm_agl = float(round(sum(x['Length1']for x in _1mm_2mm_rice)/len(_1mm_2mm_rice), 3))
    if _2mm_3mm_rice:
        _2mm_3mm_agl = float(round(sum(x['Length1']for x in _2mm_3mm_rice)/len(_2mm_3mm_rice), 3))
    if _3mm_4mm_rice:
        _3mm_4mm_agl = float(round(sum(x['Length1']for x in _3mm_4mm_rice)/len(_3mm_4mm_rice), 3))
    if _4mm_5mm_rice:
        _4mm_5mm_agl = float(round(sum(x['Length1']for x in _4mm_5mm_rice)/len(_4mm_5mm_rice), 3))
    if _5mm_6mm_rice:
        _5mm_6mm_agl = float(round(sum(x['Length1']for x in _5mm_6mm_rice)/len(_5mm_6mm_rice), 3))
    if _6mm_7mm_rice:
        _6mm_7mm_agl = float(round(sum(x['Length1']for x in _6mm_7mm_rice)/len(_6mm_7mm_rice), 3))
    if _7mm_8mm_rice:
        _7mm_8mm_agl = float(round(sum(x['Length1']for x in _7mm_8mm_rice)/len(_7mm_8mm_rice), 3))
    if _8mm_9mm_rice:
        _8mm_9mm_agl = float(round(sum(x['Length1']for x in _8mm_9mm_rice)/len(_8mm_9mm_rice), 3))
    if _9mm_10mm_rice:
        _9mm_10mm_agl = float(round(sum(x['Length1']for x in _9mm_10mm_rice)/len(_9mm_10mm_rice), 3))

    # Ahsan adding head_rice AGL in report

    head_rice_AGL = float(round(sum(x['Length1']
                          for x in head_rice)/len(head_rice), 3))
    head_rice_AGL = head_rice_AGL
    print("This is head_rice AGL", head_rice_AGL)
    #model = tf.keras.models.load_model('w.h5')

    for i in range(0, len(head_rice)-1):
        #print("\n\n\nThis is first element's Length & Width of head_rice",head_rice[i]["Length"],head_rice[i]["Width"])
        #global head_weight

        nm = model.predict(
            [[float(head_rice[i]["Length"]), float(head_rice[i]["Width"])]])
        head_weight.append(nm)
    # head_weight.append(round((((-0.00860)+(0.00167*head_rice[i]["Length"]))+(0.00663*head_rice[i]["Width"])),5)) Muzammil commented
    # head_weight.append(round((((-0.00860)+(0.00188*head_rice[i]["Length"]))+(0.00680*head_rice[i]["Width"])),5))old

    #total_head_weight = float(round(sum(head_weight),3))
    total_head_weight = float(sum(head_weight))
    #print("\n\nThis is total weight of head_rice",total_head_weight)

    for i in range(0, len(broken_rice)-1):

        nm1 = model.predict(
            [[float(broken_rice[i]["Length"]), float(broken_rice[i]["Width"])]])
        broken_rice_weight.append(nm1)
        # broken_rice_weight.append(round((((-0.00860)+(0.00167*broken_rice[i]["Length"]))+(0.00663*broken_rice[i]["Width"])),5))

    total_brokenRice_weight = float(sum(broken_rice_weight))
    #print("\n\nThis is total weight of long_broken_rice",total_brokenRice_weight)

    global Total_new_weight
    Total_new_weight = float(total_head_weight + total_brokenRice_weight)
    #print("This is total_new_weight",Total_new_weight)

    # leena
    if long_broken_list:  # if the list is not empty then do following
        for i in range(0, len(long_broken_list)-1):
            long_broken_weight.append(model.predict(
                [[float(long_broken_list[i]["Length"]), float(long_broken_list[i]["Width"])]]))
            # long_broken_weight.append(round((((-0.00994)+(0.00167*long_broken_list[i]["Length"]))+(0.00663*long_broken_list[i]["Width"])),5))

        total_long_broken_weight = float(sum(long_broken_weight))
        #print("This is total_new_weight of long broken ",total_long_broken_weight)

    if medium_broken_list:
        for i in range(0, len(medium_broken_list)-1):
            medium_broken_weight.append(model.predict(
                [[float(medium_broken_list[i]["Length"]), float(medium_broken_list[i]["Width"])]]))
            # medium_broken_weight.append(round((((-0.00994)+(0.00167*medium_broken_list[i]["Length"]))+(0.00663*medium_broken_list[i]["Width"])),5))

        total_medium_broken_weight = float(sum(medium_broken_weight))
        #print("This is total_new_weight of medium broken",total_medium_broken_weight)

    if small_broken_list:
        for i in range(0, len(small_broken_list)-1):
            small_broken_weight.append(model.predict(
                [[float(small_broken_list[i]["Length"]), float(small_broken_list[i]["Width"])]]))
            # small_broken_weight.append(round((((-0.00994)+(0.00167*small_broken_list[i]["Length"]))+(0.00663*small_broken_list[i]["Width"])),5))

        total_small_broken_weight = float(sum(small_broken_weight))
        #print("This is total_new_weight of small broken",total_small_broken_weight)
#####

    #print("\n\n\nEnd of for loop")

    ## Making the logic of weighted average for head rice & broken rice ##
        ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
        ##   Start  ##

    from analysis_super_kernel_basmati_white import yellow_length, yellow_width
    for i, j in zip(yellow_length, yellow_width):
        yellow_weight.append(model.predict([[float(i), float(j)]]))
        # yellow_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    #total_yellow_weight = round(sum(yellow_weight),3)
    global total_yellow_weight
    total_yellow_weight = round(float(sum(yellow_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    ## Making the logic of weighted average for damage rice ##
    ##   Start  ##

    from analysis_super_kernel_basmati_white import damage_length, damage_width
    for i, j in zip(damage_length, damage_width):
        damage_weight.append(model.predict([[float(i), float(j)]]))
        # damage_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_damage_weight
    total_damage_weight = round(float(sum(damage_weight)), 3)
    #print("\n\nThis is total weight of damage",total_damage_weight)

    ## Making the logic of weighted average for damage rice ##
    ##   End  ##

    ## Making the logic of weighted average for chalky rice ##
    ##   Start  ##

    from analysis_super_kernel_basmati_white import chalky_length, chalky_width
    for i, j in zip(chalky_length, chalky_width):
        chalky_weight.append(model.predict([[float(i), float(j)]]))
        # chalky_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_chalky_weight
    total_chalky_weight = round(float(sum(chalky_weight)), 3)
    #print("\n\nThis is total weight of chalky",total_chalky_weight)

    ## Making the logic of weighted average for chalky rice ##
    ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
    ##   Start  ##

    from analysis_super_kernel_basmati_white import paddy_length, paddy_width
    for i, j in zip(paddy_length, paddy_width):
        paddy_weight.append(model.predict([[float(i), float(j)]]))
        # paddy_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    total_paddy_weight = round(float(sum(paddy_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    head = round(len(head_rice))

    long = round(len(broken_rice))

    # Report generation with mm Reference

    # (calculate_value.result3 == 'No-AGL') and
    if (len(get_user_input.result1) != 0):

        from analysis_super_kernel_basmati_white import yellow_count, chalky_count, new_damage1_count, paddy_count
        global paddy_percentage, yellow_percentage, chalky_percentage, damage_percentage
        yellow_percentage = round(
            float(total_yellow_weight/Total_new_weight), 2)
        chalky_percentage = round(
            float(total_chalky_weight/Total_new_weight), 2)
        damage_percentage = round(
            float(total_damage_weight/Total_new_weight), 2)
        paddy_percentage = round(float(total_paddy_weight/Total_new_weight), 2)

        #Muzammil adding
        #Muzammil adding
        _1mm_2mm_percentage = round(float(total_1mm_2mm_weight/Total_new_weight),2)
        _2mm_3mm_percentage = round(float(total_2mm_3mm_weight/Total_new_weight),2)
        _3mm_4mm_percentage = round(float(total_3mm_4mm_weight/Total_new_weight),2)
        _4mm_5mm_percentage = round(float(total_4mm_5mm_weight/Total_new_weight),2)
        _5mm_6mm_percentage = round(float(total_5mm_6mm_weight/Total_new_weight),2)
        _6mm_7mm_percentage = round(float(total_6mm_7mm_weight/Total_new_weight),2)
        _7mm_8mm_percentage = round(float(total_7mm_8mm_weight/Total_new_weight),2)
        _8mm_9mm_percentage = round(float(total_8mm_9mm_weight/Total_new_weight),2)
        _9mm_10mm_percentage = round(float(total_9mm_10mm_weight/Total_new_weight),2)

        # leena
        data3 = [['Sample No', get_sampleNo.input],
                 ['Date', get_date.input],
                 ['Time', get_day.input],
                 ['Arrival No', get_arrivalNo.input],
                 ['Party Name', get_partyName.input],
                 ['Vehicle No', get_vehicleNo.input],
                 ['Rice Type', get_riceType.input],
                 ['Moisture', get_moisture.input],
                 ['Look', get_look.input]
                 ]
        ###
        # removing 0.14 in agl
        data2 = [[Time, Date], [' Variables        ', ' Values  '], ['Average Length (10g) (mm)      ', round(avg_length, 3)],
                 ['Average Width (10g) (mm)        ', round(avg_width, 3)],
                 ['Head Rice AGL       ', round(head_rice_AGL, 3)],
                 ['Whole Grain (qty)      ', head],
                 ['Whole Grain Weight (gm)     ', round(total_head_weight, 3)],
                 ['Broken Grain   (qty)      ', long],
                 ['Broken Grain Weight (gm)     ', round(
                     total_brokenRice_weight, 3)],
                 ['Total Grains (qty)    ', total_grains],
                 ['Reference Value (100g) (mm)',    x],
                 ['Yellow Grains (qty)    ', yellow_count],
                 ['Yellow Grains Weight (gm)    ', total_yellow_weight],
                 ['Yellow Percengate (%)    ', round(
                     (yellow_percentage*100), 3)],
                 ['Chalky Grains (qty)    ', chalky_count],
                 ['Chalky Grains Weight (gm)    ', total_chalky_weight],
                 ['Chalky Percengate (%)    ', round(
                     (chalky_percentage*100), 3)],
                 ['Paddy Grains (qty)    ', paddy_count],
                 ['Paddy Grains Weight (gm)    ', total_paddy_weight],
                 ['Paddy Percengate (%)    ', (paddy_percentage*100)],
                 ['Total Weight (gm)',    round(Total_new_weight, 3)],
                 ['Broken Rice Percengate',    round(
                     ((total_brokenRice_weight/Total_new_weight)*100), 3)],
                 ['Long Broken Weight', round(total_long_broken_weight, 3)],
                 ['Medium Broken Weight', round(
                     total_medium_broken_weight, 3)],
                 ['Small Broken Weight', round(total_small_broken_weight, 3)]
                 ]

        data4 = [['Range', "Count", "Average Length(AGL)", "Percent by Weight %"],
                 ["1mm to 2mm", _1mm_2mm, _1mm_2mm_agl, (_1mm_2mm_percentage*100)],
                 ["2mm to 3mm", _2mm_3mm, _2mm_3mm_agl, (_2mm_3mm_percentage*100)],
                 ["3mm to 4mm", _3mm_4mm, _3mm_4mm_agl, (_3mm_4mm_percentage*100)],
                 ["4mm to 5mm", _4mm_5mm, _4mm_5mm_agl, (_4mm_5mm_percentage*100)],
                 ["5mm to 6mm", _5mm_6mm, _5mm_6mm_agl, (_5mm_6mm_percentage*100)],
                 ["6mm to 7mm", _6mm_7mm, _6mm_7mm_agl, (_6mm_7mm_percentage*100)],
                 ["7mm to 8mm", _7mm_8mm, _7mm_8mm_agl, (_7mm_8mm_percentage*100)],
                 ["8mm to 9mm", _8mm_9mm, _8mm_9mm_agl, (_8mm_9mm_percentage*100)],
                 ["9mm to 10mm", _9mm_10mm, _9mm_10mm_agl, (_9mm_10mm_percentage*100)],
                 ]

    table2 = Table(data2, colWidths=[170, 150],
                   rowHeights=22.1)  # rowHeights=24.2
    table2.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    # leena
    ldata = (len(head_rice), len(broken_rice),
             len(med_broken), len(small_broken))
    ####

    cdata = (0, 1, 2, 3)
    tdata = (gtype[0], gtype[1], gtype[2], gtype[3])

    table2.wrapOn(c, 20, 400)  # 20,400, to set
    # c,20,25,,, to set report alignment increase or decrease the last value
    table2.drawOn(c, 20, 70)

    # leena
    # for user defined values
    table3 = Table(data3, colWidths=[100, 130], rowHeights=30)
    table3.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    table3.wrapOn(c, 20, 400)  # 20,400
    table3.drawOn(c, 360, 360)  # c,160,260
    ##

    c.showPage()

    # leena
    # for user defined values
    img = "img/header2.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    table4 = Table(data4, colWidths=[100, 130], rowHeights=30)
    table4.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BACKGROUND',(0,0),(4,0),colors.lightskyblue) # (row start, column end), (row start, coulmn end)
    ]))

    table4.wrapOn(c, 20, 400)  # 20,400
    table4.drawOn(c, 70, 350)  # c,x,y
    ##


    c.save()


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -----------------------------Super kernel basmati brown Report------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


def gen_report_super_kernel_basmati_brown(objects, S_Report):
    print(">>>>>>>>>> Sumarize report for brown >>>>>>>>>>>>>")
    import time

    gtype = [0, 0, 0, 0]
    global ldata, cdata, tdata, Date, Time
    head = 0
    long = 0
    med = 0
    small = 0

    ## Making the logic of weighted average for head rice & broken rice ##
    ## Initializing variables ##
    #global broken_weight, final_weight

    head_weight = []
    broken_rice_weight = []
    yellow_weight = []
    damage_weight = []
    chalky_weight = []
    paddy_weight = []
    head_rice = []
    broken_rice = []

    # leena
    long_broken = []
    med_broken = []
    small_broken = []

    long_broken_list = []
    medium_broken_list = []
    small_broken_list = []

    long_broken_weight = []
    medium_broken_weight = []
    small_broken_weight = []

    total_long_broken_weight = 0
    total_medium_broken_weight = 0
    total_small_broken_weight = 0

    #Muzammil adding 1mm to 10mm analysis
    _1mm_2mm = 0
    _2mm_3mm = 0
    _3mm_4mm = 0
    _4mm_5mm = 0
    _5mm_6mm = 0
    _6mm_7mm = 0
    _7mm_8mm = 0
    _8mm_9mm = 0
    _9mm_10mm = 0


    _1mm_2mm_weight = []
    _2mm_3mm_weight = []
    _3mm_4mm_weight = []
    _4mm_5mm_weight = []
    _5mm_6mm_weight = []
    _6mm_7mm_weight = []
    _7mm_8mm_weight = []
    _8mm_9mm_weight = []
    _9mm_10mm_weight = []


    _1mm_2mm_rice = []
    _2mm_3mm_rice = []
    _3mm_4mm_rice = []
    _4mm_5mm_rice = []
    _5mm_6mm_rice = []
    _6mm_7mm_rice = []
    _7mm_8mm_rice = []
    _8mm_9mm_rice = []
    _9mm_10mm_rice = []


    total_1mm_2mm_weight = 0
    total_2mm_3mm_weight = 0
    total_3mm_4mm_weight = 0
    total_4mm_5mm_weight = 0
    total_5mm_6mm_weight = 0
    total_6mm_7mm_weight = 0
    total_7mm_8mm_weight = 0
    total_8mm_9mm_weight = 0
    total_9mm_10mm_weight = 0


    _1mm_2mm_agl = 0
    _2mm_3mm_agl = 0
    _3mm_4mm_agl = 0
    _4mm_5mm_agl = 0
    _5mm_6mm_agl = 0
    _6mm_7mm_agl = 0
    _7mm_8mm_agl = 0
    _8mm_9mm_agl = 0
    _9mm_10mm_agl = 0

    if globals.called is not 1:
        # if values are empty in that case
        get_sampleNo.input = "-"
        get_date.input = "-"
        get_day.input = "-"
        get_arrivalNo.input = "-"
        get_partyName.input = "-"
        get_vehicleNo.input = "-"
        get_riceType.input = "-"
        get_moisture.input = "-"
        get_look.input = "-"
        ##

    whole_kernel = []
    PAGE_HEIGHT = defaultPageSize[0]
    PAGE_WIDTH = defaultPageSize[0]
    DefaultPageSize = letter
    c = canvas.Canvas(S_Report, DefaultPageSize)

    # leena
    img = "img/header.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    ##

    form = c.acroForm
    import datetime
    now = datetime.datetime.now()
    now.strftime("%A")
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")
    c.setFont("Helvetica", 12)
    Time = "Test time : %s" % time
    c.setFont("Helvetica", 12)
    Date = "Test date : %s" % date

    global total_grains
    total_grains = len(objects)

    avg_length = float(round(sum(x['Length1']
                       for x in objects)/len(objects), 3))
    avg_width = float(round(sum(x['Width'] for x in objects)/len(objects), 2))
    #avg_area = round(sum(x['Area'] for x in objects)/len(objects),2)

    for i in objects:

        # Calculations for whole/broken ratio

        # (calculate_value.result3 == 'No-AGL') and
        if (len(get_user_input.result1) != 0):

            #print("The user input for mm field exists. Not taking AGL as reference")
            #print("The input variable is: ",get_user_input.result1)
            #print("The length of variable is: ",len(get_user_input.result1))
            global x
            x = get_user_input.result1
            # print("\n\n\n")
            if (float(i['Length1']) >= float((x))):
                #print( "{} >= {}".format(float(i['Length']), float((x))) )
                head_rice.append(i)
            elif(float(i['Length1']) < float((x))):
                #print( "{} < {}".format(float(i['Length']), float((x))) )
                broken_rice.append(i)
            # print("\n\n\n")

##
# (calculate_value.result3 == 'AGL') and len(get_user_input2.result2) != 0
# elif ( (get_user_input.result1) == "" ):
##
# print("The user input for % field exists. Taking AGL as reference")
##
##            from reportnew import AGL
##
##            temp_AGL = AGL
# print("100 Grain test ran",temp_AGL)
##
##
##            x = float(get_user_input2.result2)/float(100)
# print("The percentage is:", x)
# j = (float(avg_length)*float(x))
##            j = (float(temp_AGL)*float(x))
##
# if (float((i['Length'])) >= (j)):
# head_rice.append(i)
# elif(float((i['Length'])) < (j)):
# broken_rice.append(i)

            # and (get_user_input2.result2) == ""
        elif ((get_user_input.result1) == ""):

            #print("The user inputs for both fields do not exist. By defaul input is 75%")

            x = 3/4
            y = 1/2
            z = 1/4

            # print(x,y,z)

            if (i['Length1'] >= avg_length*(x)):
                head_rice.append(i)
            elif((i['Length1'] < avg_length*(x)) and (i['Length1'] > avg_length*(y))):
                broken_rice.append(i)
            elif((i['Length1'] <= avg_length*(y)) and (i['Length1'] > avg_length*(z))):
                broken_rice.append(i)
            elif(i['Length1'] <= (z)):
                broken_rice.append(i)

    ## Making the logic of weighted average for head rice & broken rice ##
                ##   Start  ##

    #final_weight = 0

    #print("This is head rice array items",head_rice)
    #print("This is broken rice array items",broken_rice)

    # leena
    if broken_rice:
        #print("broken rice list here")
        # print(broken_rice)
        for brokenRice_element in broken_rice:
            if not get_input_LongBroken.Max is "" or not get_input_LongBroken.Min is "":
                if(float(get_input_LongBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_LongBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_LongBroken.Max), brokenRice_element["Length"] ,float(get_input_LongBroken.Min)))
                    #print("long broken rice detected")
                    long_broken_list.append(brokenRice_element)

            if not get_input_MediumBroken.Max is "" or not get_input_MediumBroken.Min is "":
                if(float(get_input_MediumBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_MediumBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_MediumBroken.Max), brokenRice_element["Length"] ,float(get_input_MediumBroken.Min)))
                    #print(" Medium broken rice detected")
                    # if particular item need to be added then brokenRice_element["Length"]
                    medium_broken_list.append(brokenRice_element)

            if not get_input_SmallBroken.Max is "" or not get_input_SmallBroken.Min is "":
                if(float(get_input_SmallBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_SmallBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_SmallBroken.Max), brokenRice_element["Length"] ,float(get_input_SmallBroken.Min)))
                    #print(" Small broken rice detected")
                    small_broken_list.append(brokenRice_element)
    ##############
    #Muzammil adding 1mm to 10mm analysis

    for i in objects:
        if i["Length1"] >= 1 and i["Length1"] <= 2:
            _1mm_2mm = _1mm_2mm + 1
            _1mm_2mm_rice.append(i)
        
        elif i["Length1"] >= 2 and i["Length1"] <= 3:
            _2mm_3mm = _2mm_3mm + 1
            _2mm_3mm_rice.append(i)

        elif i["Length1"] >= 3 and i["Length1"] <= 4:
            _3mm_4mm = _3mm_4mm +1
            _3mm_4mm_rice.append(i)

        elif i["Length1"] >= 4 and i["Length1"] <= 5:
            _4mm_5mm = _4mm_5mm +1
            _4mm_5mm_rice.append(i)

        elif i["Length1"] >= 5 and i["Length1"] <= 6:
            _5mm_6mm = _5mm_6mm +1
            _5mm_6mm_rice.append(i)

        elif i["Length1"] >= 6 and i["Length1"] <= 7:
            _6mm_7mm = _6mm_7mm + 1
            _6mm_7mm_rice.append(i)
        
        elif i["Length1"] >= 7 and i["Length1"] <= 8:
            _7mm_8mm = _7mm_8mm + 1
            _7mm_8mm_rice.append(i)
        
        elif i["Length1"] >= 8 and i["Length1"] <= 9:
            _8mm_9mm = _8mm_9mm + 1
            _8mm_9mm_rice.append(i)

        elif i["Length1"] >= 9 and i["Length1"] <= 10:
            _9mm_10mm = _9mm_10mm + 1
            _9mm_10mm_rice.append(i)



    if _1mm_2mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_1mm_2mm_rice)-1):
            _1mm_2mm_weight.append(model.predict([[float(_1mm_2mm_rice[i]["Length"]),float(_1mm_2mm_rice[i]["Width"])]]))
            
        total_1mm_2mm_weight = float(sum(_1mm_2mm_weight))

    if _2mm_3mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_2mm_3mm_rice)-1):
            _2mm_3mm_weight.append(model.predict([[float(_2mm_3mm_rice[i]["Length"]),float(_2mm_3mm_rice[i]["Width"])]]))
            
        total_2mm_3mm_weight = float(sum(_2mm_3mm_weight))

    if _3mm_4mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_3mm_4mm_rice)-1):
            _3mm_4mm_weight.append(model.predict([[float(_3mm_4mm_rice[i]["Length"]),float(_3mm_4mm_rice[i]["Width"])]]))
            
        total_3mm_4mm_weight = float(sum(_3mm_4mm_weight))
    
    if _4mm_5mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_4mm_5mm_rice)-1):
            _4mm_5mm_weight.append(model.predict([[float(_4mm_5mm_rice[i]["Length"]),float(_4mm_5mm_rice[i]["Width"])]]))
            
        total_4mm_5mm_weight = float(sum(_4mm_5mm_weight))
    
    if _5mm_6mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_5mm_6mm_rice)-1):
            _5mm_6mm_weight.append(model.predict([[float(_5mm_6mm_rice[i]["Length"]),float(_5mm_6mm_rice[i]["Width"])]]))
            
        total_5mm_6mm_weight = float(sum(_5mm_6mm_weight))

    if _6mm_7mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_6mm_7mm_rice)-1):
            _6mm_7mm_weight.append(model.predict([[float(_6mm_7mm_rice[i]["Length"]),float(_6mm_7mm_rice[i]["Width"])]]))
            
        total_6mm_7mm_weight = float(sum(_6mm_7mm_weight))

    if _7mm_8mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_7mm_8mm_rice)-1):
            _7mm_8mm_weight.append(model.predict([[float(_7mm_8mm_rice[i]["Length"]),float(_7mm_8mm_rice[i]["Width"])]]))
            
        total_7mm_8mm_weight = float(sum(_7mm_8mm_weight))

    if _8mm_9mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_8mm_9mm_rice)-1):
            _8mm_9mm_weight.append(model.predict([[float(_8mm_9mm_rice[i]["Length"]),float(_8mm_9mm_rice[i]["Width"])]]))
            
        total_8mm_9mm_weight = float(sum(_8mm_9mm_weight))

    if _9mm_10mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_9mm_10mm_rice)-1):
            _9mm_10mm_weight.append(model.predict([[float(_9mm_10mm_rice[i]["Length"]),float(_9mm_10mm_rice[i]["Width"])]]))
            
        total_9mm_10mm_weight = float(sum(_9mm_10mm_weight))



    if _1mm_2mm_rice:
        _1mm_2mm_agl = float(round(sum(x['Length1']for x in _1mm_2mm_rice)/len(_1mm_2mm_rice), 3))
    if _2mm_3mm_rice:
        _2mm_3mm_agl = float(round(sum(x['Length1']for x in _2mm_3mm_rice)/len(_2mm_3mm_rice), 3))
    if _3mm_4mm_rice:
        _3mm_4mm_agl = float(round(sum(x['Length1']for x in _3mm_4mm_rice)/len(_3mm_4mm_rice), 3))
    if _4mm_5mm_rice:
        _4mm_5mm_agl = float(round(sum(x['Length1']for x in _4mm_5mm_rice)/len(_4mm_5mm_rice), 3))
    if _5mm_6mm_rice:
        _5mm_6mm_agl = float(round(sum(x['Length1']for x in _5mm_6mm_rice)/len(_5mm_6mm_rice), 3))
    if _6mm_7mm_rice:
        _6mm_7mm_agl = float(round(sum(x['Length1']for x in _6mm_7mm_rice)/len(_6mm_7mm_rice), 3))
    if _7mm_8mm_rice:
        _7mm_8mm_agl = float(round(sum(x['Length1']for x in _7mm_8mm_rice)/len(_7mm_8mm_rice), 3))
    if _8mm_9mm_rice:
        _8mm_9mm_agl = float(round(sum(x['Length1']for x in _8mm_9mm_rice)/len(_8mm_9mm_rice), 3))
    if _9mm_10mm_rice:
        _9mm_10mm_agl = float(round(sum(x['Length1']for x in _9mm_10mm_rice)/len(_9mm_10mm_rice), 3))

    # Ahsan adding head_rice AGL in report

    head_rice_AGL = float(round(sum(x['Length1']
                          for x in head_rice)/len(head_rice), 3))
    head_rice_AGL = head_rice_AGL
    print("This is head_rice AGL", head_rice_AGL)
    #model = tf.keras.models.load_model('w.h5')

    for i in range(0, len(head_rice)-1):
        #print("\n\n\nThis is first element's Length & Width of head_rice",head_rice[i]["Length"],head_rice[i]["Width"])
        #global head_weight

        nm = model.predict(
            [[float(head_rice[i]["Length"]), float(head_rice[i]["Width"])]])
        head_weight.append(nm)
    # head_weight.append(round((((-0.00860)+(0.00167*head_rice[i]["Length"]))+(0.00663*head_rice[i]["Width"])),5)) Muzammil commented
    # head_weight.append(round((((-0.00860)+(0.00188*head_rice[i]["Length"]))+(0.00680*head_rice[i]["Width"])),5))old

    #total_head_weight = float(round(sum(head_weight),3))
    total_head_weight = float(sum(head_weight))
    #print("\n\nThis is total weight of head_rice",total_head_weight)

    for i in range(0, len(broken_rice)-1):

        nm1 = model.predict(
            [[float(broken_rice[i]["Length"]), float(broken_rice[i]["Width"])]])
        broken_rice_weight.append(nm1)
        # broken_rice_weight.append(round((((-0.00860)+(0.00167*broken_rice[i]["Length"]))+(0.00663*broken_rice[i]["Width"])),5))

    total_brokenRice_weight = float(sum(broken_rice_weight))
    #print("\n\nThis is total weight of long_broken_rice",total_brokenRice_weight)

    global Total_new_weight
    Total_new_weight = float(total_head_weight + total_brokenRice_weight)
    #print("This is total_new_weight",Total_new_weight)

    # leena
    if long_broken_list:  # if the list is not empty then do following
        for i in range(0, len(long_broken_list)-1):
            long_broken_weight.append(model.predict(
                [[float(long_broken_list[i]["Length"]), float(long_broken_list[i]["Width"])]]))
            # long_broken_weight.append(round((((-0.00994)+(0.00167*long_broken_list[i]["Length"]))+(0.00663*long_broken_list[i]["Width"])),5))

        total_long_broken_weight = float(sum(long_broken_weight))
        #print("This is total_new_weight of long broken ",total_long_broken_weight)

    if medium_broken_list:
        for i in range(0, len(medium_broken_list)-1):
            medium_broken_weight.append(model.predict(
                [[float(medium_broken_list[i]["Length"]), float(medium_broken_list[i]["Width"])]]))
            # medium_broken_weight.append(round((((-0.00994)+(0.00167*medium_broken_list[i]["Length"]))+(0.00663*medium_broken_list[i]["Width"])),5))

        total_medium_broken_weight = float(sum(medium_broken_weight))
        #print("This is total_new_weight of medium broken",total_medium_broken_weight)

    if small_broken_list:
        for i in range(0, len(small_broken_list)-1):
            small_broken_weight.append(model.predict(
                [[float(small_broken_list[i]["Length"]), float(small_broken_list[i]["Width"])]]))
            # small_broken_weight.append(round((((-0.00994)+(0.00167*small_broken_list[i]["Length"]))+(0.00663*small_broken_list[i]["Width"])),5))

        total_small_broken_weight = float(sum(small_broken_weight))
        #print("This is total_new_weight of small broken",total_small_broken_weight)
#####

    #print("\n\n\nEnd of for loop")

    ## Making the logic of weighted average for head rice & broken rice ##
        ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
        ##   Start  ##

    from analysis_super_kernel_basmati_brown import yellow_length, yellow_width
    for i, j in zip(yellow_length, yellow_width):
        yellow_weight.append(model.predict([[float(i), float(j)]]))
        # yellow_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    #total_yellow_weight = round(sum(yellow_weight),3)
    global total_yellow_weight
    total_yellow_weight = round(float(sum(yellow_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    ## Making the logic of weighted average for damage rice ##
    ##   Start  ##

    from analysis_super_kernel_basmati_brown import damage_length, damage_width
    for i, j in zip(damage_length, damage_width):
        damage_weight.append(model.predict([[float(i), float(j)]]))
        # damage_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_damage_weight
    total_damage_weight = round(float(sum(damage_weight)), 3)
    #print("\n\nThis is total weight of damage",total_damage_weight)

    ## Making the logic of weighted average for damage rice ##
    ##   End  ##

    ## Making the logic of weighted average for chalky rice ##
    ##   Start  ##

    from analysis_super_kernel_basmati_brown import chalky_length, chalky_width
    for i, j in zip(chalky_length, chalky_width):
        chalky_weight.append(model.predict([[float(i), float(j)]]))
        # chalky_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_chalky_weight
    total_chalky_weight = round(float(sum(chalky_weight)), 3)
    #print("\n\nThis is total weight of chalky",total_chalky_weight)

    ## Making the logic of weighted average for chalky rice ##
    ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
    ##   Start  ##

    from analysis_super_kernel_basmati_brown import paddy_length, paddy_width
    for i, j in zip(paddy_length, paddy_width):
        paddy_weight.append(model.predict([[float(i), float(j)]]))
        # paddy_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    total_paddy_weight = round(float(sum(paddy_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    head = round(len(head_rice))

    long = round(len(broken_rice))

    # Report generation with mm Reference

    # (calculate_value.result3 == 'No-AGL') and
    if (len(get_user_input.result1) != 0):

        from analysis_super_kernel_basmati_brown import yellow_count, chalky_count, new_damage1_count, paddy_count
        global paddy_percentage, yellow_percentage, chalky_percentage, damage_percentage
        yellow_percentage = round(
            float(total_yellow_weight/Total_new_weight), 2)
        chalky_percentage = round(
            float(total_chalky_weight/Total_new_weight), 2)
        damage_percentage = round(
            float(total_damage_weight/Total_new_weight), 2)
        paddy_percentage = round(float(total_paddy_weight/Total_new_weight), 2)

        #Muzammil adding
        #Muzammil adding
        _1mm_2mm_percentage = round(float(total_1mm_2mm_weight/Total_new_weight),2)
        _2mm_3mm_percentage = round(float(total_2mm_3mm_weight/Total_new_weight),2)
        _3mm_4mm_percentage = round(float(total_3mm_4mm_weight/Total_new_weight),2)
        _4mm_5mm_percentage = round(float(total_4mm_5mm_weight/Total_new_weight),2)
        _5mm_6mm_percentage = round(float(total_5mm_6mm_weight/Total_new_weight),2)
        _6mm_7mm_percentage = round(float(total_6mm_7mm_weight/Total_new_weight),2)
        _7mm_8mm_percentage = round(float(total_7mm_8mm_weight/Total_new_weight),2)
        _8mm_9mm_percentage = round(float(total_8mm_9mm_weight/Total_new_weight),2)
        _9mm_10mm_percentage = round(float(total_9mm_10mm_weight/Total_new_weight),2)

        # leena
        data3 = [['Sample No', get_sampleNo.input],
                 ['Date', get_date.input],
                 ['Time', get_day.input],
                 ['Arrival No', get_arrivalNo.input],
                 ['Party Name', get_partyName.input],
                 ['Vehicle No', get_vehicleNo.input],
                 ['Rice Type', get_riceType.input],
                 ['Moisture', get_moisture.input],
                 ['Look', get_look.input]
                 ]
        ###
        # removing 0.14 in agl
        data2 = [[Time, Date], [' Variables        ', ' Values  '], ['Average Length (10g) (mm)      ', round(avg_length, 3)],
                 ['Average Width (10g) (mm)        ', round(avg_width, 3)],
                 ['Head Rice AGL       ', round(head_rice_AGL, 3)],
                 ['Whole Grain (qty)      ', head],
                 ['Whole Grain Weight (gm)     ', round(total_head_weight, 3)],
                 ['Broken Grain   (qty)      ', long],
                 ['Broken Grain Weight (gm)     ', round(
                     total_brokenRice_weight, 3)],
                 ['Total Grains (qty)    ', total_grains],
                 ['Reference Value (100g) (mm)',    x],
                 ['Red Grains (qty)    ', yellow_count],
                 ['Red Grains Weight (gm)    ', total_yellow_weight],
                 ['Red Percengate (%)    ', round((yellow_percentage*100), 3)],
                 ['Green Grains (qty)    ', chalky_count],
                 ['Green Grains Weight (gm)    ', total_chalky_weight],
                 ['Green Percengate (%)    ', round(
                     (chalky_percentage*100), 3)],
                 ['Paddy Grains (qty)    ', paddy_count],
                 ['Paddy Grains Weight (gm)    ', total_paddy_weight],
                 ['Paddy Percengate (%)    ', (paddy_percentage*100)],
                 ['Total Weight (gm)',    round(Total_new_weight, 3)],
                 ['Broken Rice Percengate',    round(
                     ((total_brokenRice_weight/Total_new_weight)*100), 3)],
                 ['Long Broken Weight', round(total_long_broken_weight, 3)],
                 ['Medium Broken Weight', round(
                     total_medium_broken_weight, 3)],
                 ['Small Broken Weight', round(total_small_broken_weight, 3)]
                 ]

        data4 = [['Range', "Count", "Average Length(AGL)", "Percent by Weight %"],
                 ["1mm to 2mm", _1mm_2mm, _1mm_2mm_agl, (_1mm_2mm_percentage*100)],
                 ["2mm to 3mm", _2mm_3mm, _2mm_3mm_agl, (_2mm_3mm_percentage*100)],
                 ["3mm to 4mm", _3mm_4mm, _3mm_4mm_agl, (_3mm_4mm_percentage*100)],
                 ["4mm to 5mm", _4mm_5mm, _4mm_5mm_agl, (_4mm_5mm_percentage*100)],
                 ["5mm to 6mm", _5mm_6mm, _5mm_6mm_agl, (_5mm_6mm_percentage*100)],
                 ["6mm to 7mm", _6mm_7mm, _6mm_7mm_agl, (_6mm_7mm_percentage*100)],
                 ["7mm to 8mm", _7mm_8mm, _7mm_8mm_agl, (_7mm_8mm_percentage*100)],
                 ["8mm to 9mm", _8mm_9mm, _8mm_9mm_agl, (_8mm_9mm_percentage*100)],
                 ["9mm to 10mm", _9mm_10mm, _9mm_10mm_agl, (_9mm_10mm_percentage*100)],
                 ]

    table2 = Table(data2, colWidths=[170, 150],
                   rowHeights=22.1)  # rowHeights=24.2
    table2.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    # leena
    ldata = (len(head_rice), len(broken_rice),
             len(med_broken), len(small_broken))
    ####

    cdata = (0, 1, 2, 3)
    tdata = (gtype[0], gtype[1], gtype[2], gtype[3])

    table2.wrapOn(c, 20, 400)  # 20,400, to set
    # c,20,25,,, to set report alignment increase or decrease the last value
    table2.drawOn(c, 20, 70)

    # leena
    # for user defined values
    table3 = Table(data3, colWidths=[100, 130], rowHeights=30)
    table3.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    table3.wrapOn(c, 20, 400)  # 20,400
    table3.drawOn(c, 360, 360)  # c,160,260
    ##

    c.showPage()

    # leena
    # for user defined values
    img = "img/header2.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    table4 = Table(data4, colWidths=[100, 130], rowHeights=30)
    table4.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BACKGROUND',(0,0),(4,0),colors.lightskyblue) # (row start, column end), (row start, coulmn end)
    ]))

    table4.wrapOn(c, 20, 400)  # 20,400
    table4.drawOn(c, 70, 350)  # c,x,y
    ##


    c.save()


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -----------------------------1121 sela Report------------------------------
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


def gen_report_1121_sela(objects, S_Report):
    print(">>>>>>>>>> Sumarize report for brown >>>>>>>>>>>>>")
    import time

    gtype = [0, 0, 0, 0]
    global ldata, cdata, tdata, Date, Time
    head = 0
    long = 0
    med = 0
    small = 0

    ## Making the logic of weighted average for head rice & broken rice ##
    ## Initializing variables ##
    #global broken_weight, final_weight

    head_weight = []
    broken_rice_weight = []
    yellow_weight = []
    damage_weight = []
    chalky_weight = []
    paddy_weight = []
    head_rice = []
    broken_rice = []

    # leena
    long_broken = []
    med_broken = []
    small_broken = []

    long_broken_list = []
    medium_broken_list = []
    small_broken_list = []

    long_broken_weight = []
    medium_broken_weight = []
    small_broken_weight = []

    total_long_broken_weight = 0
    total_medium_broken_weight = 0
    total_small_broken_weight = 0

    #Muzammil adding 1mm to 10mm analysis
    _1mm_2mm = 0
    _2mm_3mm = 0
    _3mm_4mm = 0
    _4mm_5mm = 0
    _5mm_6mm = 0
    _6mm_7mm = 0
    _7mm_8mm = 0
    _8mm_9mm = 0
    _9mm_10mm = 0


    _1mm_2mm_weight = []
    _2mm_3mm_weight = []
    _3mm_4mm_weight = []
    _4mm_5mm_weight = []
    _5mm_6mm_weight = []
    _6mm_7mm_weight = []
    _7mm_8mm_weight = []
    _8mm_9mm_weight = []
    _9mm_10mm_weight = []


    _1mm_2mm_rice = []
    _2mm_3mm_rice = []
    _3mm_4mm_rice = []
    _4mm_5mm_rice = []
    _5mm_6mm_rice = []
    _6mm_7mm_rice = []
    _7mm_8mm_rice = []
    _8mm_9mm_rice = []
    _9mm_10mm_rice = []


    total_1mm_2mm_weight = 0
    total_2mm_3mm_weight = 0
    total_3mm_4mm_weight = 0
    total_4mm_5mm_weight = 0
    total_5mm_6mm_weight = 0
    total_6mm_7mm_weight = 0
    total_7mm_8mm_weight = 0
    total_8mm_9mm_weight = 0
    total_9mm_10mm_weight = 0


    _1mm_2mm_agl = 0
    _2mm_3mm_agl = 0
    _3mm_4mm_agl = 0
    _4mm_5mm_agl = 0
    _5mm_6mm_agl = 0
    _6mm_7mm_agl = 0
    _7mm_8mm_agl = 0
    _8mm_9mm_agl = 0
    _9mm_10mm_agl = 0

    if globals.called is not 1:
        # if values are empty in that case
        get_sampleNo.input = "-"
        get_date.input = "-"
        get_day.input = "-"
        get_arrivalNo.input = "-"
        get_partyName.input = "-"
        get_vehicleNo.input = "-"
        get_riceType.input = "-"
        get_moisture.input = "-"
        get_look.input = "-"
        ##

    whole_kernel = []
    PAGE_HEIGHT = defaultPageSize[0]
    PAGE_WIDTH = defaultPageSize[0]
    DefaultPageSize = letter
    c = canvas.Canvas(S_Report, DefaultPageSize)

    # leena
    img = "img/header.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    ##

    form = c.acroForm
    import datetime
    now = datetime.datetime.now()
    now.strftime("%A")
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")
    c.setFont("Helvetica", 12)
    Time = "Test time : %s" % time
    c.setFont("Helvetica", 12)
    Date = "Test date : %s" % date

    global total_grains
    total_grains = len(objects)

    avg_length = float(round(sum(x['Length1']
                       for x in objects)/len(objects), 3))
    avg_width = float(round(sum(x['Width'] for x in objects)/len(objects), 2))
    #avg_area = round(sum(x['Area'] for x in objects)/len(objects),2)

    for i in objects:

        # Calculations for whole/broken ratio

        # (calculate_value.result3 == 'No-AGL') and
        if (len(get_user_input.result1) != 0):

            #print("The user input for mm field exists. Not taking AGL as reference")
            #print("The input variable is: ",get_user_input.result1)
            #print("The length of variable is: ",len(get_user_input.result1))
            global x
            x = get_user_input.result1
            # print("\n\n\n")
            if (float(i['Length1']) >= float((x))):
                #print( "{} >= {}".format(float(i['Length']), float((x))) )
                head_rice.append(i)
            elif(float(i['Length1']) < float((x))):
                #print( "{} < {}".format(float(i['Length']), float((x))) )
                broken_rice.append(i)
            # print("\n\n\n")

##
# (calculate_value.result3 == 'AGL') and len(get_user_input2.result2) != 0
# elif ( (get_user_input.result1) == "" ):
##
# print("The user input for % field exists. Taking AGL as reference")
##
##            from reportnew import AGL
##
##            temp_AGL = AGL
# print("100 Grain test ran",temp_AGL)
##
##
##            x = float(get_user_input2.result2)/float(100)
# print("The percentage is:", x)
# j = (float(avg_length)*float(x))
##            j = (float(temp_AGL)*float(x))
##
# if (float((i['Length'])) >= (j)):
# head_rice.append(i)
# elif(float((i['Length'])) < (j)):
# broken_rice.append(i)

            # and (get_user_input2.result2) == ""
        elif ((get_user_input.result1) == ""):

            #print("The user inputs for both fields do not exist. By defaul input is 75%")

            x = 3/4
            y = 1/2
            z = 1/4

            # print(x,y,z)

            if (i['Length1'] >= avg_length*(x)):
                head_rice.append(i)
            elif((i['Length1'] < avg_length*(x)) and (i['Length1'] > avg_length*(y))):
                broken_rice.append(i)
            elif((i['Length1'] <= avg_length*(y)) and (i['Length1'] > avg_length*(z))):
                broken_rice.append(i)
            elif(i['Length1'] <= (z)):
                broken_rice.append(i)

    ## Making the logic of weighted average for head rice & broken rice ##
                ##   Start  ##

    #final_weight = 0

    #print("This is head rice array items",head_rice)
    #print("This is broken rice array items",broken_rice)

    # leena
    if broken_rice:
        #print("broken rice list here")
        # print(broken_rice)
        for brokenRice_element in broken_rice:
            if not get_input_LongBroken.Max is "" or not get_input_LongBroken.Min is "":
                if(float(get_input_LongBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_LongBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_LongBroken.Max), brokenRice_element["Length"] ,float(get_input_LongBroken.Min)))
                    #print("long broken rice detected")
                    long_broken_list.append(brokenRice_element)

            if not get_input_MediumBroken.Max is "" or not get_input_MediumBroken.Min is "":
                if(float(get_input_MediumBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_MediumBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_MediumBroken.Max), brokenRice_element["Length"] ,float(get_input_MediumBroken.Min)))
                    #print(" Medium broken rice detected")
                    # if particular item need to be added then brokenRice_element["Length"]
                    medium_broken_list.append(brokenRice_element)

            if not get_input_SmallBroken.Max is "" or not get_input_SmallBroken.Min is "":
                if(float(get_input_SmallBroken.Max) >= brokenRice_element["Length1"] >= float(get_input_SmallBroken.Min)):
                    #print( "{} >= {} >= {}".format(float(get_input_SmallBroken.Max), brokenRice_element["Length"] ,float(get_input_SmallBroken.Min)))
                    #print(" Small broken rice detected")
                    small_broken_list.append(brokenRice_element)
    ##############
    #Muzammil adding 1mm to 10mm analysis

    for i in objects:
        if i["Length1"] >= 1 and i["Length1"] <= 2:
            _1mm_2mm = _1mm_2mm + 1
            _1mm_2mm_rice.append(i)
        
        elif i["Length1"] >= 2 and i["Length1"] <= 3:
            _2mm_3mm = _2mm_3mm + 1
            _2mm_3mm_rice.append(i)

        elif i["Length1"] >= 3 and i["Length1"] <= 4:
            _3mm_4mm = _3mm_4mm +1
            _3mm_4mm_rice.append(i)

        elif i["Length1"] >= 4 and i["Length1"] <= 5:
            _4mm_5mm = _4mm_5mm +1
            _4mm_5mm_rice.append(i)

        elif i["Length1"] >= 5 and i["Length1"] <= 6:
            _5mm_6mm = _5mm_6mm +1
            _5mm_6mm_rice.append(i)

        elif i["Length1"] >= 6 and i["Length1"] <= 7:
            _6mm_7mm = _6mm_7mm + 1
            _6mm_7mm_rice.append(i)
        
        elif i["Length1"] >= 7 and i["Length1"] <= 8:
            _7mm_8mm = _7mm_8mm + 1
            _7mm_8mm_rice.append(i)
        
        elif i["Length1"] >= 8 and i["Length1"] <= 9:
            _8mm_9mm = _8mm_9mm + 1
            _8mm_9mm_rice.append(i)

        elif i["Length1"] >= 9 and i["Length1"] <= 10:
            _9mm_10mm = _9mm_10mm + 1
            _9mm_10mm_rice.append(i)



    if _1mm_2mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_1mm_2mm_rice)-1):
            _1mm_2mm_weight.append(model.predict([[float(_1mm_2mm_rice[i]["Length"]),float(_1mm_2mm_rice[i]["Width"])]]))
            
        total_1mm_2mm_weight = float(sum(_1mm_2mm_weight))

    if _2mm_3mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_2mm_3mm_rice)-1):
            _2mm_3mm_weight.append(model.predict([[float(_2mm_3mm_rice[i]["Length"]),float(_2mm_3mm_rice[i]["Width"])]]))
            
        total_2mm_3mm_weight = float(sum(_2mm_3mm_weight))

    if _3mm_4mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_3mm_4mm_rice)-1):
            _3mm_4mm_weight.append(model.predict([[float(_3mm_4mm_rice[i]["Length"]),float(_3mm_4mm_rice[i]["Width"])]]))
            
        total_3mm_4mm_weight = float(sum(_3mm_4mm_weight))
    
    if _4mm_5mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_4mm_5mm_rice)-1):
            _4mm_5mm_weight.append(model.predict([[float(_4mm_5mm_rice[i]["Length"]),float(_4mm_5mm_rice[i]["Width"])]]))
            
        total_4mm_5mm_weight = float(sum(_4mm_5mm_weight))
    
    if _5mm_6mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_5mm_6mm_rice)-1):
            _5mm_6mm_weight.append(model.predict([[float(_5mm_6mm_rice[i]["Length"]),float(_5mm_6mm_rice[i]["Width"])]]))
            
        total_5mm_6mm_weight = float(sum(_5mm_6mm_weight))

    if _6mm_7mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_6mm_7mm_rice)-1):
            _6mm_7mm_weight.append(model.predict([[float(_6mm_7mm_rice[i]["Length"]),float(_6mm_7mm_rice[i]["Width"])]]))
            
        total_6mm_7mm_weight = float(sum(_6mm_7mm_weight))

    if _7mm_8mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_7mm_8mm_rice)-1):
            _7mm_8mm_weight.append(model.predict([[float(_7mm_8mm_rice[i]["Length"]),float(_7mm_8mm_rice[i]["Width"])]]))
            
        total_7mm_8mm_weight = float(sum(_7mm_8mm_weight))

    if _8mm_9mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_8mm_9mm_rice)-1):
            _8mm_9mm_weight.append(model.predict([[float(_8mm_9mm_rice[i]["Length"]),float(_8mm_9mm_rice[i]["Width"])]]))
            
        total_8mm_9mm_weight = float(sum(_8mm_9mm_weight))

    if _9mm_10mm_rice:    #if the list is not empty then do following
        for i in range(0,len(_9mm_10mm_rice)-1):
            _9mm_10mm_weight.append(model.predict([[float(_9mm_10mm_rice[i]["Length"]),float(_9mm_10mm_rice[i]["Width"])]]))
            
        total_9mm_10mm_weight = float(sum(_9mm_10mm_weight))



    if _1mm_2mm_rice:
        _1mm_2mm_agl = float(round(sum(x['Length1']for x in _1mm_2mm_rice)/len(_1mm_2mm_rice), 3))
    if _2mm_3mm_rice:
        _2mm_3mm_agl = float(round(sum(x['Length1']for x in _2mm_3mm_rice)/len(_2mm_3mm_rice), 3))
    if _3mm_4mm_rice:
        _3mm_4mm_agl = float(round(sum(x['Length1']for x in _3mm_4mm_rice)/len(_3mm_4mm_rice), 3))
    if _4mm_5mm_rice:
        _4mm_5mm_agl = float(round(sum(x['Length1']for x in _4mm_5mm_rice)/len(_4mm_5mm_rice), 3))
    if _5mm_6mm_rice:
        _5mm_6mm_agl = float(round(sum(x['Length1']for x in _5mm_6mm_rice)/len(_5mm_6mm_rice), 3))
    if _6mm_7mm_rice:
        _6mm_7mm_agl = float(round(sum(x['Length1']for x in _6mm_7mm_rice)/len(_6mm_7mm_rice), 3))
    if _7mm_8mm_rice:
        _7mm_8mm_agl = float(round(sum(x['Length1']for x in _7mm_8mm_rice)/len(_7mm_8mm_rice), 3))
    if _8mm_9mm_rice:
        _8mm_9mm_agl = float(round(sum(x['Length1']for x in _8mm_9mm_rice)/len(_8mm_9mm_rice), 3))
    if _9mm_10mm_rice:
        _9mm_10mm_agl = float(round(sum(x['Length1']for x in _9mm_10mm_rice)/len(_9mm_10mm_rice), 3))

    # Ahsan adding head_rice AGL in report

    head_rice_AGL = float(round(sum(x['Length1']
                          for x in head_rice)/len(head_rice), 3))
    head_rice_AGL = head_rice_AGL
    print("This is head_rice AGL", head_rice_AGL)
    #model = tf.keras.models.load_model('w.h5')

    for i in range(0, len(head_rice)-1):
        #print("\n\n\nThis is first element's Length & Width of head_rice",head_rice[i]["Length"],head_rice[i]["Width"])
        #global head_weight

        nm = model.predict(
            [[float(head_rice[i]["Length"]), float(head_rice[i]["Width"])]])
        head_weight.append(nm)
    # head_weight.append(round((((-0.00860)+(0.00167*head_rice[i]["Length"]))+(0.00663*head_rice[i]["Width"])),5)) Muzammil commented
    # head_weight.append(round((((-0.00860)+(0.00188*head_rice[i]["Length"]))+(0.00680*head_rice[i]["Width"])),5))old

    #total_head_weight = float(round(sum(head_weight),3))
    total_head_weight = float(sum(head_weight))
    #print("\n\nThis is total weight of head_rice",total_head_weight)

    for i in range(0, len(broken_rice)-1):

        nm1 = model.predict(
            [[float(broken_rice[i]["Length"]), float(broken_rice[i]["Width"])]])
        broken_rice_weight.append(nm1)
        # broken_rice_weight.append(round((((-0.00860)+(0.00167*broken_rice[i]["Length"]))+(0.00663*broken_rice[i]["Width"])),5))

    total_brokenRice_weight = float(sum(broken_rice_weight))
    #print("\n\nThis is total weight of long_broken_rice",total_brokenRice_weight)

    global Total_new_weight
    Total_new_weight = float(total_head_weight + total_brokenRice_weight)
    #print("This is total_new_weight",Total_new_weight)

    # leena
    if long_broken_list:  # if the list is not empty then do following
        for i in range(0, len(long_broken_list)-1):
            long_broken_weight.append(model.predict(
                [[float(long_broken_list[i]["Length"]), float(long_broken_list[i]["Width"])]]))
            # long_broken_weight.append(round((((-0.00994)+(0.00167*long_broken_list[i]["Length"]))+(0.00663*long_broken_list[i]["Width"])),5))

        total_long_broken_weight = float(sum(long_broken_weight))
        #print("This is total_new_weight of long broken ",total_long_broken_weight)

    if medium_broken_list:
        for i in range(0, len(medium_broken_list)-1):
            medium_broken_weight.append(model.predict(
                [[float(medium_broken_list[i]["Length"]), float(medium_broken_list[i]["Width"])]]))
            # medium_broken_weight.append(round((((-0.00994)+(0.00167*medium_broken_list[i]["Length"]))+(0.00663*medium_broken_list[i]["Width"])),5))

        total_medium_broken_weight = float(sum(medium_broken_weight))
        #print("This is total_new_weight of medium broken",total_medium_broken_weight)

    if small_broken_list:
        for i in range(0, len(small_broken_list)-1):
            small_broken_weight.append(model.predict(
                [[float(small_broken_list[i]["Length"]), float(small_broken_list[i]["Width"])]]))
            # small_broken_weight.append(round((((-0.00994)+(0.00167*small_broken_list[i]["Length"]))+(0.00663*small_broken_list[i]["Width"])),5))

        total_small_broken_weight = float(sum(small_broken_weight))
        #print("This is total_new_weight of small broken",total_small_broken_weight)
#####

    #print("\n\n\nEnd of for loop")

    ## Making the logic of weighted average for head rice & broken rice ##
        ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
        ##   Start  ##

    from analysis_1121_sela import yellow_length, yellow_width
    for i, j in zip(yellow_length, yellow_width):
        yellow_weight.append(model.predict([[float(i), float(j)]]))
        # yellow_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    #total_yellow_weight = round(sum(yellow_weight),3)
    global total_yellow_weight
    total_yellow_weight = round(float(sum(yellow_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    ## Making the logic of weighted average for damage rice ##
    ##   Start  ##

    from analysis_1121_sela import damage_length, damage_width
    for i, j in zip(damage_length, damage_width):
        damage_weight.append(model.predict([[float(i), float(j)]]))
        # damage_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_damage_weight
    total_damage_weight = round(float(sum(damage_weight)), 3)
    #print("\n\nThis is total weight of damage",total_damage_weight)

    ## Making the logic of weighted average for damage rice ##
    ##   End  ##

    ## Making the logic of weighted average for chalky rice ##
    ##   Start  ##

    from analysis_1121_sela import chalky_length, chalky_width
    for i, j in zip(chalky_length, chalky_width):
        chalky_weight.append(model.predict([[float(i), float(j)]]))
        # chalky_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    global total_chalky_weight
    total_chalky_weight = round(float(sum(chalky_weight)), 3)
    #print("\n\nThis is total weight of chalky",total_chalky_weight)

    ## Making the logic of weighted average for chalky rice ##
    ##   End  ##

    ## Making the logic of weighted average for yellow rice ##
    ##   Start  ##

    from analysis_1121_sela import paddy_length, paddy_width
    for i, j in zip(paddy_length, paddy_width):
        paddy_weight.append(model.predict([[float(i), float(j)]]))
        # paddy_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))

    total_paddy_weight = round(float(sum(paddy_weight)), 3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)

    ## Making the logic of weighted average for yellow rice ##
    ##   End  ##

    head = round(len(head_rice))

    long = round(len(broken_rice))

    # Report generation with mm Reference

    # (calculate_value.result3 == 'No-AGL') and
    if (len(get_user_input.result1) != 0):

        from analysis_1121_sela import yellow_count, chalky_count, new_damage1_count, paddy_count
        global paddy_percentage, yellow_percentage, chalky_percentage, damage_percentage
        yellow_percentage = round(
            float(total_yellow_weight/Total_new_weight), 2)
        chalky_percentage = round(
            float(total_chalky_weight/Total_new_weight), 2)
        damage_percentage = round(
            float(total_damage_weight/Total_new_weight), 2)
        paddy_percentage = round(float(total_paddy_weight/Total_new_weight), 2)

        #Muzammil adding
        #Muzammil adding
        _1mm_2mm_percentage = round(float(total_1mm_2mm_weight/Total_new_weight),2)
        _2mm_3mm_percentage = round(float(total_2mm_3mm_weight/Total_new_weight),2)
        _3mm_4mm_percentage = round(float(total_3mm_4mm_weight/Total_new_weight),2)
        _4mm_5mm_percentage = round(float(total_4mm_5mm_weight/Total_new_weight),2)
        _5mm_6mm_percentage = round(float(total_5mm_6mm_weight/Total_new_weight),2)
        _6mm_7mm_percentage = round(float(total_6mm_7mm_weight/Total_new_weight),2)
        _7mm_8mm_percentage = round(float(total_7mm_8mm_weight/Total_new_weight),2)
        _8mm_9mm_percentage = round(float(total_8mm_9mm_weight/Total_new_weight),2)
        _9mm_10mm_percentage = round(float(total_9mm_10mm_weight/Total_new_weight),2)

        # leena
        data3 = [['Sample No', get_sampleNo.input],
                 ['Date', get_date.input],
                 ['Time', get_day.input],
                 ['Arrival No', get_arrivalNo.input],
                 ['Party Name', get_partyName.input],
                 ['Vehicle No', get_vehicleNo.input],
                 ['Rice Type', get_riceType.input],
                 ['Moisture', get_moisture.input],
                 ['Look', get_look.input]
                 ]
        ###
        # removing 0.14 in agl
        data2 = [[Time, Date], [' Variables        ', ' Values  '], ['Average Length (10g) (mm)      ', round(avg_length, 3)],
                 ['Average Width (10g) (mm)        ', round(avg_width, 3)],
                 ['Head Rice AGL       ', round(head_rice_AGL, 3)],
                 ['Whole Grain (qty)      ', head],
                 ['Whole Grain Weight (gm)     ', round(total_head_weight, 3)],
                 ['Broken Grain   (qty)      ', long],
                 ['Broken Grain Weight (gm)     ', round(
                     total_brokenRice_weight, 3)],
                 ['Total Grains (qty)    ', total_grains],
                 ['Reference Value (100g) (mm)',    x],
                 ['Yellow Grains (qty)    ', yellow_count],
                 ['Yellow Grains Weight (gm)    ', total_yellow_weight],
                 ['Yellow Percengate (%)    ', round(
                     (yellow_percentage*100), 3)],
                 ['Chalky Grains (qty)    ', chalky_count],
                 ['Chalky Grains Weight (gm)    ', total_chalky_weight],
                 ['Chalky Percengate (%)    ', round(
                     (chalky_percentage*100), 3)],
                 ['Damage Grains (qty)    ', new_damage1_count],
                 ['Damage Grains Weight (gm)    ', total_damage_weight],
                 ['Damage Percengate (%)    ', round(
                     (damage_percentage*100), 3)],
                 ['Paddy Grains (qty)    ', paddy_count],
                 ['Paddy Grains Weight (gm)    ', total_paddy_weight],
                 ['Paddy Percengate (%)    ', (paddy_percentage*100)],
                 ['Total Weight (gm)',    round(Total_new_weight, 3)],
                 ['Broken Rice Percengate',    round(
                     ((total_brokenRice_weight/Total_new_weight)*100), 3)],
                 ['Long Broken Weight', round(total_long_broken_weight, 3)],
                 ['Medium Broken Weight', round(
                     total_medium_broken_weight, 3)],
                 ['Small Broken Weight', round(total_small_broken_weight, 3)]
                 ]

        data4 = [['Range', "Count", "Average Length(AGL)", "Percent by Weight %"],
                 ["1mm to 2mm", _1mm_2mm, _1mm_2mm_agl, (_1mm_2mm_percentage*100)],
                 ["2mm to 3mm", _2mm_3mm, _2mm_3mm_agl, (_2mm_3mm_percentage*100)],
                 ["3mm to 4mm", _3mm_4mm, _3mm_4mm_agl, (_3mm_4mm_percentage*100)],
                 ["4mm to 5mm", _4mm_5mm, _4mm_5mm_agl, (_4mm_5mm_percentage*100)],
                 ["5mm to 6mm", _5mm_6mm, _5mm_6mm_agl, (_5mm_6mm_percentage*100)],
                 ["6mm to 7mm", _6mm_7mm, _6mm_7mm_agl, (_6mm_7mm_percentage*100)],
                 ["7mm to 8mm", _7mm_8mm, _7mm_8mm_agl, (_7mm_8mm_percentage*100)],
                 ["8mm to 9mm", _8mm_9mm, _8mm_9mm_agl, (_8mm_9mm_percentage*100)],
                 ["9mm to 10mm", _9mm_10mm, _9mm_10mm_agl, (_9mm_10mm_percentage*100)],
                 ]

    table2 = Table(data2, colWidths=[170, 150],
                   rowHeights=22.1)  # rowHeights=24.2
    table2.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    # leena
    ldata = (len(head_rice), len(broken_rice),
             len(med_broken), len(small_broken))
    ####

    cdata = (0, 1, 2, 3)
    tdata = (gtype[0], gtype[1], gtype[2], gtype[3])

    table2.wrapOn(c, 20, 400)  # 20,400, to set
    # c,20,25,,, to set report alignment increase or decrease the last value
    table2.drawOn(c, 20, 15)

    # leena
    # for user defined values
    table3 = Table(data3, colWidths=[100, 130], rowHeights=30)
    table3.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12)
    ]))

    table3.wrapOn(c, 20, 400)  # 20,400
    table3.drawOn(c, 360, 360)  # c,160,260
    ##

    c.showPage()

    # leena
    # for user defined values
    img = "img/header2.jpg"

    # path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img, 1, 640, width=650, height=150)
    table4 = Table(data4, colWidths=[100, 130], rowHeights=30)
    table4.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BACKGROUND',(0,0),(4,0),colors.lightskyblue) # (row start, column end), (row start, coulmn end)
    ]))

    table4.wrapOn(c, 20, 400)  # 20,400
    table4.drawOn(c, 70, 350)  # c,x,y
    ##

    c.save()
