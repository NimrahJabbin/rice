# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 09:27:31 2018


"""

######### This file is for 100 grain test ##############

# import the necessary packages
from __future__ import division
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
from PIL import Image, ImageTk, ImageEnhance
import os
import tensorflow as tf
from win32api import GetSystemMetrics




#leena
import globals
screen_width, screen_height= GetSystemMetrics(0),GetSystemMetrics(1)
#from report import no_type_selected,no_value_selected,no_user_input
nofile=1
##

#print(str(no_type_selected)+", "+str(no_value_selected)+", "+str(no_user_input))


##########Report Start
white1 =0
yb =0
brown=0
yellow = 0
filename=0

model = tf.keras.models.load_model('w.h5')
# ---------------------------------------------------------------------------
# Report Writing
# Report Writing
# ---------------------------------------------------------------------------
def calculate_no_of_grains(objects):
    print("Checking number of grains")
    print("The number of grains are:", len(objects))
    calculate_no_of_grains.no_of_grains = len(objects)
    return(calculate_no_of_grains.no_of_grains)

# Getting the user input (type_name) for Record Purpose and Broken Sizes Ratios selection
def calculate_type(selected_type):
    if selected_type is "":
        #global no_type_selected
        globals.no_type_selected=0
        print("The selected type is: empty")
    else:
        #global no_type_selected
        globals.no_type_selected=1
        print("The selected type is:", selected_type)
        calculate_type.result = selected_type
        #return result
    
    
# Getting user input (in mm) for broken size calculation
def get_user_input(x1):
    if x1 is "":
        #global no_user_input
        globals.no_user_input=0
        print("The user input is: empty")
    else:
        #global no_user_input
        globals.no_user_input=1
        
    print("The user input is:",x1 ,"mm")
    get_user_input.result1 = x1


#leena
#to get user desired data to be add on report
def get_sampleNo(sampleNo):
    globals.called=1
    if sampleNo is "":
        get_sampleNo.input="-"
    else:
        get_sampleNo.input = sampleNo

def get_date(date):
    globals.called=1
    if date is "":
        get_date.input="-"
    else:
        get_date.input = date

def get_day(day):
    globals.called=1
    if day is "":
        get_day.input="-"
    else:
        get_day.input = day

def get_arrivalNo(arrivalNo):
    globals.called=1
    if arrivalNo is "":
        get_arrivalNo.input="-"
    else:
        get_arrivalNo.input = arrivalNo

def get_partyName(partyName):
    globals.called=1
    if partyName is "":
        get_partyName.input="-"
    else:
        get_partyName.input = partyName

def get_vehicleNo(vehicleNo):
    globals.called=1
    if vehicleNo is "":
        get_vehicleNo.input="-"
    else:
        get_vehicleNo.input = vehicleNo

def get_riceType(riceType):
    globals.called=1
    if riceType is "":
        get_riceType.input="-"
    else:
        get_riceType.input = riceType

def get_moisture(moisture):
    globals.called=1
    if moisture is "":
        get_moisture.input="-"
    else:
        get_moisture.input = moisture

def get_look(look):
    globals.called=1
    if look is "":
        get_look.input="-"
    else:
        get_look.input = look

####

    
    
# Getting user input (in %) for broken size calculation
def get_user_input2(x2):
    print("The user input is:",x2 ,"%")
    get_user_input2.result2 = x2

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -----------------------------irri-6 Report------------------------------
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# Checking if 100 grains are there or not on the scanner
def gen_report_irri6(objects,S_Report):
    import time

    gtype = [0,0,0,0]
    global ldata, cdata, tdata, Date, Time, AGL, AGW
    head = 0
    long = 0
    med = 0
    small = 0

    yellow_weight = []
    damage_weight = []
    chalky_weight = []
    paddy_weight = []

    head_rice = []
    
    long_broken = []
    med_broken = []
    small_broken = []

    if globals.called is not 1:
        #if values are empty in that case
        get_sampleNo.input="-"
        get_date.input="-"
        get_day.input="-"
        get_arrivalNo.input="-"
        get_partyName.input="-"
        get_vehicleNo.input="-"
        get_riceType.input="-"
        get_moisture.input="-"
        get_look.input="-"
    ##

    
    whole_kernel = []
    PAGE_HEIGHT = defaultPageSize[0]
    PAGE_WIDTH = defaultPageSize[0]
    DefaultPageSize = letter
    c=canvas.Canvas(S_Report ,DefaultPageSize)


    img="img/header.jpg"

    #leena
    #path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img,1,640,width=650,height=150) 
    ##
    
    form = c.acroForm
    import datetime
    now = datetime.datetime.now()
    date= now.strftime("%d-%m-%Y")
    time= now.strftime("%I:%M:%S %p")
    c.setFont("Helvetica", 12)
    Time = "Test time : %s" %time
    c.setFont("Helvetica", 12)
    Date = "Test date : %s" %date
    
    total_grains=len(objects)
    
    AGL = round(sum(x['Length'] for x in objects)/len(objects),2)
    AGW = round(sum(x['Width'] for x in objects)/len(objects),2)
    #avg_area = round(sum(x['Area'] for x in objects)/len(objects),2)
    
    #Code to calculate Average length to Average Width Ratio
    AGL_to_AGW_ratio = round(float((AGL)/(AGW)),2)
    
    #Code for weight calculation
    #weight = round(total_grains*0.029,2)
    

    head=round(len(head_rice))
    
    long=round(len(long_broken))





    ## Making the logic of weighted average for yellow rice ##
                        ##   Start  ##
                        
    from analysis_irri6 import yellow_length, yellow_width
    from analysis_irri6 import yellow_count,new_damage1_count,chalky_count
    
    for i,j in zip(yellow_length, yellow_width):
            
            yellow_weight.append(model.predict([[float(i),float(j)]]))
            
    total_yellow_weight = round(sum(yellow_weight),3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)   


    ## Making the logic of weighted average for yellow rice ##
                        ##   End  ##
                        
    
    ## Making the logic of weighted average for damage rice ##
                        ##   Start  ##
                        
    from analysis_irri6 import damage_length, damage_width
    for i,j in zip(damage_length, damage_width):
            
            damage_weight.append(model.predict([[float(i),float(j)]]))
            
    total_damage_weight = round(sum(damage_weight),3)
    #print("\n\nThis is total weight of damage",total_damage_weight)
    
        ## Making the logic of weighted average for damage rice ##
                        ##   End  ##
                        
        ## Making the logic of weighted average for chalky rice ##
                        ##   Start  ##
                        
    from analysis_irri6 import chalky_length, chalky_width
    for i,j in zip(chalky_length, chalky_width):
            
            chalky_weight.append(model.predict([[float(i),float(j)]]))
            
    total_chalky_weight = round(sum(chalky_weight),3)
    #print("\n\nThis is total weight of chalky",total_chalky_weight)
    
        ## Making the logic of weighted average for chalky rice ##
                        ##   End  ##       
                        
    from analysis_irri6 import paddy_length, paddy_width
    for i,j in zip(paddy_length, paddy_width):
            paddy_weight.append(model.predict([[float(i),float(j)]]))
            #paddy_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))
            
    total_paddy_weight = round(float(sum(paddy_weight)),3)


    from analysis_irri6 import total_weight
    
    global paddy_percentage,yellow_percentage,chalky_percentage,damage_percentage
    yellow_percentage = round(float(total_yellow_weight/total_weight),2)
    chalky_percentage = round(float(total_chalky_weight/total_weight),2)
    damage_percentage = round(float(total_damage_weight/total_weight),2)
    paddy_percentage = round(float(total_paddy_weight/total_weight),2)

    data2=[[Time , Date],[' Variables        ',' Values  '], ['Average Grain Length (mm)      ',round(float(AGL),2)],
        ['Average Grain Width (mm)        ' ,round(float(AGW),2)],
        ['Aspect Ratio (mm)      ',AGL_to_AGW_ratio],
        ['Total Grains (qty)      ', total_grains],
        ['Total Weight (gm)      ', round(total_weight,2)],
        ['Yellow Grains (qty)    ', yellow_count],
        ['Yellow Grains Weight (gm)    ', total_yellow_weight],
        ['Chalky Grains (qty)    ', chalky_count],
        ['Chalky Grains Weight (gm)    ', total_chalky_weight]
        ]

    #leena
    data3=[['Sample No',get_sampleNo.input],
    ['Date', get_date.input],
    ['Time',get_day.input],
    ['Arrival No',get_arrivalNo.input],
    ['Party Name',get_partyName.input],
    ['Vehicle No',get_vehicleNo.input],
    ['Rice Type',get_riceType.input],
    ['Moisture',get_moisture.input],
    ['Look', get_look.input]
    ]
    ##

    table2 = Table(data2, colWidths=[160,150], rowHeights=40)
    table2.setStyle(TableStyle([
                            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                            ('FONTSIZE',(0,0),(-1,-1),12)
                            ]))
    
    ldata=(len(head_rice), len(long_broken), len(med_broken), len(small_broken))
    
    cdata=(1,2,3)
    tdata=(gtype[0], gtype[1], gtype[2], gtype[3])

    
    table2.wrapOn(c, 20, 400)
    table2.drawOn(c,20,190)    

    #leena
    #for user defined values
    table3 = Table(data3, colWidths=[100,130], rowHeights=30)
    table3.setStyle(TableStyle([
                            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                            ('FONTSIZE',(0,0),(-1,-1),12)
                            ]))

    
    table3.wrapOn(c, 20, 400)#20,400
    table3.drawOn(c,360,360)  #c,160,260  to set report alignment increase or decrease the last value
    ##

    c.save()
   

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -----------------------------1121 Report------------------------------
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#Generating report
def gen_report_1121(objects,S_Report):
    import time

    gtype = [0,0,0,0]
    global ldata, cdata, tdata, Date, Time, AGL, AGW
    head = 0
    long = 0
    med = 0
    small = 0

    yellow_weight = []
    damage_weight = []
    chalky_weight = []
    paddy_weight = []

    head_rice = []
    
    long_broken = []
    med_broken = []
    small_broken = []

    if globals.called is not 1:
        #if values are empty in that case
        get_sampleNo.input="-"
        get_date.input="-"
        get_day.input="-"
        get_arrivalNo.input="-"
        get_partyName.input="-"
        get_vehicleNo.input="-"
        get_riceType.input="-"
        get_moisture.input="-"
        get_look.input="-"
    ##

    
    whole_kernel = []
    PAGE_HEIGHT = defaultPageSize[0]
    PAGE_WIDTH = defaultPageSize[0]
    DefaultPageSize = letter
    c=canvas.Canvas(S_Report ,DefaultPageSize)


    img="img/header.jpg"

    #leena
    #path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img,1,640,width=650,height=150) 
    ##
    
    form = c.acroForm
    import datetime
    now = datetime.datetime.now()
    date= now.strftime("%d-%m-%Y")
    time= now.strftime("%I:%M:%S %p")
    c.setFont("Helvetica", 12)
    Time = "Test time : %s" %time
    c.setFont("Helvetica", 12)
    Date = "Test date : %s" %date
    
    total_grains=len(objects)
    
    AGL = round(sum(x['Length1'] for x in objects)/len(objects),2)
    AGW = round(sum(x['Width'] for x in objects)/len(objects),2)
    #avg_area = round(sum(x['Area'] for x in objects)/len(objects),2)
    
    #Code to calculate Average length to Average Width Ratio
    AGL_to_AGW_ratio = round(float((AGL)/(AGW)),2)
    
    #Code for weight calculation
    #weight = round(total_grains*0.029,2)
    

    head=round(len(head_rice))
    
    long=round(len(long_broken))





    ## Making the logic of weighted average for yellow rice ##
                        ##   Start  ##
                        
    from analysis_1121 import yellow_length, yellow_width
    from analysis_1121 import yellow_count,new_damage1_count,chalky_count
    
    for i,j in zip(yellow_length, yellow_width):
            
            yellow_weight.append(model.predict([[float(i),float(j)]]))
            
    total_yellow_weight = round(sum(yellow_weight),3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)   


    ## Making the logic of weighted average for yellow rice ##
                        ##   End  ##
                        
    
    ## Making the logic of weighted average for damage rice ##
                        ##   Start  ##
                        
    from analysis_1121 import damage_length, damage_width
    for i,j in zip(damage_length, damage_width):
            
            damage_weight.append(model.predict([[float(i),float(j)]]))
            
    total_damage_weight = round(sum(damage_weight),3)
    #print("\n\nThis is total weight of damage",total_damage_weight)
    
        ## Making the logic of weighted average for damage rice ##
                        ##   End  ##
                        
        ## Making the logic of weighted average for chalky rice ##
                        ##   Start  ##
                        
    from analysis_1121 import chalky_length, chalky_width
    for i,j in zip(chalky_length, chalky_width):
            
            chalky_weight.append(model.predict([[float(i),float(j)]]))
            
    total_chalky_weight = round(sum(chalky_weight),3)
    #print("\n\nThis is total weight of chalky",total_chalky_weight)
    
        ## Making the logic of weighted average for chalky rice ##
                        ##   End  ##       


    from analysis_1121 import paddy_length, paddy_width
    for i,j in zip(paddy_length, paddy_width):
            paddy_weight.append(model.predict([[float(i),float(j)]]))
            #paddy_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))
            
    total_paddy_weight = round(float(sum(paddy_weight)),3)


    from analysis_1121 import total_weight
    
    global paddy_percentage,yellow_percentage,chalky_percentage,damage_percentage
    yellow_percentage = round(float(total_yellow_weight/total_weight),2)
    chalky_percentage = round(float(total_chalky_weight/total_weight),2)
    damage_percentage = round(float(total_damage_weight/total_weight),2)
    paddy_percentage = round(float(total_paddy_weight/total_weight),2)
    
    

    data2=[[Time , Date],[' Variables        ',' Values  '], ['Average Grain Length (mm)      ',round(float(AGL),2)],
        ['Average Grain Width (mm)        ' ,round(float(AGW),2)],
        ['Aspect Ratio (mm)      ',AGL_to_AGW_ratio],
        ['Total Grains (qty)      ', total_grains],
        ['Total Weight (gm)      ', round(total_weight,2)],
        ['Yellow Grains (qty)    ', yellow_count],
        ['Yellow Grains Weight (gm)    ', total_yellow_weight],
        ['Chalky Grains (qty)    ', chalky_count],
        ['Chalky Grains Weight (gm)    ', total_chalky_weight]
        ]

    #leena
    data3=[['Sample No',get_sampleNo.input],
    ['Date', get_date.input],
    ['Time',get_day.input],
    ['Arrival No',get_arrivalNo.input],
    ['Party Name',get_partyName.input],
    ['Vehicle No',get_vehicleNo.input],
    ['Rice Type',get_riceType.input],
    ['Moisture',get_moisture.input],
    ['Look', get_look.input]
    ]
    ##

    table2 = Table(data2, colWidths=[160,150], rowHeights=40)
    table2.setStyle(TableStyle([
                            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                            ('FONTSIZE',(0,0),(-1,-1),12)
                            ]))
    
    ldata=(len(head_rice), len(long_broken), len(med_broken), len(small_broken))
    
    cdata=(1,2,3)
    tdata=(gtype[0], gtype[1], gtype[2], gtype[3])

    
    table2.wrapOn(c, 20, 400)
    table2.drawOn(c,20,190)    

    #leena
    #for user defined values
    table3 = Table(data3, colWidths=[100,130], rowHeights=30)
    table3.setStyle(TableStyle([
                            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                            ('FONTSIZE',(0,0),(-1,-1),12)
                            ]))

    
    table3.wrapOn(c, 20, 400)#20,400
    table3.drawOn(c,360,360)  #c,160,260  
    ##

    c.save()
        
        
        
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -----------------------------pk386 Report------------------------------
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    

#Generating report
def gen_report_pk386(objects,S_Report):
    import time

    gtype = [0,0,0,0]
    global ldata, cdata, tdata, Date, Time, AGL, AGW
    head = 0
    long = 0
    med = 0
    small = 0

    yellow_weight = []
    damage_weight = []
    chalky_weight = []
    paddy_weight = []

    head_rice = []
    
    long_broken = []
    med_broken = []
    small_broken = []

    if globals.called is not 1:
        #if values are empty in that case
        get_sampleNo.input="-"
        get_date.input="-"
        get_day.input="-"
        get_arrivalNo.input="-"
        get_partyName.input="-"
        get_vehicleNo.input="-"
        get_riceType.input="-"
        get_moisture.input="-"
        get_look.input="-"
    ##

    
    whole_kernel = []
    PAGE_HEIGHT = defaultPageSize[0]
    PAGE_WIDTH = defaultPageSize[0]
    DefaultPageSize = letter
    c=canvas.Canvas(S_Report ,DefaultPageSize)


    img="img/header.jpg"

    #leena
    #path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img,1,640,width=650,height=150) 
    ##
    
    form = c.acroForm
    import datetime
    now = datetime.datetime.now()
    date= now.strftime("%d-%m-%Y")
    time= now.strftime("%I:%M:%S %p")
    c.setFont("Helvetica", 12)
    Time = "Test time : %s" %time
    c.setFont("Helvetica", 12)
    Date = "Test date : %s" %date
    
    total_grains=len(objects)
    
    AGL = round(sum(x['Length1'] for x in objects)/len(objects),2)
    AGW = round(sum(x['Width'] for x in objects)/len(objects),2)
    #avg_area = round(sum(x['Area'] for x in objects)/len(objects),2)
    
    #Code to calculate Average length to Average Width Ratio
    AGL_to_AGW_ratio = round(float((AGL)/(AGW)),2)
    
    #Code for weight calculation
    #weight = round(total_grains*0.029,2)
    

    head=round(len(head_rice))
    
    long=round(len(long_broken))





    ## Making the logic of weighted average for yellow rice ##
                        ##   Start  ##
                        
    from analysis_pk386 import yellow_length, yellow_width
    from analysis_pk386 import yellow_count,new_damage1_count,chalky_count
    
    for i,j in zip(yellow_length, yellow_width):
            
            yellow_weight.append(model.predict([[float(i),float(j)]]))
            
    total_yellow_weight = round(sum(yellow_weight),3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)   


    ## Making the logic of weighted average for yellow rice ##
                        ##   End  ##
                        
    
    ## Making the logic of weighted average for damage rice ##
                        ##   Start  ##
                        
    from analysis_pk386 import damage_length, damage_width
    for i,j in zip(damage_length, damage_width):
            
            damage_weight.append(model.predict([[float(i),float(j)]]))
            
    total_damage_weight = round(sum(damage_weight),3)
    #print("\n\nThis is total weight of damage",total_damage_weight)
    
        ## Making the logic of weighted average for damage rice ##
                        ##   End  ##
                        
        ## Making the logic of weighted average for chalky rice ##
                        ##   Start  ##
                        
    from analysis_pk386 import chalky_length, chalky_width
    for i,j in zip(chalky_length, chalky_width):
            
            chalky_weight.append(model.predict([[float(i),float(j)]]))
            
    total_chalky_weight = round(sum(chalky_weight),3)
    #print("\n\nThis is total weight of chalky",total_chalky_weight)
    
        ## Making the logic of weighted average for chalky rice ##
                        ##   End  ##       


    from analysis_pk386 import paddy_length, paddy_width
    for i,j in zip(paddy_length, paddy_width):
            paddy_weight.append(model.predict([[float(i),float(j)]]))
            #paddy_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))
            
    total_paddy_weight = round(float(sum(paddy_weight)),3)


    from analysis_pk386 import total_weight
    
    global paddy_percentage,yellow_percentage,chalky_percentage,damage_percentage
    yellow_percentage = round(float(total_yellow_weight/total_weight),2)
    chalky_percentage = round(float(total_chalky_weight/total_weight),2)
    damage_percentage = round(float(total_damage_weight/total_weight),2)
    paddy_percentage = round(float(total_paddy_weight/total_weight),2)
    
    

    data2=[[Time , Date],[' Variables        ',' Values  '], ['Average Grain Length (mm)      ',round(float(AGL),2)],
        ['Average Grain Width (mm)        ' ,round(float(AGW),2)],
        ['Aspect Ratio (mm)      ',AGL_to_AGW_ratio],
        ['Total Grains (qty)      ', total_grains],
        ['Total Weight (gm)      ', round(total_weight,2)],
        ['Yellow Grains (qty)    ', yellow_count],
        ['Yellow Grains Weight (gm)    ', total_yellow_weight],
        ['Chalky Grains (qty)    ', chalky_count],
        ['Chalky Grains Weight (gm)    ', total_chalky_weight]
        ]

    #leena
    data3=[['Sample No',get_sampleNo.input],
    ['Date', get_date.input],
    ['Time',get_day.input],
    ['Arrival No',get_arrivalNo.input],
    ['Party Name',get_partyName.input],
    ['Vehicle No',get_vehicleNo.input],
    ['Rice Type',get_riceType.input],
    ['Moisture',get_moisture.input],
    ['Look', get_look.input]
    ]
    ##

    table2 = Table(data2, colWidths=[160,150], rowHeights=40)
    table2.setStyle(TableStyle([
                            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                            ('FONTSIZE',(0,0),(-1,-1),12)
                            ]))
    
    ldata=(len(head_rice), len(long_broken), len(med_broken), len(small_broken))
    
    cdata=(1,2,3)
    tdata=(gtype[0], gtype[1], gtype[2], gtype[3])

    
    table2.wrapOn(c, 20, 400)
    table2.drawOn(c,20,190)    

    #leena
    #for user defined values
    table3 = Table(data3, colWidths=[100,130], rowHeights=30)
    table3.setStyle(TableStyle([
                            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                            ('FONTSIZE',(0,0),(-1,-1),12)
                            ]))

    
    table3.wrapOn(c, 20, 400)#20,400
    table3.drawOn(c,360,360)  #c,160,260  
    ##

    c.save()
        
        
        
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# -----------------------------brown Report------------------------------
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        
#Generating report
def gen_report_brown(objects,S_Report):
    import time

    gtype = [0,0,0,0]
    global ldata, cdata, tdata, Date, Time, AGL, AGW
    head = 0
    long = 0
    med = 0
    small = 0

    yellow_weight = []
    damage_weight = []
    chalky_weight = []
    paddy_weight = []

    head_rice = []
    
    long_broken = []
    med_broken = []
    small_broken = []

    if globals.called is not 1:
        #if values are empty in that case
        get_sampleNo.input="-"
        get_date.input="-"
        get_day.input="-"
        get_arrivalNo.input="-"
        get_partyName.input="-"
        get_vehicleNo.input="-"
        get_riceType.input="-"
        get_moisture.input="-"
        get_look.input="-"
    ##

    
    whole_kernel = []
    PAGE_HEIGHT = defaultPageSize[0]
    PAGE_WIDTH = defaultPageSize[0]
    DefaultPageSize = letter
    c=canvas.Canvas(S_Report ,DefaultPageSize)


    img="img/header.jpg"

    #leena
    #path, position of x-axis, position of y-axis, width, height)
    c.drawImage(img,1,640,width=650,height=150) 
    ##
    
    form = c.acroForm
    import datetime
    now = datetime.datetime.now()
    date= now.strftime("%d-%m-%Y")
    time= now.strftime("%I:%M:%S %p")
    c.setFont("Helvetica", 12)
    Time = "Test time : %s" %time
    c.setFont("Helvetica", 12)
    Date = "Test date : %s" %date
    
    total_grains=len(objects)
    
    AGL = round(sum(x['Length1'] for x in objects)/len(objects),2)
    AGW = round(sum(x['Width'] for x in objects)/len(objects),2)
    #avg_area = round(sum(x['Area'] for x in objects)/len(objects),2)
    
    #Code to calculate Average length to Average Width Ratio
    AGL_to_AGW_ratio = round(float((AGL)/(AGW)),2)
    
    #Code for weight calculation
    #weight = round(total_grains*0.029,2)
    

    head=round(len(head_rice))
    
    long=round(len(long_broken))





    ## Making the logic of weighted average for yellow rice ##
                        ##   Start  ##
                        
    from analysis_brown import yellow_length, yellow_width
    from analysis_brown import yellow_count,new_damage1_count,chalky_count
    
    for i,j in zip(yellow_length, yellow_width):
            
            yellow_weight.append(model.predict([[float(i),float(j)]]))
            
    total_yellow_weight = round(sum(yellow_weight),3)
    #print("\n\nThis is total weight of yellow",total_yellow_weight)   


    ## Making the logic of weighted average for yellow rice ##
                        ##   End  ##
                        
    
    ## Making the logic of weighted average for damage rice ##
                        ##   Start  ##
                        
    from analysis_brown import damage_length, damage_width
    for i,j in zip(damage_length, damage_width):
            
            damage_weight.append(model.predict([[float(i),float(j)]]))
            
    total_damage_weight = round(sum(damage_weight),3)
    #print("\n\nThis is total weight of damage",total_damage_weight)
    
        ## Making the logic of weighted average for damage rice ##
                        ##   End  ##
                        
        ## Making the logic of weighted average for chalky rice ##
                        ##   Start  ##
                        
    from analysis_brown import chalky_length, chalky_width
    for i,j in zip(chalky_length, chalky_width):
            
            chalky_weight.append(model.predict([[float(i),float(j)]]))
            
    total_chalky_weight = round(sum(chalky_weight),3)
    #print("\n\nThis is total weight of chalky",total_chalky_weight)
    
        ## Making the logic of weighted average for chalky rice ##
                        ##   End  ##       


    from analysis_brown import paddy_length, paddy_width
    for i,j in zip(paddy_length, paddy_width):
            paddy_weight.append(model.predict([[float(i),float(j)]]))
            #paddy_weight.append(round((((-0.00994)+(0.00167*i))+(0.00663*j)),5))
            
    total_paddy_weight = round(float(sum(paddy_weight)),3)


    from analysis_brown import total_weight
    
    global paddy_percentage,yellow_percentage,chalky_percentage,damage_percentage
    yellow_percentage = round(float(total_yellow_weight/total_weight),2)
    chalky_percentage = round(float(total_chalky_weight/total_weight),2)
    damage_percentage = round(float(total_damage_weight/total_weight),2)
    paddy_percentage = round(float(total_paddy_weight/total_weight),2)

    data2=[[Time , Date],[' Variables        ',' Values  '], ['Average Grain Length (mm)      ',round(float(AGL),2)],
        ['Average Grain Width (mm)        ' ,round(float(AGW),2)],
        ['Aspect Ratio (mm)      ',AGL_to_AGW_ratio],
        ['Total Grains (qty)      ', total_grains],
        ['Total Weight (gm)      ', round(total_weight,2)],
        ['Yellow Grains (qty)    ', yellow_count],
        ['Yellow Grains Weight (gm)    ', total_yellow_weight],
        ['Chalky Grains (qty)    ', chalky_count],
        ['Chalky Grains Weight (gm)    ', total_chalky_weight]
        ]

    #leena
    data3=[['Sample No',get_sampleNo.input],
    ['Date', get_date.input],
    ['Time',get_day.input],
    ['Arrival No',get_arrivalNo.input],
    ['Party Name',get_partyName.input],
    ['Vehicle No',get_vehicleNo.input],
    ['Rice Type',get_riceType.input],
    ['Moisture',get_moisture.input],
    ['Look', get_look.input]
    ]
    ##

    table2 = Table(data2, colWidths=[160,150], rowHeights=40)
    table2.setStyle(TableStyle([
                            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                            ('FONTSIZE',(0,0),(-1,-1),12)
                            ]))
    
    ldata=(len(head_rice), len(long_broken), len(med_broken), len(small_broken))
    
    cdata=(1,2,3)
    tdata=(gtype[0], gtype[1], gtype[2], gtype[3])

    
    table2.wrapOn(c, 20, 400)
    table2.drawOn(c,20,190)    

    #leena
    #for user defined values
    table3 = Table(data3, colWidths=[100,130], rowHeights=30)
    table3.setStyle(TableStyle([
                            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                            ('FONTSIZE',(0,0),(-1,-1),12)
                            ]))

    
    table3.wrapOn(c, 20, 400)#20,400
    table3.drawOn(c,360,360)  #c,160,260  
    ##

    c.save()