# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 02:32:55 2018

@author: Muzammil, Leena, Khalid, Ahsan

Rice type pk-386
"""
# Importing Libraries
from scipy.spatial import distance as dist
from tensorflow.python.ops.numpy_ops import *
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.python.keras.engine import base_layer_v1

from distutils.dir_util import copy_tree
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
from imutils import perspective
from imutils import contours
import concurrent.futures
from multiprocessing.pool import ThreadPool
import numpy as np
import pythoncom
import os
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import re
import imutils
import cv2
from numpy import array
import pandas as pd
import threading
import multiprocessing
from multiprocessing import Process
import shutil 


from reportlab.platypus import SimpleDocTemplate, Table, TableStyle , Paragraph
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from bidi.algorithm import get_display
from rtl import reshaper
from reportlab.platypus import SimpleDocTemplate, Paragraph
from textwrap3 import wrap
from reportlab.graphics.charts.legends import Legend
from reportlab.pdfbase.ttfonts import TTFont
from time import process_time


r=0
orig = 0
global leng
global weight


# function definition of mid-point and color conversion from RGB to HEX
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

def rgb2hex(r,g,b):
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    return hex


# Muzammil's functions definition

def yellowDetection():
    x = os.listdir("scan")
    #print(np.__version__)
    count = 0
    for i in x:
        image = cv2.imread('scan/'+str(i))
        original = image.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        #this is yellow values
        # lower = np.array([0, 84, 57], dtype="uint8")
        # upper = np.array([179 , 255, 255], dtype="uint8")
        #this is red values
        lower = np.array([0,56,104], dtype="uint8")
        upper = np.array([45  , 246, 153], dtype="uint8")
        mask = cv2.inRange(image, lower, upper)
        count = count + 1
        if not os.path.exists('yellow'):
            os.makedirs('yellow')
        cv2.imwrite("yellow/"+ str(i) , mask)

def chalkyDetection():
    x = os.listdir("scan")
    count = 0
    for i in x:
        image = cv2.imread('scan/'+str(i))
        original = image.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        #this is yellow values
        # lower = np.array([0, 84, 57], dtype="uint8")
        # upper = np.array([179 , 255, 255], dtype="uint8")
        #this is red values
        lower = np.array([25, 25, 75], dtype="uint8")
        upper = np.array([67 , 195, 255], dtype="uint8")
        mask = cv2.inRange(image, lower, upper)
        count = count + 1
        if not os.path.exists('chaly_temp'):
            os.makedirs('chaly_temp')
        cv2.imwrite("chaly_temp/"+ str(i) , mask)

def pergrain(path1,path2):
    counter1 = 0
    leng1 = [] 
    width1 = []
    filename = []
    filename1 = []
    x89 = os.listdir(path1)
    x891 = os.listdir(path2)
    fazool = 0
    fazool1 = 0
    a = []
    b = []
    

    for (i,j) in zip(x89,x891):
        # load our input image, convert it to grayscale, and blur it slightly
        image = cv2.imread(str(path1)+"/"+str(i))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)
        # perform edge detection, then perform a dilation + erosion to
        # close gaps in between object edges
        edged = cv2.Canny(gray, 50, 100)
        edged = cv2.dilate(edged, None, iterations=1)
        edged = cv2.erode(edged, None, iterations=1)

        image1 = cv2.imread(str(path2)+"/"+str(j))
        gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        gray1 = cv2.GaussianBlur(gray1, (7, 7), 0)
        # perform edge detection, then perform a dilation + erosion to
        # close gaps in between object edges
        edged1 = cv2.Canny(gray1, 50, 100)
        edged1 = cv2.dilate(edged1, None, iterations=1)
        edged1 = cv2.erode(edged1, None, iterations=1)

        # find contours in the edge map
        #cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
            #cv2.CHAIN_APPROX_SIMPLE)
        #cnts = imutils.grab_contours(cnts)
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        # sort the contours from left-to-right and initialize the bounding box
        cnts1 = cv2.findContours(edged1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cnts1 = cnts1[0] if imutils.is_cv2() else cnts1[1]


        try:
            (cnts, _) = contours.sort_contours(cnts)
        except:
            fazool = fazool + 1

        try:
            (cnts1, _) = contours.sort_contours(cnts1)
        except:
            fazool1 = fazool1 + 1

        # loop over the contours individually
        
        for c in cnts:
            vb = cv2.contourArea(c)
            if vb > 200:
                a.append(vb)
                filename.append(i)
        for kl in cnts1:
            klo = cv2.contourArea(kl)
            if klo >200:
                b.append(klo)
                filename1.append(j)
    
    #for (jj,kk,dd) in zip(a,b)
    if len(filename) == len(filename1): 
        print("these are the values is true")
    else:
        print("these values are false")
        

            
            
    #return counter1, filename


def damage(path):
    #pythoncom.CoInitialize()
    x009 = os.listdir(path)
    t1_start = process_time()
    new_model12 = tf.keras.models.load_model('mpil', compile=False)
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the MODELLOAD program in seconds:", 
                                         t1_stop-t1_start)
                                         
    damage_co = 0
    damage_na = []
    chalky_co = 0
    chalky_na = []
    
    
    for i in x009:
        img = image.load_img(str(path)+str(i), target_size=(32,32,3))
        img = image.img_to_array(img)
        img = img/255
        f1 = np.array(img)
        f3 = f1.reshape(1,32,32,-1)
        predictionsc111 = new_model12.predict(f3)

        #find max indexed array
        max_index111 = np.argmax(predictionsc111)

        emotions111 = ('chalky', 'damage', 'undamage')
        predicted_emotion1111 = emotions111[max_index111]
        if predicted_emotion1111 == "damage":
            damage_co = damage_co + 1
            damage_na.append(str(i))
            #np.append(damage_na,str(i))
        elif predicted_emotion1111 == "chalky":
            chalky_co = chalky_co + 1
            chalky_na.append(str(i))
            #np.append(chalky_na,str(i))
        
    return damage_co, damage_na, chalky_co, chalky_na

def new_damage(path):
    #pythoncom.CoInitialize()
    x009 = os.listdir(path)
    t1_start = process_time()
    new_model12 = tf.keras.models.load_model('cos.h5')
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the MODELLOAD program in seconds:", 
                                         t1_stop-t1_start)
                                         
    damage_co = 0
    damage_na = []
    
    for i in x009:
        img = image.load_img(str(path)+str(i), target_size=(32,32,3))
        img = image.img_to_array(img)
        img = img/255
        f1 = np.array(img)
        f3 = f1.reshape(1,32,32,-1)
        pred7651 = new_model12.predict(f3)
        new_pred12151 = int(round(pred7651))
        if new_pred12151 == 0:
            damage_co = damage_co + 1
            damage_na.append(i)
    
    return damage_co, damage_na,

def pad(img, w=200, h=200):
    #  in case when you have odd number
    top_pad = np.floor((h - img.shape[0]) / 2).astype(np.uint16)
    bottom_pad = np.ceil((h - img.shape[0]) / 2).astype(np.uint16)
    right_pad = np.ceil((w - img.shape[1]) / 2).astype(np.uint16)
    left_pad = np.floor((w - img.shape[1]) / 2).astype(np.uint16)
    return np.copy(np.pad(img, ((top_pad, bottom_pad), (left_pad, right_pad), (0, 0)), mode='constant', constant_values=0))


def new_damage2(path):
    #pythoncom.CoInitialize()
    x009 = os.listdir(path)
    t1_start = process_time()
    new_model12 = tf.keras.models.load_model('second_scanner.h5')
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the MODELLOAD program in seconds:", 
                                         t1_stop-t1_start)
                                         
    damage_co = 0
    damage_na = []
    ui = []
    
    if len(x009) >= 1:
        for i in x009:
            img = image.load_img(str(path)+str(i))
            img = image.img_to_array(img)
            img = pad(img)
            img = img/255
            ui.append(img)
        pos1 = np.array(ui)
        pred7651 = new_model12.predict(pos1)
        new_pred12151 = [int(round(p[0])) for p in pred7651]
        for (k,l) in zip(new_pred12151,x009) :
            if k == 0:
                damage_co = damage_co + 1
                damage_na.append(l)
    
    return damage_co, damage_na,

def paddy(path):
    #pythoncom.CoInitialize()
    x009 = os.listdir(path)
    t1_start = process_time()
    new_model12 = tf.keras.models.load_model('paddy.h5')
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the MODELLOAD program in seconds:", 
                                         t1_stop-t1_start)
                                         
    paddy_co = 0
    paddy_na = []
    ui = []
    
    for i in x009:
        img = image.load_img(str(path)+str(i))
        img = image.img_to_array(img)
        img = pad(img)
        img = img/255
        ui.append(img)
    pos1 = np.array(ui)
    pred7651 = new_model12.predict(pos1)
    new_pred12151 = [int(round(p[0])) for p in pred7651]
    for (k,l) in zip(new_pred12151,x009) :
        if k == 1:
            paddy_co = paddy_co + 1
            paddy_na.append(l)
    
    return paddy_co, paddy_na,


def chalkynames(path1):
    counter1 = 0
    leng1 = [] 
    width1 = []
    filename = []
    try:
        x89 = os.listdir(path1)
    except:
        pass
    fazool = 0
    
    if os.path.exists(path1): 
        for i in x89:
            # load our input image, convert it to grayscale, and blur it slightly
            image = cv2.imread(str(path1)+"/"+str(i))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (7, 7), 0)
            # perform edge detection, then perform a dilation + erosion to
            # close gaps in between object edges
            edged = cv2.Canny(gray, 50, 100)
            edged = cv2.dilate(edged, None, iterations=1)
            edged = cv2.erode(edged, None, iterations=1)

            # find contours in the edge map
            #cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                #cv2.CHAIN_APPROX_SIMPLE)
            #cnts = imutils.grab_contours(cnts)
            cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            cnts = cnts[0] if imutils.is_cv2() else cnts[1]
            # sort the contours from left-to-right and initialize the bounding box
            try:
                (cnts, _) = contours.sort_contours(cnts)
            except:
                fazool = fazool + 1
                
            pixelsPerMetric = None
            object_num=0
            r=object_num
            objects = []

            idx=0

            waitTime = 33

            # loop over the contours individually
            for c in cnts:
            # if the contour is not sufficiently large, ignore it

                if cv2.contourArea(c) < 200:
                    continue
                # compute the rotated bounding box of the contour
                orig = image.copy()
                box = cv2.minAreaRect(c)
                box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
                box = np.array(box, dtype="int")
                # order the points in the contour such that they appear
                # in top-left, top-right, bottom-right, and bottom-left
                # order, then draw the outline of the rotated bounding
                # box
                box = perspective.order_points(box)
                cv2.drawContours(orig, [c], -1, (0, 255, 0), 2)
                box.astype
                # unpack the ordered bounding box, then compute the midpoint
                # between the top-left and top-right coordinates, followed by
                # the midpoint between bottom-left and bottom-right coordinates
                (tl, tr, br, bl) = box
                (tltrX, tltrY) = midpoint(tl, tr)
                (blbrX, blbrY) = midpoint(bl, br)
                # compute the midpoint between the top-left and top-right points,
                # followed by the midpoint between the top-righ and bottom-right
                (tlblX, tlblY) = midpoint(tl, bl)
                (trbrX, trbrY) = midpoint(tr, br)

                # compute the Euclidean distance between the midpoints
                dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
                dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
                # if the pixels per metric has not been initialized, then
                # compute it as the ratio of pixels to supplied metric
                # (in this case, inches)
                if pixelsPerMetric is None:
                    pixelsPerMetric = 14.0

                dimA = dA / pixelsPerMetric
                dimB = dB / pixelsPerMetric
                if (dimA >= dimB):
                    temp=dimA
                    dimA=dimB
                    dimB=temp
                leng1.append(float(dimB))
                width1.append(float(dimA))
                filename.append(i)
                counter1 = counter1 +1
    return counter1, filename
    # else:
    #     return counter1, filename

def Calculation():
    counter1 = 0
    leng1 = [] 
    width1 = []
    filename = []
    try:
        x89 = os.listdir("yellow")
    except:
        pass
    fazool = 0
    
    if os.path.exists("yellow"): 
        for i in x89:
            # load our input image, convert it to grayscale, and blur it slightly
            image = cv2.imread("yellow/"+str(i))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (7, 7), 0)
            # perform edge detection, then perform a dilation + erosion to
            # close gaps in between object edges
            edged = cv2.Canny(gray, 50, 100)
            edged = cv2.dilate(edged, None, iterations=1)
            edged = cv2.erode(edged, None, iterations=1)

            # find contours in the edge map
            #cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                #cv2.CHAIN_APPROX_SIMPLE)
            #cnts = imutils.grab_contours(cnts)
            cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            cnts = cnts[0] if imutils.is_cv2() else cnts[1]
            # sort the contours from left-to-right and initialize the bounding box
            try:
                (cnts, _) = contours.sort_contours(cnts)
            except:
                fazool = fazool + 1
                
            pixelsPerMetric = None
            object_num=0
            r=object_num
            objects = []

            idx=0

            waitTime = 33

            # loop over the contours individually
            for c in cnts:
            # if the contour is not sufficiently large, ignore it

                if cv2.contourArea(c) < 370:
                    continue
                # compute the rotated bounding box of the contour
                orig = image.copy()
                box = cv2.minAreaRect(c)
                box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
                box = np.array(box, dtype="int")
                # order the points in the contour such that they appear
                # in top-left, top-right, bottom-right, and bottom-left
                # order, then draw the outline of the rotated bounding
                # box
                box = perspective.order_points(box)
                cv2.drawContours(orig, [c], -1, (0, 255, 0), 2)
                box.astype
                # unpack the ordered bounding box, then compute the midpoint
                # between the top-left and top-right coordinates, followed by
                # the midpoint between bottom-left and bottom-right coordinates
                (tl, tr, br, bl) = box
                (tltrX, tltrY) = midpoint(tl, tr)
                (blbrX, blbrY) = midpoint(bl, br)
                # compute the midpoint between the top-left and top-right points,
                # followed by the midpoint between the top-righ and bottom-right
                (tlblX, tlblY) = midpoint(tl, bl)
                (trbrX, trbrY) = midpoint(tr, br)

                # compute the Euclidean distance between the midpoints
                dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
                dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
                # if the pixels per metric has not been initialized, then
                # compute it as the ratio of pixels to supplied metric
                # (in this case, inches)
                if pixelsPerMetric is None:
                    pixelsPerMetric = 14.0

                dimA = dA / pixelsPerMetric
                dimB = dB / pixelsPerMetric
                if (dimA >= dimB):
                    temp=dimA
                    dimA=dimB
                    dimB=temp
                leng1.append(float(dimB))
                width1.append(float(dimA))
                filename.append(i)
                counter1 = counter1 +1
    return leng1 , width1 , counter1, filename
    # else:
    #     return leng1 , width1 , counter1, filename




def cal(redfilename):

    leng1 = [] 
    width1 = []
    fazool1 = 0
    
    if len(redfilename) >= 1:

        for i in redfilename:
            # load our input image, convert it to grayscale, and blur it slightly
            image = cv2.imread("scan/"+str(i))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (7, 7), 0)
            # perform edge detection, then perform a dilation + erosion to
            # close gaps in between object edges
            edged = cv2.Canny(gray, 50, 100)
            edged = cv2.dilate(edged, None, iterations=1)
            edged = cv2.erode(edged, None, iterations=1)

            # find contours in the edge map
            cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            # sort the contours from left-to-right and initialize the bounding box
            try:
                (cnts, _) = contours.sort_contours(cnts)
            except:
                fazool1 = fazool1 + 1

            pixelsPerMetric = None
            object_num=0
            r=object_num
            objects = []

            idx=0

            waitTime = 33

            # loop over the contours individually
            for c in cnts:
            # if the contour is not sufficiently large, ignore it
                #print("This is contour value",cv2.contourArea(c))
                if cv2.contourArea(c) < 90:
                    #print("succeed")
                    continue
                # compute the rotated bounding box of the contour
                #print(chalky_input.result)
                orig = image.copy()
                box = cv2.minAreaRect(c)
                box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
                box = np.array(box, dtype="int")
                # order the points in the contour such that they appear
                # in top-left, top-right, bottom-right, and bottom-left
                # order, then draw the outline of the rotated bounding
                # box
                box = perspective.order_points(box)
                cv2.drawContours(orig, [c], -1, (0, 255, 0), 2)
                box.astype
                        # unpack the ordered bounding box, then compute the midpoint
                        # between the top-left and top-right coordinates, followed by
                        # the midpoint between bottom-left and bottom-right coordinates
                (tl, tr, br, bl) = box
                (tltrX, tltrY) = midpoint(tl, tr)
                (blbrX, blbrY) = midpoint(bl, br)
                # compute the midpoint between the top-left and top-right points,
                # followed by the midpoint between the top-righ and bottom-right
                (tlblX, tlblY) = midpoint(tl, bl)
                (trbrX, trbrY) = midpoint(tr, br)

                # compute the Euclidean distance between the midpoints
                dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
                dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
                # if the pixels per metric has not been initialized, then
                # compute it as the ratio of pixels to supplied metric
                # (in this case, inches)
                if pixelsPerMetric is None:
                    pixelsPerMetric = 14.0

                dimA = dA / pixelsPerMetric
                dimB = dB / pixelsPerMetric
                if (dimA >= dimB):
                    temp=dimA
                    dimA=dimB
                    dimB=temp
                leng1.append(float(dimB))
                width1.append(float(dimA))
    return leng1 , width1




print("[INFO] loading network...")


def analyze(image,D_Report):

    global orig , r

    # load the image, convert it to grayscale, and blur it slightly
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]

    # perform edge detection, then perform a dilation + erosion to
    # close gaps in between object edges
    edged = cv2.Canny(thresh, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)

    # find contours in the edge map
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    # sort the contours from left-to-right and initialize the
    # 'pixels per metric' calibration variable
    (cnts, _) = contours.sort_contours(cnts)
    pixelsPerMetric = None

    object_num=0
    r=object_num
    objects = []
    
    idx=0

    orig = image.copy()
    counter = 0
    leng = [0] * 1000
    width = [0] * 1000
    leng1 = [0] * 1000
    # width1 = [0] * 1000
    weight = [0] * 1000

    # loop over the contours individually
    for c in cnts:
        # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 90:
            continue

        # compute the rotated bounding box of the contour
        box = cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        box = np.array(box, dtype="int")

        # order the points in the contour such that they appear
        # in top-left, top-right, bottom-right, and bottom-left
    	# order, then draw the outline of the rotated bounding box
        box = perspective.order_points(box)
        cv2.drawContours(orig, [c], -1, (0, 255, 0), 2)
        box.astype

    	 # unpack the ordered bounding box, then compute the midpoint
    	 # between the top-left and top-right coordinates, followed by
    	 # the midpoint between bottom-left and bottom-right coordinates
        (tl, tr, br, bl) = box
        (tltrX, tltrY) = midpoint(tl, tr)
        (blbrX, blbrY) = midpoint(bl, br)

    	 # compute the midpoint between the top-left and top-right points,
    	 # followed by the midpoint between the top-right and bottom-right
        (tlblX, tlblY) = midpoint(tl, bl)
        (trbrX, trbrY) = midpoint(tr, br)

    	 # compute the Euclidean distance between the midpoints
        dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
        dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

    	 # if the pixels per metric has not been initialized, then
    	 # compute it as the ratio of pixels to supplied metric (in this case, inches)
        if pixelsPerMetric is None:

            #pixelsPerMetric = dB / 22.6 # For 2 Rupee Coin
            #pixelsPerMetric = dB / 24.0 # For old 5 Rupee Coin
            #pixelsPerMetric = 12.5  # For Lide 220
            #pixelsPerMetric = 11.7699  # For Lide 300 (Not giving accurate results on this value)
            #pixelsPerMetric = 11.81 #again get the ppm on Lide 300 and its give 99% accurate results
            #pixelsPerMetric = 11.8226
            #pixelsPerMetric = 12.5
            #pixelsPerMetric = 11.8141529292035397

            pixelsPerMetric = 12.87
            
            
            #print("This is dB, Width", dB)
            print("This is PPM",pixelsPerMetric)

        dimA = round(dA / pixelsPerMetric, 3)
        dimB = round(dB / pixelsPerMetric, 3)

        if (dimA >= dimB):
            temp=dimA
            dimA=dimB
            dimB=temp
        
        leng[counter] = float(dimB)
        width[counter] = float(dimA)
        #leng1[counter] = float(dimB+0.8)
        # width1[counter] = float(dimA+0.8)
        counter = counter +1
        
        x,y,w,h = cv2.boundingRect(c)
        x1,y1,w1,h1 = cv2.boundingRect(c)
        x1 = x1 + -5  
        y1 = y1 + -10
        w1 = w1 + 15
        h1 = h1 + 15
        ROI = image[y1:y1+h1, x1:x1+w1] 
        
        if not os.path.exists('scan'):
                os.makedirs('scan')
                
        cv2.imwrite("scan/"+ str(counter) +".jpg", ROI)
        idx+=1
        
        mask = np.zeros(image.shape[:2],np.uint8)
        cv2.drawContours(mask, [c],-1, 255, -1)
        dst = cv2.bitwise_and(image, image, mask=mask)
        new_img=dst[y-20:y+h+20,x-20:x+w+20]


        object_num = object_num+1
        #image1 = cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB)
        #image1 = new_img.reshape((image1.shape[0] * new_img.shape[1], 3))


        obj_num=object_num # because one item on the left most side we have for the pixel constant value
        #dominant_color
        global content
        content = {
                "Object_number": obj_num,
                "Width": dimA,
                "Length": dimB,
                "Length1": (dimB+0.50)}
        objects.append(content)

        # Detailed Report 
        doc = SimpleDocTemplate(D_Report)#D_Report
        from  reportlab.lib.styles import ParagraphStyle as PS
        h1 = PS(
            name = 'Heading1',
            fontSize = 14,
            leading = 16,
            alignment = 1,
            spaceAfter = 10)
        h2 = PS(name = 'Heading2',
            fontSize = 12,
            leading = 14,
            alignment = 1,
            spaceAfter = 20)
        import datetime
        now = datetime.datetime.now()
        now.strftime("%A")
        date= now.strftime("%d-%m-%Y")
        time= now.strftime("%I:%M:%S %p")
        
        Time = "Test time : %s" %time
        
        Date = "Test date : %s" %date
        
        # container for the "Flowable" objects
        elements = []
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_RIGHT
        
        elements.append(Paragraph('Detailed Report of Rice Sample\n', h1))
        
        elements.append(Paragraph("Test time : %s" %time + "  And Test date : %s" %date, h2))

		#Make heading for each column and start data list
        column1Heading = "Item No. "
        column2Heading = "Length (mm)"
        column3Heading = "Width (mm)"
        column4Heading = "Weight (gm)"

        # Assemble data for each column using simple loop to append it into data list
        data = [[column1Heading,column2Heading,column3Heading,column4Heading]]
        f = object_num
        
        global total_weight
        total_weight = 0

        for i in range(0,f):
            
            #weight[i] = float(round((((-0.00860)+(0.00167*leng[i]))+(0.00663*(width[i]))),5))
            
            weight[i] = float(round((((-0.00994)+(0.00161*leng[i]))+(0.00663*(width[i]))),5))
            data.append([str(i),leng[i],width[i],weight[i]])
            
            total_weight = total_weight + weight[i]
        
        
        tableThatSplitsOverPages = Table(data, [2 * cm, 5 * cm, 5 * cm], repeatRows=1)
        tableThatSplitsOverPages.hAlign = 'CENTER'
        tblStyle = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
		                       ('VALIGN',(0,0),(-1,-1),'TOP'),
		                       ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
		                       ('BOX',(0,0),(-1,-1),1,colors.black),
		                       ('BOX',(0,0),(0,-1),1,colors.black)])
        tblStyle.add('BACKGROUND',(0,0),(1,0),colors.lightblue)
        tblStyle.add('BACKGROUND',(0,0),(2,2),colors.lightblue)
        tblStyle.add('BACKGROUND',(0,0),(3,3),colors.lightblue)
        tblStyle.add('BACKGROUND',(0,1),(-1,-1),colors.white)
        tableThatSplitsOverPages.setStyle(tblStyle)
        elements.append(tableThatSplitsOverPages)
        doc.build(elements)

        # draw the object sizes on the image
        cv2.putText(orig, str(obj_num),(int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,1,
                   (255, 255, 255), 1)

            
        cv2.putText(orig, "{}".format(obj_num),
            (int(box[0][0] - 15), int(box[0][1] - 15)),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)


    x899 = os.listdir("scan")
    for cp in x899:
        if not os.path.exists('scan_copy'):
            os.makedirs('scan_copy')
        shutil.copy("scan/"+str(cp), "scan_copy/")
        
    global yellow_length, yellow_width, yellow_count, yellow_filename, yellow_check, damage_count, damage_name, chalky_count, chalky_name, damage_length, damage_width, chalky_length, chalky_width, undamage_length, undamage_width,new_damage1_count ,paddy_length, paddy_width,paddy_count, new_damage1_name, paddy_name
        
    # Ahsan checking process time
    paddy_count, paddy_name = paddy("scan/")
    paddy_length, paddy_width = cal(paddy_name)
    print("Paddy Rice : ",paddy_count)
    for move109 in paddy_name:
        if not os.path.exists('paddy'):
            os.makedirs('paddy')
        shutil.copy("scan/"+str(move109), "paddy/")
    for delete109 in paddy_name:
        if os.path.exists("scan/"+ delete109):
            os.remove("scan/"+ delete109)
    t1_start = process_time()
    yellowDetection()
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)  
    print("Elapsed time during the YELLOW program in seconds:", 
                                         t1_stop-t1_start) 
    
    #global yellow_length, yellow_width, yellow_count, yellow_filename, yellow_check, damage_count, damage_name, chalky_count, chalky_name, damage_length, damage_width, chalky_length, chalky_width, undamage_length, undamage_width,new_damage1_count ,paddy_length, paddy_width,paddy_count, new_damage1_name
    yellow_length, yellow_width, yellow_count, yellow_filename = Calculation()
    for move1 in yellow_filename:
        if not os.path.exists('yellowTemp'):
            os.makedirs('yellowTemp')
        shutil.copy("scan/"+str(move1), "yellowTemp/")
    for delete1 in yellow_filename:
        if os.path.exists("scan/"+ delete1):
            os.remove("scan/"+ delete1)

    t1_start = process_time()
    chalkyDetection()
    chalky_count, chalky_name = chalkynames('chaly_temp')
    chalky_length, chalky_width = cal(chalky_name)
    for move12 in chalky_name:
        if not os.path.exists('chaly_temp3'):
            os.makedirs('chaly_temp3')
        shutil.copy("scan/"+str(move12), "chaly_temp3/")
    for delete12 in chalky_name:
        if os.path.exists("scan/"+ delete12):
            os.remove("scan/"+ delete12)
    #damage_count, damage_name, chalky_count, chalky_name = damage("scan/")
    new_damage1_count , new_damage1_name = new_damage2("scan/")
    
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     future = executor.submit(damage, "scan/")
    #     damage_count, damage_name, chalky_count, chalky_name = future.result()
    #     print("this is the total damage rice",damage_count)
        
    #threading.Thread(target=damage, args=("scan/",)).start()
    #damage_count, damage_name, chalky_count, chalky_name = damage_co, damage_na, chalky_co, chalky_na
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the ALL program in seconds:", 
                                         t1_stop-t1_start)
    t1_start = process_time()
    damage_length, damage_width = cal(new_damage1_name)
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the DAMAGE program in seconds:", 
                                         t1_stop-t1_start)
    t1_start = process_time()                                     
    # paddy_length, paddy_width = cal(paddy_name)
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the CHALKY program in seconds:", 
                                         t1_stop-t1_start)
    #pergrain("scan_copy","chaly_temp")
    
    return objects

def return_final_image():
    return orig


