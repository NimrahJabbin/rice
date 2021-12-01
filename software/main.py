# -*- coding: utf-8 -*-

#python version = 3.5.3

"""
Created on Fri Sep  7 05:16:18 2018

@author: Nimra
"""
## Importing Libraries


from __future__ import division
import webbrowser
from tkinter import filedialog
import shutil
from tkinter import *
from tkinter import StringVar
import tkinter.messagebox
from tkinter import ttk
from multiprocessing.pool import ThreadPool
import tkinter as tk
import threading
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import numpy as np
import os
import random
from win32com.client import Dispatch
#import analysis
import report
import reportnew
from win32api import GetSystemMetrics #to resize anything dynmaically by getting size of window
from win32gui import FindWindow, GetWindowRect
#import pygetwindow as gw\
import time
from PIL import ImageGrab


import sys
import datetime
import cv2
from PIL import Image, ImageTk, ImageEnhance

#Libraries for executable
import sklearn.utils._cython_blas
import sklearn.neighbors.typedefs
import sklearn.neighbors.quad_tree
import sklearn.tree
import sklearn.tree._utils

from time import process_time
from multiprocessing import Pool

import analysis_1121
import analysis_irri6
import analysis_brown
import analysis_pk386
import analysis_super_kernel_basmati_white
import analysis_super_kernel_basmati_brown
import analysis_1121_sela

#leena
import globals
from reportnew import nofile
Image_screen_width, Image_screen_height= GetSystemMetrics(0),GetSystemMetrics(1) #to get width and height of current screen
#global no_func
no_func=0
import sqlite3 #local database
import tempfile #to create file in temp folder

global viewSample_counter
viewSample_counter = 0
##


##########################################################
def create_grainPro_dir():
    global roaming_dir_path
    roaming_dir_path = '%s\\Grain Pro\\' %  os.environ['APPDATA'] 
    if not os.path.exists(roaming_dir_path):
        os.makedirs(roaming_dir_path)
    
###create directory inside roaming if not exists
create_grainPro_dir() 
global roaming_dir_path
db_file_path = '%sprofile.db' % roaming_dir_path
#https://www.tutorialspoint.com/sqlite/sqlite_python.htm
###creating sqlite database if not exist
conn = sqlite3.connect(db_file_path)
##dropQuery = "DROP TABLE IF EXISTS " + "profile_table";
##conn.execute(dropQuery)
conn.execute('''CREATE TABLE IF NOT EXISTS profile_table
         (TYPE_RICE        TEXT   NOT NULL,
         BROKEN           REAL   NOT NULL,
         LONG_BROKEN_MIN      REAL   NOT NULL,
         LONG_BROKEN_MAX      REAL   NOT NULL,
         MEDIUM_BROKEN_MIN    REAL   NOT NULL,
         MEDIUM_BROKEN_MAX    REAL   NOT NULL,
         SMALL_BROKEN_MIN     REAL   NOT NULL,
         SMALL_BROKEN_MAX     REAL   NOT NULL);''')

#temp_folder = tempfile.gettempdir() #current temporary directory path
#if the following file exists in roaming directory then don't insert
if not os.path.exists(roaming_dir_path+"\de99006f-f1fe-4cdc-8624-b2b86dc0159a.txt"):
    file = open(roaming_dir_path+"\de99006f-f1fe-4cdc-8624-b2b86dc0159a.txt", "w") 
    file.write("Hacked") 
    file.close()
    conn.execute("insert into profile_table(TYPE_RICE, BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX) values (?, ?, ?, ?, ?, ?, ?, ?) ",
                 ("irri-6",
                  globals.b1,
                  globals.l1_min,
                  globals.l1_max,
                  globals.m1_min,
                  globals.m1_max,
                  globals.s1_min,
                  globals.s1_max))
    conn.execute("insert into profile_table(TYPE_RICE, BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX) values (?, ?, ?, ?, ?, ?, ?, ?) ",
                 ("1121",
                  globals.b2,
                  globals.l2_min,
                  globals.l2_max,
                  globals.m2_min,
                  globals.m2_max,
                  globals.s2_min,
                  globals.s2_max))
    conn.execute("insert into profile_table(TYPE_RICE, BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX) values (?, ?, ?, ?, ?, ?, ?, ?) ",
                 ("pk386",
                  globals.b3,
                  globals.l3_min,
                  globals.l3_max,
                  globals.m3_min,
                  globals.m3_max,
                  globals.s3_min,
                  globals.s3_max))
    
    conn.execute("insert into profile_table(TYPE_RICE, BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX) values (?, ?, ?, ?, ?, ?, ?, ?) ",
                 ("brown",
                  globals.b4,
                  globals.l4_min,
                  globals.l4_max,
                  globals.m4_min,
                  globals.m4_max,
                  globals.s4_min,
                  globals.s4_max))
    
    conn.execute("insert into profile_table(TYPE_RICE, BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX) values (?, ?, ?, ?, ?, ?, ?, ?) ",
                 ("super kernel basmati white",
                  globals.b5,
                  globals.l5_min,
                  globals.l5_max,
                  globals.m5_min,
                  globals.m5_max,
                  globals.s5_min,
                  globals.s5_max))

    conn.execute("insert into profile_table(TYPE_RICE, BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX) values (?, ?, ?, ?, ?, ?, ?, ?) ",
                 ("super kernel basmati brown",
                  globals.b6,
                  globals.l6_min,
                  globals.l6_max,
                  globals.m6_min,
                  globals.m6_max,
                  globals.s6_min,
                  globals.s6_max))

    conn.execute("insert into profile_table(TYPE_RICE, BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX) values (?, ?, ?, ?, ?, ?, ?, ?) ",
                 ("1121 sela",
                  globals.b7,
                  globals.l7_min,
                  globals.l7_max,
                  globals.m7_min,
                  globals.m7_max,
                  globals.s7_min,
                  globals.s7_max))
    
    #conn.execute("INSERT INTO profile_table(TYPE_RICE, BROKEN, LONG_BROKEN, MEDIUM_BROKEN, SMALL_BROKEN) \
    #VALUES('irri-6',vall, 32, 4.3, 20 )");
    conn.commit()
    

global runflag
global type
runflag = 0

#color
mustard_color = "#F1C40F"
##font family
mfont_family = "Lucida Sans"


#reseting on startup

if os.path.exists("scan"):
    
    # Muzammil adding these lines for deleting our temp imgs
    shutil.rmtree("scan")

if os.path.exists("yellowTemp"):    
    shutil.rmtree("yellowTemp")

if os.path.exists("paddy"):    
    shutil.rmtree("paddy")

if os.path.exists("scan_copy"):    
    shutil.rmtree("scan_copy")

if os.path.exists("yellow"):    
    shutil.rmtree("yellow")
            
if os.path.exists("chaly_temp"):    
    shutil.rmtree("chaly_temp")
    
if os.path.exists("chaly_temp3"):    
    shutil.rmtree("chaly_temp3")

from datetime import datetime


app_date = datetime(year=2021, month=5, day=30)  # setup a datetime object
now = datetime.now()
print(now)
print("the", (now.year-app_date.year))
if (now - app_date).days >= 28000000 or (now.year-app_date.year) < 0 or (now.month-app_date.month) < 0:  # change to 30
    print("Your System Has been expired")
    #os.startfile("history.bat")
    #os.remove("paddy.h5")
    #os.remove("damage_3000img_final_.h5")
    #shutil.rmtree("img")
    #os.startfile("history.bat")
    sys.exit()
else:
    print("Success")


# Need current date here
#Checking if file exists

valid_d = os.path.exists('D:check.txt')
valid_e = os.path.exists('E:check.txt')
valid_f = os.path.exists('F:check.txt')
valid_i = os.path.exists('I:check.txt')
valid_h = os.path.exists('H:check.txt')
valid2 = os.path.exists('history.bat')


# ex = datetime.datetime.now()

# daye = 30
# me = 1
# ye = 2025
# day = int(ex.strftime("%d"))
# m = int(ex.strftime("%m"))
# y = int(ex.strftime("%Y"))

if valid2==True:
    print("Ready to execute")
else:
    print("bat missing error")
    sys.exit()

# if (y >= ye and m >= me and day >= daye):
#     os.startfile(r"history.bat")
#     print("history")
#     sys.exit("Softwere has been expired.")
# else:
#     print("Run succes")


# if valid_d==True or valid_e==True or valid_f==True or valid_i==True or valid_h==True:
#    print("Ready to execute")
# else:
#    print(".dll missing error")
#    sys.exit()


#########GUI Start
LARGE_FONT= ("Helvetica", 16)
style.use('ggplot')
# rice_image = cv2.imread('irri3.jpg')
objects = []

#-----------------------------------------------------------#
# Main Class Definition
# Main Class Definition
#-----------------------------------------------------------#

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs )
        
        tk.Tk.iconbitmap(self,default="img/icon1.ico")
        tk.Tk.wm_title(self, "National Grain Tech NGT")
 
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
         
        # create the menubar
        menubar = tk.Menu(container)
        tk.Tk.config(self, menu=menubar)
          
        #create the sub menu
        subMenu = tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="File", menu= subMenu)
        subMenu.add_command(label="New Sample", command=reset_button)
        
        #subMenu.add_command(label="Recent Files", command=reset_button)
        


        #leena
        def destroyAll():
            app.destroy()
            global no_func
            no_func=1
            reset_button()

        #menu element
        subMenu.add_command(label="Quit",command= destroyAll)
            
        ####

        #leena
        # create about us function for menubar
        def about_us():
            mainwindow = Tk()
            mainframe = Frame(mainwindow, bg="floral white")
            mainframe.pack(fill="both", expand=True)

##            label = Label(mainframe, text="About Grain Tech", bg='#336699', fg="white", padx=5, pady=5)
##            label.config(font=("Arial", 18))
##            label.pack(fill="x")

            im = Image.open("img/image1.png")
            resized = im.resize((120, 120), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(resized, master=mainframe)

            im1 = Image.open("img/image2.png")
            resized1 = im1.resize((120, 120), Image.ANTIALIAS)
            tkimage1 = ImageTk.PhotoImage(resized1, master=mainframe)

            im2 = Image.open("img/image3.png")
            resized2 = im2.resize((120, 120), Image.ANTIALIAS)
            tkimage2 = ImageTk.PhotoImage(resized2, master=mainframe)
            horizontal_frame = Frame(mainframe, bg='#336699')

            label1 = Label(horizontal_frame, image=tkimage, bg='#336699', padx=10, pady=10)
            # label1.image = tkimage
            label1.grid(row=0, column=0, padx=50, pady=5, sticky="nsew")
            label2 = Label(horizontal_frame, image=tkimage1, bg='#336699', padx=10, pady=10)
            # label2.image = tkimage1
            label2.grid(row=0, column=1, padx=90, pady=5, sticky="nsew")
            label3 = Label(horizontal_frame, image=tkimage2, bg='#336699', padx=10, pady=10)
            # label3.image = tkimage2
            label3.grid(row=0, column=2, padx=50, pady=5, sticky="nsew")

            horizontal_frame.grid_columnconfigure(0, weight=1)
            horizontal_frame.grid_columnconfigure(1, weight=1)
            horizontal_frame.grid_columnconfigure(2, weight=1)
            horizontal_frame.grid_columnconfigure(3, weight=1)
            horizontal_frame.pack(fill="x")

            # end horizontal

            # grid data
            label = Label(mainframe, text="Rice Quality Analyzer is an alternative solution for grain"
                                        " quality analysis. It can identify average length, average "
                                        "width, broken rice (%), the weight of the sample, whole grain,"
                                        " aspect ratio. These parameters will be able to facilitate the"
                                        " exporters in terms of money by improving Quality inspection and"
                                        " decreasing human error. Thus, it is time-saving, gives accuracy"
                                        " results up to 99%- and one-time investment leads to cost "
                                        "efficiency. This product can be used by exporters as it is a "
                                        "very fast and inexpensive process as compared to the manual one."
                                        " Further, it is going to increase the exports of Pakistan by "
                                        "minimizing human errors and increasing efficiency.",
                        bg='#336699', wraplength=600, padx=5, pady=5, justify=CENTER,fg="white")
            label.config(font=("Arial", 11))
            label.pack(fill="x")

            horizontal_frame = Frame(mainframe, bg='floral white')

            def callback_website(url):
                webbrowser.open_new(url)

            label2 = Label(horizontal_frame, text="CONTACT INFORMATION",
                        font=('Berlin Sans FB', 16, 'underline', 'bold'), bg='floral white')
            label2.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

            imm7 = Image.open("img/icon_loc.png")
            #resizeddd7 = imm7.resize((50, 50), Image.ANTIALIAS)
            tkimageee7 = ImageTk.PhotoImage(imm7, master=horizontal_frame)
            #labell8 = Label(horizontal_frame, image=tkimageee7, padx=0, pady=0)
            #labell8.place(relx=0.08,rely=0.3, anchor="center")
            #labell8.grid(row=1, column=0, padx=0, pady=10, sticky="nsew")

##            "\n Email: ahsan191@hotmail.com \n"
##                                    "\n Website : http://grainscan.rcai.pk/ \n"
##                                    "\n Contact No: +92 331 8859953 \n"
                                    
            label1 = Label(horizontal_frame, image=tkimageee7, compound="left", text="   University Road, Gulshan-e-Iqbal Block 6, Karachi"                                                          
                                    , bg="floral white", padx=0, pady=0, wraplength=350, justify="center",
            font=("Arial", 12))

            label1.grid(row=1, column=0, padx=10, pady=0, sticky="nw")

        #############
            imm6 = Image.open("img/icon_mail.png")
            #resizeddd6 = imm6.resize((50, 50), Image.ANTIALIAS)
            tkimageee6 = ImageTk.PhotoImage(imm6, master=horizontal_frame)
            
            label122 = Label(horizontal_frame, image=tkimageee6, compound="left", text="   ahsan191@hotmail.com"                                                          
                                    , bg="floral white", padx=0, pady=0,
            font=("Arial", 12))

            label122.grid(row=1, column=0, padx=10, pady=60, sticky="nw")

            imm5 = Image.open("img/icon_web.png")
            #resizeddd5 = imm5.resize((50, 50), Image.ANTIALIAS)
            tkimageee5 = ImageTk.PhotoImage(imm5, master=horizontal_frame)
            
            label132 = Label(horizontal_frame, image=tkimageee5, compound="left", text="    http://grainscan.rcai.pk/"                                                          
                                    , bg="floral white", padx=0, pady=0,fg="blue", font=("Arial", 12), cursor="hand2")

            label132.grid(row=1, column=0, padx=10, pady=120, sticky="nw")

            label132.bind("<Button-1>", lambda e: callback_website("https://graintech.com.pk/"))

            imm4 = Image.open("img/icon_phone.png")
            #resizeddd4 = imm4.resize((50, 50), Image.ANTIALIAS)
            tkimageee4 = ImageTk.PhotoImage(imm4, master=horizontal_frame)

            label142 = Label(horizontal_frame, image=tkimageee4, compound="left", text="   +92 331 8859953"                                                          
                                    , bg="floral white", padx=0, pady=0,
            font=("Arial", 12))

            label142.grid(row=1, column=0, padx=10, pady=180, sticky="nw")

            
            horizontal_frame.grid_columnconfigure(0, weight=1)
            horizontal_frame.grid_columnconfigure(1, weight=1)
            horizontal_frame.grid_columnconfigure(0, weight=1)
            horizontal_frame.grid_columnconfigure(1, weight=1)
            horizontal_frame.grid_columnconfigure(0, weight=1)

            label3 = Label(horizontal_frame, text="CORE VALUES",
                        font=('Berlin Sans FB', 16, 'underline', 'bold'), bg='floral white', padx=0, pady=0)
            label3.grid(row=0, column=1, padx=10, pady=0, sticky="nsew")

            im4 = Image.open("img/image6.png")
            resized4 = im4.resize((120, 120), Image.ANTIALIAS)
            tkimage4 = ImageTk.PhotoImage(resized4, master=mainframe)

            im5 = Image.open("img/image9.png")
            resized5 = im5.resize((120, 120), Image.ANTIALIAS)
            tkimage5 = ImageTk.PhotoImage(resized5, master=mainframe)

            im6 = Image.open("img/image11.png")
            resized6 = im6.resize((120, 120), Image.ANTIALIAS)
            tkimage6 = ImageTk.PhotoImage(resized6, master=mainframe)

            im7 = Image.open("img/image13.png")
            resized7 = im7.resize((120, 120), Image.ANTIALIAS)
            tkimage7 = ImageTk.PhotoImage(resized7, master=mainframe)
            label8 = Label(horizontal_frame, image=tkimage4, bg='floral white', padx=0, pady=0, text="Ethics",
                        compound='top', font=('Berlin Sans FB', 12, 'bold'))
            label8.grid(row=1, column=1, padx=20, pady=0, sticky="ne")
            label9 = Label(horizontal_frame, image=tkimage5, bg='floral white', padx=0, pady=0, text="Trust",
                        compound='top', font=('Berlin Sans FB', 12, 'bold'))
            label9.grid(row=1, column=2, padx=40, pady=0, sticky="ne")
            label10 = Label(horizontal_frame, image=tkimage6, bg='floral white', padx=0, pady=0, text="Customer Satisfaction",
                            compound='top', font=('Berlin Sans FB', 12, 'bold'))
            label10.grid(row=1, column=1, padx=0, pady=120, sticky="ne")
            label11 = Label(horizontal_frame, image=tkimage7, bg='floral white', padx=0, pady=0, text="Goals",
                            compound='top', font=('Berlin Sans FB', 12, 'bold'))
            label11.grid(row=1, column=2, padx=40, pady=120, sticky="ne")
            label8.grid_columnconfigure(1, weight=1)
            label9.grid_columnconfigure(2, weight=1)
            label10.grid_columnconfigure(1, weight=1)
            label11.grid_columnconfigure(2, weight=1)
            horizontal_frame.pack(fill="x")


            mainwindow.resizable(0, 0)
            mainwindow.title("About Us")
            mainwindow.mainloop()

        ###############

            

        #create the sub menu
        subMenuu = tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Edit", menu= subMenuu)
        subMenuu.add_command(label="Profile", command=profile_edit)        
        #profiling end here


        #leena
        def instructions():
            
            instruction_root = tk.Tk()
            #instruction_root.resizable(0,0)
            instruction_root.state('zoomed')
            instruction_root.title("Instructions")
            instruction_root.columnconfigure(0, weight=1)
            instruction_root.rowconfigure(0, weight=1)
            self.screen_width = instruction_root.winfo_screenwidth() - 100
            self.screen_width1 = int(instruction_root.winfo_screenwidth() /2)
            self.screen_height = instruction_root.winfo_screenheight() - 200

            

##            thisdict = {
##            "brand1": ["Click on 0g Grain Test","img/1.png"],
##            "brand2": ["Click on 30g Grain Test","img/1.png"],
##            "brand3": ["Click on 200g Grain Test","img/1.png"] }

##            for key, values in thisdict:
##                print(key)
##            self.mainframe = Frame(instruction_root, bg='floral white')
##            self.mainframe.pack(fill="both", expand=True)
##            label = Label(self.mainframe, text="Click on 0g Grain Test", font=28
##                        , bg='floral white', padx=5, pady=5, fg='#336699')
##            label.config(font=("Arial", 18))
##            label.pack(fill="x")
##
##            im = Image.open("img/1.png")
##            resized = im.resize((self.screen_width, self.screen_height), Image.ANTIALIAS)
##            tkimage = ImageTk.PhotoImage(resized, master=instruction_root)
##
##            horizontal_frame = Frame(self.mainframe, bg='floral white')
##            
##
##            label1 = Label(horizontal_frame, image=tkimage, bg='floral white', padx=10, pady=10)
##            label1.image = tkimage
##            label1.grid(row=0, column=0, sticky="nsew")
##
##            horizontal_frame.grid_columnconfigure(0, weight=1)
##            horizontal_frame.grid_columnconfigure(1, weight=1)
##            horizontal_frame.grid_columnconfigure(2, weight=1)
##            horizontal_frame.grid_columnconfigure(3, weight=1)
##
##            horizontal_frame.pack(fill="x")
##
##            horizontal_frame1 = Frame(self.mainframe, bg='floral white')
##            l = Label(horizontal_frame1, bg='floral white')
##            l.grid(row=1, column=0)
##            next_1 = Button(horizontal_frame1, text="NEXT", width=12, height=2, bd=5,
##                            highlightcolor='grey48',
##                            relief=RIDGE)
##            next_1.grid(row=2, column=0, padx=200)
##
##            cancel_button = Button(horizontal_frame1, text="CANCEL", width=12,  height=2, bd=5,
##                            highlightcolor='grey48',
##                            relief=RIDGE)
##            cancel_button.grid(row=2, column=1, padx=100)
##            horizontal_frame1.grid_columnconfigure(0, weight=1)
##            horizontal_frame1.grid_columnconfigure(1, weight=1)
##            horizontal_frame1.grid_columnconfigure(1, weight=1)
##            horizontal_frame1.grid_rowconfigure(1, weight=1)
##            horizontal_frame1.grid_rowconfigure(1, weight=1)
##            horizontal_frame1.grid_rowconfigure(1, weight=1)
##
##            horizontal_frame1.pack(fill='x')
                
            
            def slideshow():

                
                self.mainframe = Frame(instruction_root, bg='floral white')
                self.mainframe.grid(row=0,column=0, sticky="nsew")

                background_image(self.mainframe)
                
                label = Label(self.mainframe, text="Click on 10g Grain Test", font=28
                            , bg='floral white', padx=5, pady=5, fg='#336699')
                label.config(font=("Arial", 18))
                #label.grid(row=1, column=1, sticky="nsew")
                label.place(relx=.11,rely=.45, anchor="center")
                #label.pack(fill="x")

                im = Image.open("img/1.png")
                
                resized = im.resize((int(self.screen_width/1.7),int(self.screen_height)), Image.ANTIALIAS)#1.7
                ##resized = im.resize((int(500),int(300)), Image.ANTIALIAS)
                tkimage = ImageTk.PhotoImage(resized, master=instruction_root)

##                horizontal_frame = Frame(self.mainframe, bg='floral white')
                

                label1 = Label(self.mainframe, image=tkimage, bg='floral white', pady=10)
                label1.image = tkimage
                label1.place(relx=.7,rely=.45, anchor="center")
                #label1.grid(row=1, column=2, sticky="nsew",pady=30)

##                horizontal_frame.grid_columnconfigure(0, weight=1)
##                horizontal_frame.grid_columnconfigure(1, weight=1)
##                horizontal_frame.grid_columnconfigure(2, weight=1)
##                horizontal_frame.grid_columnconfigure(3, weight=1)
##
##                ##horizontal_frame.pack(fill="x")
##                horizontal_frame.grid(row=1,column=2)

                horizontal_frame1 = self.mainframe
##                horizontal_frame1 = Frame(self.mainframe, bg='floral white')
                l = Label(horizontal_frame1, bg='floral white')
                l.grid(row=1, column=0)
                next_1 = Button(horizontal_frame1, text="NEXT", command=slideshow1, width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                next_1.place(relx=.65,rely=.93, anchor="center")
                ##next_1.grid(row=2, column=0, padx=300,sticky="n")

                cancel_button = Button(horizontal_frame1, text="CANCEL", width=20, command=cancel, height=2, bd=2, bg= "#aaadaa", fg="black",
                            highlightcolor='grey48',
                            relief=GROOVE)
                cancel_button.place(relx=.25,rely=.93, anchor="center")
                ##cancel_button.grid(row=2, column=1, padx=200, sticky="s")
##                horizontal_frame1.grid_columnconfigure(0, weight=1)
##                horizontal_frame1.grid_columnconfigure(1, weight=1)
##                horizontal_frame1.grid_columnconfigure(1, weight=1)
##                horizontal_frame1.grid_rowconfigure(1, weight=1)
##                horizontal_frame1.grid_rowconfigure(1, weight=1)
##                horizontal_frame1.grid_rowconfigure(1, weight=1)
##
##                ##horizontal_frame1.pack(fill='x')
##                horizontal_frame1.grid(row=2,column=1)

            def slideshow1():
            
                if self.mainframe is not None:
                    self.mainframe.destroy()
                    self.mainframe1 = Frame(instruction_root, bg='#336699')
                    self.mainframe1.pack(fill="both", expand=True)

                background_image(self.mainframe1)

                label = Label(self.mainframe1, text=" Select AGL or no AGL." +
                                                    "\n" + "Option1: Insert the number in mm for broken size."
                                                        "\nOption2: Insert the number in % for broken size,if you have AGL "
                                                        "then click on button 'submit'."
                            , bg='floral white', pady=5, fg='#336699' , wraplength=400, justify="left")
                label.config(font=("Arial", 16))
                label.place(relx=.15,rely=.45, anchor="center")

                im = Image.open("img/2.png")
                resized = im.resize((int(self.screen_width/1.7),int(self.screen_height)), Image.ANTIALIAS)
                tkimage = ImageTk.PhotoImage(resized, master=instruction_root)

    
                label1 = Label(self.mainframe1, image=tkimage, bg='floral white', pady=10)
                label1.image = tkimage
                label1.place(relx=.7,rely=.45, anchor="center")

                    
                next_1 = Button(self.mainframe1, text="NEXT", command=slideshow2, width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                next_1.place(relx=.65,rely=.93, anchor="center")

                back = Button(self.mainframe1, text="BACK", command=canv1_destroy,  width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                
                back.place(relx=.45,rely=.93, anchor="center")

                cancel_button = Button(self.mainframe1, text="CANCEL", width=20, command=cancel, height=2, bd=2, bg= "#aaadaa", fg="black",
                            highlightcolor='grey48',
                            relief=GROOVE)
                cancel_button.place(relx=.25,rely=.93, anchor="center")

            def slideshow2():
                if self.mainframe1 is not None:
                    self.mainframe.destroy()
                    self.mainframe1.destroy()
                    self.mainframe2 = Frame(instruction_root, bg='floral white')
                    self.mainframe2.pack(fill="both", expand=True)

                background_image(self.mainframe2)
                label = Label(self.mainframe2,
                            text="If you already have image of sample then click on button 'Browse Image'. or" +
                                "\n" + " If you do not have image of sample then click 'Scan Image'."
                            , bg='floral white', pady=5, fg='#336699' , wraplength=400, justify="left")
                label.config(font=("Arial", 17))
                label.place(relx=.15,rely=.45, anchor="center")

                im = Image.open("img/3.png")
                resized = im.resize((int(self.screen_width/1.7),int(self.screen_height)), Image.ANTIALIAS) 
                tkimage = ImageTk.PhotoImage(resized, master=self.mainframe2)


                label1 = Label(self.mainframe2, image=tkimage, bg='floral white', padx=10, pady=10)
                label1.image = tkimage
                label1.place(relx=.7,rely=.45, anchor="center")

                next_1 = Button(self.mainframe2, text="NEXT", command=slideshow3, width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                next_1.place(relx=.65,rely=.93, anchor="center")

                back = Button(self.mainframe2, text="BACK", command=canv2_destroy,  width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                
                back.place(relx=.45,rely=.93, anchor="center")

                cancel_button = Button(self.mainframe2, text="CANCEL", width=20, command=cancel, height=2, bd=2, bg= "#aaadaa", fg="black",
                            highlightcolor='grey48',
                            relief=GROOVE)
                cancel_button.place(relx=.25,rely=.93, anchor="center")


            def slideshow3():
                if self.mainframe2 is not None:
                    self.mainframe.destroy()
                    self.mainframe1.destroy()
                    self.mainframe2.destroy()
                    self.mainframe3 = Frame(instruction_root, bg='floral white')
                    self.mainframe3.pack(fill="both", expand=True)

                background_image(self.mainframe3)
                label = Label(self.mainframe3, text="Click on ok button and it will take one minute to process your sample."
                           , bg='floral white', pady=5, fg='#336699' , wraplength=400, justify="left")
                label.config(font=("Arial", 18))
                label.place(relx=.15,rely=.45, anchor="center")

                im = Image.open("img/4.png")
                resized = im.resize((int(self.screen_width/1.7),int(self.screen_height)), Image.ANTIALIAS)
                tkimage = ImageTk.PhotoImage(resized, master=self.mainframe3)


                label1 = Label(self.mainframe3, image=tkimage, bg='floral white', padx=10, pady=10)
                label1.image = tkimage
                label1.place(relx=.7,rely=.45, anchor="center")

                next_1 = Button(self.mainframe3, text="NEXT", command=slideshow4, width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                next_1.place(relx=.65,rely=.93, anchor="center")

                back = Button(self.mainframe3, text="BACK", command=canv3_destroy,  width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                
                back.place(relx=.45,rely=.93, anchor="center")

                cancel_button = Button(self.mainframe3, text="CANCEL", width=20, command=cancel, height=2, bd=2, bg= "#aaadaa", fg="black",
                            highlightcolor='grey48',
                            relief=GROOVE)
                cancel_button.place(relx=.25,rely=.93, anchor="center")



            def slideshow4():
                if self.mainframe3 is not None:
                    self.mainframe.destroy()
                    self.mainframe1.destroy()
                    self.mainframe2.destroy()
                    self.mainframe3.destroy()
                    self.mainframe4 = Frame(instruction_root, bg='floral white')
                    self.mainframe4.pack(fill="both", expand=True)

                background_image(self.mainframe4)
                label = Label(self.mainframe4, text="After the scanning, Click on the button 'View Sample'.",
                                 bg='floral white', pady=5, fg='#336699' , wraplength=400, justify="left")
                label.config(font=("Arial", 18))
                label.place(relx=.15,rely=.45, anchor="center")

                im = Image.open("img/5.png")
                resized = im.resize((int(self.screen_width/1.7),int(self.screen_height)), Image.ANTIALIAS)
                tkimage = ImageTk.PhotoImage(resized, master=self.mainframe4)


                label1 = Label(self.mainframe4, image=tkimage, bg='floral white', padx=10, pady=10)
                label1.image = tkimage
                label1.place(relx=.7,rely=.45, anchor="center")

                next_1 = Button(self.mainframe4, text="NEXT", command=slideshow5, width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                next_1.place(relx=.65,rely=.93, anchor="center")

                back = Button(self.mainframe4, text="BACK", command=canv4_destroy,  width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                
                back.place(relx=.45,rely=.93, anchor="center")

                cancel_button = Button(self.mainframe4, text="CANCEL", width=20, command=cancel, height=2, bd=2, bg= "#aaadaa", fg="black",
                            highlightcolor='grey48',
                            relief=GROOVE)
                cancel_button.place(relx=.25,rely=.93, anchor="center")

            def slideshow5():
                if self.mainframe4 is not None:
                    self.mainframe.destroy()
                    self.mainframe1.destroy()
                    self.mainframe2.destroy()
                    self.mainframe3.destroy()
                    self.mainframe4.destroy()
                    self.mainframe5 = Frame(instruction_root, bg='floral white')
                    self.mainframe5.pack(fill="both", expand=True)

                background_image(self.mainframe5)   
                label = Label(self.mainframe5, text="You can view your sample like this"
                            , bg='floral white', pady=5, fg='#336699' , wraplength=400, justify="left")
                label.config(font=("Arial", 18))
                label.place(relx=.15,rely=.45, anchor="center")

##                im = Image.open("img/6.png")
##                resized = im.resize((self.screen_width1, self.screen_height), Image.ANTIALIAS)
##                tkimage = ImageTk.PhotoImage(resized, master=self.mainframe5)

                im1 = Image.open("img/7.png")
                resized1 = im1.resize((int(self.screen_width/1.7),int(self.screen_height)), Image.ANTIALIAS)
                tkimage1 = ImageTk.PhotoImage(resized1, master=self.mainframe5)

##                horizontal_frame = Frame(self.mainframe5, bg='floral white')

##                label1 = Label(horizontal_frame, image=tkimage, bg='floral white', padx=10, pady=10)
##                label1.image = tkimage
##                label1.grid(row=0, column=0, sticky="nsew")
                label2 = Label(self.mainframe5, image=tkimage1, bg='floral white', padx=10, pady=10)
                label2.image = tkimage1
                label2.place(relx=.7,rely=.45, anchor="center")

                next_1 = Button(self.mainframe5, text="NEXT", command=slideshow6, width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                next_1.place(relx=.65,rely=.93, anchor="center")

                back = Button(self.mainframe5, text="BACK", command=canv5_destroy,  width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                
                back.place(relx=.45,rely=.93, anchor="center")

                cancel_button = Button(self.mainframe5, text="CANCEL", width=20, command=cancel, height=2, bd=2, bg= "#aaadaa", fg="black",
                            highlightcolor='grey48',
                            relief=GROOVE)
                cancel_button.place(relx=.25,rely=.93, anchor="center")


            def slideshow6():
                if self.mainframe5 is not None:
                    self.mainframe.destroy()
                    self.mainframe1.destroy()
                    self.mainframe2.destroy()
                    self.mainframe3.destroy()
                    self.mainframe4.destroy()
                    self.mainframe5.destroy()
                    self.mainframe6 = Frame(instruction_root, bg='floral white')
                    self.mainframe6.pack(fill="both", expand=True)
                background_image(self.mainframe6)   
                label = Label(self.mainframe6, text="Click on button 'Summarized Report' for viewing the "
                                                    "summarized report of rice ", 
                                                    bg='floral white', pady=5, fg='#336699' , wraplength=400, justify="left")
                label.config(font=("Arial", 18))
                label.place(relx=.15,rely=.45, anchor="center")

                # im = Image.open("img/8.png")
                # resized = im.resize((self.screen_width1, self.screen_height), Image.ANTIALIAS)
                # tkimage = ImageTk.PhotoImage(resized, master=self.mainframe6)

                im1 = Image.open("img/9.png")
                resized1 = im1.resize((self.screen_width1, self.screen_height), Image.ANTIALIAS)
                tkimage1 = ImageTk.PhotoImage(resized1, master=self.mainframe6)

                # label1 = Label(self.mainframe6, image=tkimage, bg='floral white', padx=10, pady=10)
                # label1.image = tkimage
                # label1.grid(row=0, column=0, sticky="nsew")
                label2 = Label(self.mainframe6, image=tkimage1, bg='floral white', padx=10, pady=10)
                label2.image = tkimage1
                label2.place(relx=.7,rely=.45, anchor="center")


                next_1 = Button(self.mainframe6, text="NEXT", command=slideshow7, width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                next_1.place(relx=.65,rely=.93, anchor="center")

                back = Button(self.mainframe6, text="BACK", command=canv6_destroy,  width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                
                back.place(relx=.45,rely=.93, anchor="center")

                cancel_button = Button(self.mainframe6, text="CANCEL", width=20, command=cancel, height=2, bd=2, bg= "#aaadaa", fg="black",
                            highlightcolor='grey48',
                            relief=GROOVE)
                cancel_button.place(relx=.25,rely=.93, anchor="center")


            def slideshow7():
                if self.mainframe6 is not None:
                    self.mainframe.destroy()
                    self.mainframe1.destroy()
                    self.mainframe2.destroy()
                    self.mainframe3.destroy()
                    self.mainframe4.destroy()
                    self.mainframe5.destroy()
                    self.mainframe6.destroy()
                    self.mainframe7 = Frame(instruction_root, bg='floral white')
                    self.mainframe7.pack(fill="both", expand=True)
                background_image(self.mainframe7)   
                label = Label(self.mainframe7, text="Click on button 'Detailed Report' for viewing the "
                                                    "detail report of rice .",
                                                     bg='floral white', pady=5, fg='#336699' , wraplength=400, justify="left")
                label.config(font=("Arial", 18))
                label.place(relx=.15,rely=.45, anchor="center")

                # im = Image.open("img/10.png")
                # resized = im.resize((self.screen_width1, self.screen_height), Image.ANTIALIAS)
                # tkimage = ImageTk.PhotoImage(resized, master=self.mainframe7)

                im1 = Image.open("img/11.png")
                resized1 = im1.resize((self.screen_width1, self.screen_height), Image.ANTIALIAS)
                tkimage1 = ImageTk.PhotoImage(resized1, master=self.mainframe7)


                # label1 = Label(horizontal_frame, image=tkimage, bg='floral white', padx=10, pady=10)
                # label1.image = tkimage
                # label1.grid(row=0, column=0, sticky="nsew")

                label2 = Label(self.mainframe7, image=tkimage1, bg='floral white', padx=10, pady=10)
                label2.image = tkimage1
                label2.place(relx=.7,rely=.45, anchor="center")


                next_1 = Button(self.mainframe7, text="NEXT", command=slideshow8, width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                next_1.place(relx=.65,rely=.93, anchor="center")

                back = Button(self.mainframe7, text="BACK", command=canv7_destroy,  width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                
                back.place(relx=.45,rely=.93, anchor="center")

                cancel_button = Button(self.mainframe7, text="CANCEL", width=20, command=cancel, height=2, bd=2, bg= "#aaadaa", fg="black",
                            highlightcolor='grey48',
                            relief=GROOVE)
                cancel_button.place(relx=.25,rely=.93, anchor="center")

            def slideshow8():
                if self.mainframe7 is not None:
                    self.mainframe.destroy()
                    self.mainframe1.destroy()
                    self.mainframe2.destroy()
                    self.mainframe3.destroy()
                    self.mainframe4.destroy()
                    self.mainframe5.destroy()
                    self.mainframe6.destroy()
                    self.mainframe7.destroy()
                    self.mainframe8 = Frame(instruction_root, bg='floral white')
                    self.mainframe8.pack(fill="both", expand=True)
                
                background_image(self.mainframe8)   
                im = Image.open("img/12.png")
                resized = im.resize((self.screen_width1, self.screen_height), Image.ANTIALIAS)
                tkimage = ImageTk.PhotoImage(resized, master=self.mainframe8)

                label = Label(self.mainframe8, text="Click on button 'Display Button' for viewing every grain of rice.",
                                                     bg='floral white', pady=5, fg='#336699' , wraplength=400, justify="left")
                label.config(font=("Arial", 18))
                label.place(relx=.15,rely=.45, anchor="center")

                # im1 = Image.open("img/13.png")
                # resized1 = im1.resize((self.screen_width1, self.screen_height), Image.ANTIALIAS)
                # tkimage1 = ImageTk.PhotoImage(resized1, master=self.mainframe8)

                label1 = Label(self.mainframe8, image=tkimage, bg='floral white', padx=10, pady=10)
                label1.image = tkimage
                label1.place(relx=.7,rely=.45, anchor="center")

                # label2 = Label(horizontal_frame, image=tkimage1, bg='floral white', padx=10, pady=10,
                #             text="Click on 'ALL' for viewing all the grain of rice and same as for yellow,damage and chalky"
                #             , font=("Arial", 15), compound=BOTTOM, fg='#336699')
                # label2.image = tkimage1
                

                next_1 = Button(self.mainframe8, text="NEXT", command=slideshow9, width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                next_1.place(relx=.65,rely=.93, anchor="center")

                back = Button(self.mainframe8, text="BACK", command=canv8_destroy,  width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                
                back.place(relx=.45,rely=.93, anchor="center")

                cancel_button = Button(self.mainframe8, text="CANCEL", width=20, command=cancel, height=2, bd=2, bg= "#aaadaa", fg="black",
                            highlightcolor='grey48',
                            relief=GROOVE)
                cancel_button.place(relx=.25,rely=.93, anchor="center")


            def slideshow9():
                if self.mainframe8 is not None:
                    self.mainframe.destroy()
                    self.mainframe1.destroy()
                    self.mainframe2.destroy()
                    self.mainframe3.destroy()
                    self.mainframe4.destroy()
                    self.mainframe5.destroy()
                    self.mainframe6.destroy()
                    self.mainframe7.destroy()
                    self.mainframe8.destroy()
                    self.mainframe9 = Frame(instruction_root, bg='floral white')
                    self.mainframe9.pack(fill="both", expand=True)

                background_image(self.mainframe9)   
                # im = Image.open("img/14.png")
                # resized = im.resize((self.screen_width1, self.screen_height), Image.ANTIALIAS)
                # tkimage = ImageTk.PhotoImage(resized, master=self.mainframe9)

                im1 = Image.open("img/15.png")
                resized1 = im1.resize((self.screen_width1, self.screen_height), Image.ANTIALIAS)
                tkimage1 = ImageTk.PhotoImage(resized1, master=self.mainframe9)

                label1 = Label(self.mainframe9,
                            text="Click on button 'Reset' after finishing your work.",
                            font=("Arial", 18), bg='floral white', pady=5, fg='#336699' , wraplength=400, justify="left")
                label1.place(relx=.15,rely=.45, anchor="center")
                
                label2 = Label(self.mainframe9, image=tkimage1, bg='floral white', padx=10, pady=10,
                             font=("Arial", 18), fg='white')
                label2.image = tkimage1
                label2.place(relx=.7,rely=.45, anchor="center")


                back = Button(self.mainframe9, text="BACK", command=canv9_destroy,  width=20, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE)
                
                back.place(relx=.45,rely=.93, anchor="center")

                cancel_button = Button(self.mainframe9, text="CANCEL", width=20, command=cancel, height=2, bd=2, bg= "#aaadaa", fg="black",
                            highlightcolor='grey48',
                            relief=GROOVE)
                cancel_button.place(relx=.25,rely=.93, anchor="center")


            

            def canv1_destroy():
                self.mainframe1.destroy()
                slideshow()

            def canv2_destroy():
                self.mainframe2.destroy()
                slideshow1()

            def canv3_destroy():
                self.mainframe3.destroy()
                slideshow2()

            def canv4_destroy():
                self.mainframe4.destroy()
                slideshow3()

            def canv5_destroy():
                self.mainframe5.destroy()
                slideshow4()

            def canv6_destroy():
                self.mainframe6.destroy()
                slideshow5()

            def canv7_destroy():
                self.mainframe7.destroy()
                slideshow6()

            def canv8_destroy():
                self.mainframe8.destroy()
                slideshow7()

            def canv9_destroy():
                self.mainframe9.destroy()
                slideshow8()


            def cancel():
                instruction_root.destroy()


            slideshow()
            instruction_root.mainloop()
            
        ##########################################  
          
        subMenu= tk.Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Help", menu= subMenu)
        
        #leena
        subMenu.add_command(label="Instructions",command=instructions)
        ###
        
        subMenu.add_command(label="About Us",command=about_us)
         

 
        self.frames = {}
        
        #Creating Frames

        for F in (Home, Sample, PieChart, LGraph, CGraph, TGraph): #leena added PieChart

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        frame.updateFrame()



##############################################################
# View Report function
##############################################################

def pdf1_view():
    #leena
    #globals.no_value_selected is 3 or
    if  globals.no_user_input is 3 or globals.browse_image is 3:
        #globals.no_type_selected=0
        globals.no_value_selected=0
        globals.no_user_input=0
        globals.browse_image=0 
       
    #from report import no_type_selected,no_value_selected,no_user_input
    #print(str(no_type_selected))
    #globals.no_value_selected is 0 or 
    if globals.no_user_input is 0 or  globals.browse_image is 0:
        tkinter.messagebox.showerror(title='Detailed Report Fail',message='No Report is generated')
    ####
    else:
        webbrowser.open_new(globals.D_Report)
        statusbar['text'] ="Detailed Report"

##############################################################
# View Report function
##############################################################

#########profile function starts here#################
#leena
def profile_edit():
    if os.path.exists(roaming_dir_path+"\de99006f-f1fe-4cdc-8624-b2b86dc0159a.txt"):
        cursor = conn.execute("SELECT BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX from profile_table where TYPE_RICE ='irri-6'")
        for row in cursor:
               globals.b1 = row[0]
               globals.l1_min = row[1]
               globals.l1_max = row[2]
               globals.m1_min = row[3]
               globals.m1_max = row[4]
               globals.s1_min = row[5]
               globals.s1_max = row[6]

        cursor = conn.execute("SELECT BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX from profile_table where TYPE_RICE ='1121'")
        for row in cursor:
               globals.b2 = row[0]
               globals.l2_min = row[1]
               globals.l2_max = row[2]
               globals.m2_min = row[3]
               globals.m2_max = row[4]
               globals.s2_min = row[5]
               globals.s2_max = row[6]


        cursor = conn.execute("SELECT BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX from profile_table where TYPE_RICE ='pk386'")
        for row in cursor:
               globals.b3 = row[0]
               globals.l3_min = row[1]
               globals.l3_max = row[2]
               globals.m3_min = row[3]
               globals.m3_max = row[4]
               globals.s3_min = row[5]
               globals.s3_max = row[6]

        cursor = conn.execute("SELECT BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX from profile_table where TYPE_RICE ='brown'")
        for row in cursor:
               globals.b4 = row[0]
               globals.l4_min = row[1]
               globals.l4_max = row[2]
               globals.m4_min = row[3]
               globals.m4_max = row[4]
               globals.s4_min = row[5]
               globals.s4_max = row[6]


        cursor = conn.execute("SELECT BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX from profile_table where TYPE_RICE ='super kernel basmati white'")
        for row in cursor:
               globals.b5 = row[0]
               globals.l5_min = row[1]
               globals.l5_max = row[2]
               globals.m5_min = row[3]
               globals.m5_max = row[4]
               globals.s5_min = row[5]
               globals.s5_max = row[6]

        cursor = conn.execute("SELECT BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX from profile_table where TYPE_RICE ='super kernel basmati brown'")
        for row in cursor:
               globals.b6 = row[0]
               globals.l6_min = row[1]
               globals.l6_max = row[2]
               globals.m6_min = row[3]
               globals.m6_max = row[4]
               globals.s6_min = row[5]
               globals.s6_max = row[6]


        cursor = conn.execute("SELECT BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX from profile_table where TYPE_RICE ='1121 sela'")
        for row in cursor:
               globals.b7 = row[0]
               globals.l7_min = row[1]
               globals.l7_max = row[2]
               globals.m7_min = row[3]
               globals.m7_max = row[4]
               globals.s7_min = row[5]
               globals.s7_max = row[6]

    ##for irri-6
##            globals.b1=0.4
##            globals.l1=0.4
##            globals.m1=0.4
##            globals.s1=0.4

    #for 1121
##            globals.b2=0.8
##            globals.l2=0.8
##            globals.m2=0.8
##            globals.s2=0.8
##
##            #for pk3
##            globals.b3=0.1
##            globals.l3=0.1
##            globals.m3=0.1
##            globals.s3=0.1

    profile_form_root = tk.Tk()
    profile_form_root.resizable(0, 0)
    #import datetime

    def profile_form_user(root):
        
        x = datetime.now()
        print(x.strftime("%A"))
        window = profile_form_root
        window.title("Profile")
        window.configure(background="floral white") 
        window.geometry('600x520')

        background_image(window)

        
        ##############create box#####
##                canvas = Canvas(self.window, width=480, height=430, bg='#fff')
##                #canvas.grid(column=0, row=3, columnspan=3)
##                canvas.place(x=60, y=10)
####                x1 = 200
####                y1 = 0
####                x2 = 250
####                y2 = 200
####                canvas.create_rectangle(x1, y1, x2, y2, fill="#fff",outline='#fff')
        
        title_lbl = Label(window, text="Choose Your Rice Type", bg ="floral white", fg='#336699', font=("Helvetica", 28))
        #title_lbl.grid(row=0, column=0, sticky="nw")
        title_lbl.place(x=90, y=10)
        #self.window.wm_attributes('-transparentcolor','#F1C40F')

        def window_close():
            window.destroy()
        
        def on_option_change(event):
        
            #if irri-6 is selected
            if clickednew.get() == "irri-6":
                entry_p_broken_rice.config(state=NORMAL)
                entry_p_broken_rice.delete(0, 'end')
                entry_p_broken_rice.insert(0,globals.b1)
                entry_p_broken_rice.config(state=DISABLED)
                
                entry_longBrokenMin.config(state=NORMAL)
                entry_longBrokenMin.delete(0, 'end')
                entry_longBrokenMin.insert(0,globals.l1_min)
                entry_longBrokenMin.config(state=DISABLED)

                entry_longBrokenMax.config(state=NORMAL)
                entry_longBrokenMax.delete(0, 'end')
                entry_longBrokenMax.insert(0,globals.l1_max)
                entry_longBrokenMax.config(state=DISABLED)

                entry_MediumBrokenMin.config(state=NORMAL)
                entry_MediumBrokenMin.delete(0, 'end')
                entry_MediumBrokenMin.insert(0,globals.m1_min)
                entry_MediumBrokenMin.config(state=DISABLED)

                entry_MediumBrokenMax.config(state=NORMAL)
                entry_MediumBrokenMax.delete(0, 'end')
                entry_MediumBrokenMax.insert(0,globals.m1_max)
                entry_MediumBrokenMax.config(state=DISABLED)

                entry_SmallBrokenMin.config(state=NORMAL)
                entry_SmallBrokenMin.delete(0, 'end')
                entry_SmallBrokenMin.insert(0, globals.s1_min)
                entry_SmallBrokenMin.config(state=DISABLED)

                entry_SmallBrokenMax.config(state=NORMAL)
                entry_SmallBrokenMax.delete(0, 'end')
                entry_SmallBrokenMax.insert(0, globals.s1_max)
                entry_SmallBrokenMax.config(state=DISABLED)
                
            
            #if 1121 is selected
            if clickednew.get() == "1121":
                entry_p_broken_rice.config(state=NORMAL)
                entry_p_broken_rice.delete(0, 'end')
                entry_p_broken_rice.insert(0,globals.b2)
                entry_p_broken_rice.config(state=DISABLED)
                
                entry_longBrokenMin.config(state=NORMAL)
                entry_longBrokenMin.delete(0, 'end')
                entry_longBrokenMin.insert(0,globals.l2_min)
                entry_longBrokenMin.config(state=DISABLED)

                entry_longBrokenMax.config(state=NORMAL)
                entry_longBrokenMax.delete(0, 'end')
                entry_longBrokenMax.insert(0,globals.l2_max)
                entry_longBrokenMax.config(state=DISABLED)

                entry_MediumBrokenMin.config(state=NORMAL)
                entry_MediumBrokenMin.delete(0, 'end')
                entry_MediumBrokenMin.insert(0,globals.m2_min)
                entry_MediumBrokenMin.config(state=DISABLED)

                entry_MediumBrokenMax.config(state=NORMAL)
                entry_MediumBrokenMax.delete(0, 'end')
                entry_MediumBrokenMax.insert(0,globals.m2_max)
                entry_MediumBrokenMax.config(state=DISABLED)

                entry_SmallBrokenMin.config(state=NORMAL)
                entry_SmallBrokenMin.delete(0, 'end')
                entry_SmallBrokenMin.insert(0, globals.s2_min)
                entry_SmallBrokenMin.config(state=DISABLED)

                entry_SmallBrokenMax.config(state=NORMAL)
                entry_SmallBrokenMax.delete(0, 'end')
                entry_SmallBrokenMax.insert(0, globals.s2_max)
                entry_SmallBrokenMax.config(state=DISABLED)

            #if 1121 is selected
            if clickednew.get() == "pk386":
                entry_p_broken_rice.config(state=NORMAL)
                entry_p_broken_rice.delete(0, 'end')
                entry_p_broken_rice.insert(0,globals.b3)
                entry_p_broken_rice.config(state=DISABLED)
                
                entry_longBrokenMin.config(state=NORMAL)
                entry_longBrokenMin.delete(0, 'end')
                entry_longBrokenMin.insert(0,globals.l3_min)
                entry_longBrokenMin.config(state=DISABLED)

                entry_longBrokenMax.config(state=NORMAL)
                entry_longBrokenMax.delete(0, 'end')
                entry_longBrokenMax.insert(0,globals.l3_max)
                entry_longBrokenMax.config(state=DISABLED)

                entry_MediumBrokenMin.config(state=NORMAL)
                entry_MediumBrokenMin.delete(0, 'end')
                entry_MediumBrokenMin.insert(0,globals.m3_min)
                entry_MediumBrokenMin.config(state=DISABLED)

                entry_MediumBrokenMax.config(state=NORMAL)
                entry_MediumBrokenMax.delete(0, 'end')
                entry_MediumBrokenMax.insert(0,globals.m3_max)
                entry_MediumBrokenMax.config(state=DISABLED)

                entry_SmallBrokenMin.config(state=NORMAL)
                entry_SmallBrokenMin.delete(0, 'end')
                entry_SmallBrokenMin.insert(0, globals.s3_min)
                entry_SmallBrokenMin.config(state=DISABLED)

                entry_SmallBrokenMax.config(state=NORMAL)
                entry_SmallBrokenMax.delete(0, 'end')
                entry_SmallBrokenMax.insert(0, globals.s3_max)
                entry_SmallBrokenMax.config(state=DISABLED)

            if clickednew.get() == "brown":
                entry_p_broken_rice.config(state=NORMAL)
                entry_p_broken_rice.delete(0, 'end')
                entry_p_broken_rice.insert(0,globals.b4)
                entry_p_broken_rice.config(state=DISABLED)
                
                entry_longBrokenMin.config(state=NORMAL)
                entry_longBrokenMin.delete(0, 'end')
                entry_longBrokenMin.insert(0,globals.l4_min)
                entry_longBrokenMin.config(state=DISABLED)

                entry_longBrokenMax.config(state=NORMAL)
                entry_longBrokenMax.delete(0, 'end')
                entry_longBrokenMax.insert(0,globals.l4_max)
                entry_longBrokenMax.config(state=DISABLED)

                entry_MediumBrokenMin.config(state=NORMAL)
                entry_MediumBrokenMin.delete(0, 'end')
                entry_MediumBrokenMin.insert(0,globals.m4_min)
                entry_MediumBrokenMin.config(state=DISABLED)

                entry_MediumBrokenMax.config(state=NORMAL)
                entry_MediumBrokenMax.delete(0, 'end')
                entry_MediumBrokenMax.insert(0,globals.m4_max)
                entry_MediumBrokenMax.config(state=DISABLED)

                entry_SmallBrokenMin.config(state=NORMAL)
                entry_SmallBrokenMin.delete(0, 'end')
                entry_SmallBrokenMin.insert(0, globals.s4_min)
                entry_SmallBrokenMin.config(state=DISABLED)

                entry_SmallBrokenMax.config(state=NORMAL)
                entry_SmallBrokenMax.delete(0, 'end')
                entry_SmallBrokenMax.insert(0, globals.s4_max)
                entry_SmallBrokenMax.config(state=DISABLED)

            if clickednew.get() == "super kernel basmati white":
                entry_p_broken_rice.config(state=NORMAL)
                entry_p_broken_rice.delete(0, 'end')
                entry_p_broken_rice.insert(0,globals.b5)
                entry_p_broken_rice.config(state=DISABLED)
                
                entry_longBrokenMin.config(state=NORMAL)
                entry_longBrokenMin.delete(0, 'end')
                entry_longBrokenMin.insert(0,globals.l5_min)
                entry_longBrokenMin.config(state=DISABLED)

                entry_longBrokenMax.config(state=NORMAL)
                entry_longBrokenMax.delete(0, 'end')
                entry_longBrokenMax.insert(0,globals.l5_max)
                entry_longBrokenMax.config(state=DISABLED)

                entry_MediumBrokenMin.config(state=NORMAL)
                entry_MediumBrokenMin.delete(0, 'end')
                entry_MediumBrokenMin.insert(0,globals.m5_min)
                entry_MediumBrokenMin.config(state=DISABLED)

                entry_MediumBrokenMax.config(state=NORMAL)
                entry_MediumBrokenMax.delete(0, 'end')
                entry_MediumBrokenMax.insert(0,globals.m5_max)
                entry_MediumBrokenMax.config(state=DISABLED)

                entry_SmallBrokenMin.config(state=NORMAL)
                entry_SmallBrokenMin.delete(0, 'end')
                entry_SmallBrokenMin.insert(0, globals.s5_min)
                entry_SmallBrokenMin.config(state=DISABLED)

                entry_SmallBrokenMax.config(state=NORMAL)
                entry_SmallBrokenMax.delete(0, 'end')
                entry_SmallBrokenMax.insert(0, globals.s5_max)
                entry_SmallBrokenMax.config(state=DISABLED)


            if clickednew.get() == "super kernel basmati brown":
                entry_p_broken_rice.config(state=NORMAL)
                entry_p_broken_rice.delete(0, 'end')
                entry_p_broken_rice.insert(0,globals.b6)
                entry_p_broken_rice.config(state=DISABLED)
                
                entry_longBrokenMin.config(state=NORMAL)
                entry_longBrokenMin.delete(0, 'end')
                entry_longBrokenMin.insert(0,globals.l6_min)
                entry_longBrokenMin.config(state=DISABLED)

                entry_longBrokenMax.config(state=NORMAL)
                entry_longBrokenMax.delete(0, 'end')
                entry_longBrokenMax.insert(0,globals.l6_max)
                entry_longBrokenMax.config(state=DISABLED)

                entry_MediumBrokenMin.config(state=NORMAL)
                entry_MediumBrokenMin.delete(0, 'end')
                entry_MediumBrokenMin.insert(0,globals.m6_min)
                entry_MediumBrokenMin.config(state=DISABLED)

                entry_MediumBrokenMax.config(state=NORMAL)
                entry_MediumBrokenMax.delete(0, 'end')
                entry_MediumBrokenMax.insert(0,globals.m6_max)
                entry_MediumBrokenMax.config(state=DISABLED)

                entry_SmallBrokenMin.config(state=NORMAL)
                entry_SmallBrokenMin.delete(0, 'end')
                entry_SmallBrokenMin.insert(0, globals.s6_min)
                entry_SmallBrokenMin.config(state=DISABLED)

                entry_SmallBrokenMax.config(state=NORMAL)
                entry_SmallBrokenMax.delete(0, 'end')
                entry_SmallBrokenMax.insert(0, globals.s6_max)
                entry_SmallBrokenMax.config(state=DISABLED)

            
            if clickednew.get() == "1121 sela":
                entry_p_broken_rice.config(state=NORMAL)
                entry_p_broken_rice.delete(0, 'end')
                entry_p_broken_rice.insert(0,globals.b7)
                entry_p_broken_rice.config(state=DISABLED)
                
                entry_longBrokenMin.config(state=NORMAL)
                entry_longBrokenMin.delete(0, 'end')
                entry_longBrokenMin.insert(0,globals.l7_min)
                entry_longBrokenMin.config(state=DISABLED)

                entry_longBrokenMax.config(state=NORMAL)
                entry_longBrokenMax.delete(0, 'end')
                entry_longBrokenMax.insert(0,globals.l7_max)
                entry_longBrokenMax.config(state=DISABLED)

                entry_MediumBrokenMin.config(state=NORMAL)
                entry_MediumBrokenMin.delete(0, 'end')
                entry_MediumBrokenMin.insert(0,globals.m7_min)
                entry_MediumBrokenMin.config(state=DISABLED)

                entry_MediumBrokenMax.config(state=NORMAL)
                entry_MediumBrokenMax.delete(0, 'end')
                entry_MediumBrokenMax.insert(0,globals.m7_max)
                entry_MediumBrokenMax.config(state=DISABLED)

                entry_SmallBrokenMin.config(state=NORMAL)
                entry_SmallBrokenMin.delete(0, 'end')
                entry_SmallBrokenMin.insert(0, globals.s7_min)
                entry_SmallBrokenMin.config(state=DISABLED)

                entry_SmallBrokenMax.config(state=NORMAL)
                entry_SmallBrokenMax.delete(0, 'end')
                entry_SmallBrokenMax.insert(0, globals.s7_max)
                entry_SmallBrokenMax.config(state=DISABLED)


        def yes():
            m_broken_rice = entry_p_broken_rice.get() #broken
            min_long_broken = entry_longBrokenMin.get() #min long broken
            max_long_broken = entry_longBrokenMax.get() #max long broken
            min_med_broken = entry_MediumBrokenMin.get() #min medium broken
            max_med_broken = entry_MediumBrokenMax.get() #max medium broken
            min_small_broken = entry_SmallBrokenMin.get() #min small broken
            max_small_broken = entry_SmallBrokenMax.get() #max small broken
            selected_value_type = clickednew.get() 
            print(m_broken_rice, min_long_broken, max_long_broken, min_med_broken, max_med_broken, min_small_broken, max_small_broken )
            if (0.1 <= float(min_long_broken) <= 20 and
                0.1 <= float(max_long_broken) <= 20 and
                0.1 <= float(min_med_broken) <= 20 and
                0.1 <= float(max_med_broken) <= 20 and
                0.1 <= float(min_small_broken) <= 20 and
                0.1 <= float(max_small_broken) <= 20 ):

                print("if working")
                #we use LIKE keyword when we need to match string values
                conn.execute("UPDATE profile_table set BROKEN = ?, LONG_BROKEN_MIN = ?, LONG_BROKEN_MAX = ?, MEDIUM_BROKEN_MIN = ?, MEDIUM_BROKEN_MAX = ?, SMALL_BROKEN_MIN = ?, SMALL_BROKEN_MAX = ? where TYPE_RICE LIKE ?",
                             (m_broken_rice, min_long_broken, max_long_broken, min_med_broken, max_med_broken, min_small_broken, max_small_broken, selected_value_type))
                conn.commit()  

                win_destroy()
                window_close()              

##            cursor = conn.execute("SELECT BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX from profile_table where TYPE_RICE LIKE ?",(selected_value_type,))
##            for row in cursor:
##               print("TYPE_RICE = ", row[0])
##               print("BROKEN = ", row[1])
##               print ("LONG_BROKEN_MIN = ", row[2])
##               print ("LONG_BROKEN_MAX = ", row[3])
##               print ("MEDIUM_BROKEN_MIN = ", row[4], "\n")

    ##                report.get_sampleNo(get_sampleNo)
    ##                report.get_date(a)
    ##                report.get_day(b)
    ##                report.get_arrivalNo(c)
    ##                report.get_partyName(d)
    ##                report.get_vehicleNo(e)
    ##                report.get_riceType(get_riceType)
    ##                report.get_moisture(f)
    ##                report.get_look(g)
    ##
    ##                reportnew.get_sampleNo(get_sampleNo)
    ##                reportnew.get_date(a)
    ##                reportnew.get_day(b)
    ##                reportnew.get_arrivalNo(c)
    ##                reportnew.get_partyName(d)
    ##                reportnew.get_vehicleNo(e)
    ##                reportnew.get_riceType(get_riceType)
    ##                reportnew.get_moisture(f)
    ##                reportnew.get_look(g)


                
            else:
                win_destroy()
                mmlabel_error= tk.Label(window, text= "Please enter the correct values")
                mmlabel_error.config(font=('helvetica', 14),bg = "#d1d1d1", fg="red")
                mmlabel_error.place(x=180, y=470)

                #tkinter.messagebox.showerror(title='Invalid Entry',message='Please Enter the correct values')
                
                

        def no():
            entry_p_broken_rice.delete(0,'end')
            entry_longBrokenMin.delete(0, 'end')
            entry_longBrokenMax.delete(0, 'end')
            entry_MediumBrokenMin.delete(0, 'end')
            entry_MediumBrokenMax.delete(0, 'end')
            entry_SmallBrokenMin.delete(0, 'end')
            entry_SmallBrokenMax.delete(0,'end')
            #txtfld6.delete(0, 'end')
            win_destroy()

        def ok():
            global win
            win = Toplevel()
            win.geometry('250x100')
            win.title('Continue')
            message = "Do you want to save changes?"
            Label(win, text=message, fg='grey', font=("Helvetica", 12)).place(x=20, y=10)
            Button(win, text='Yes', command=yes, width=5, height=1).place(x=50, y=60)
            Button(win, text='No', command=no, width=5, height=1).place(x=150, y=60)

        def win_destroy():
            global win
            win.destroy()

        def broken_func():
            entry_p_broken_rice.config(state=NORMAL)

        def long_broken_func():
            entry_longBrokenMin.config(state=NORMAL)
            entry_longBrokenMax.config(state=NORMAL)

        def med_broken_func():
            entry_MediumBrokenMin.config(state=NORMAL)
            entry_MediumBrokenMax.config(state=NORMAL)

        def small_broken_func():
            entry_SmallBrokenMin.config(state=NORMAL)
            entry_SmallBrokenMax.config(state=NORMAL)

####yes function ends###
            

        #Check box for rice type input
        clickednew = StringVar(window)
        clickednew.set("irri-6")

        label4 = tk.Label(window, text='Please select your Rice Type')
        label4.config(font=('helvetica', 10), bg ='floral white')
        #self.label4.grid(row=1, column=0, sticky="n")
        label4.place(x=190, y=60)
        #tk.create_window(150, 30, window=label4, master=profile_form_root)

        dropnew = OptionMenu(window, clickednew, "irri-6", "1121","pk386","brown","super kernel basmati white","super kernel basmati brown","1121 sela",command=on_option_change)
        #dropnew.place(x=130, y=80, height=35)
        dropnew.place(x=240, y=90)
        #dropnew.grid(row=2, column=0, sticky="n")
        #tk.create_window(150,60, window=dropnew, master= profile_form_root)
        ##


        # Create a Frame for border

        p_broken_rice = Label(window, text="Broken Rice", fg='black', bg ='floral white',highlightbackground="#37d3ff", font=("Helvetica", 12))
        p_broken_rice.place(x=80, y=155)
        entry_p_broken_rice = Entry(window, width=40, highlightthickness=1, highlightbackground="#fff", highlightcolor= mustard_color)
        entry_p_broken_rice.place(x=250, y=150, height=35)
        entry_p_broken_rice.insert(0,globals.b1)
        entry_p_broken_rice.config(disabledbackground="#d1d1d1", state=DISABLED)

        edit_btn_broken_rice = Button(window, text="Edit", width=7, height=1, command=broken_func, bd=2,highlightcolor='grey48',
                        relief=GROOVE)
        edit_btn_broken_rice.place(x=510, y=150)

        p_long_broken = Label(window, text="Long Broken", fg='black', bg ='floral white', font=("Helvetica", 12))
        p_long_broken.place(x=80, y=205)
##                self.p_txtfld_long_broken = Entry(self.window, width=40, highlightthickness=1, highlightbackground="#fff", highlightcolor="#F1C40F")
##                self.p_txtfld_long_broken.place(x=250, y=200, height=35)
##                self.p_txtfld_long_broken.insert(0, globals.l1)
##                self.p_txtfld_long_broken.config(disabledbackground="#d1d1d1", state=DISABLED)

        ##
        entry_longBrokenMin = Entry(window,width=10 , highlightthickness=1, highlightbackground="#fff", highlightcolor= mustard_color)
        entry_longBrokenMin.place(x=250, y=200, height=35)
        entry_longBrokenMin.insert(0, globals.l1_min)
        entry_longBrokenMin.config(disabledbackground="#d1d1d1", state=DISABLED)
        #canvas1.create_window(45, 200, window=entry_longBrokenMin)#45,200

        label_min= tk.Label(window, text= "min")
        label_min.config(font=('helvetica', 10), bg = "#d1d1d1",width=7)
        label_min.place(x=252, y=235)
##                canvas1.create_window(45, 220, window=label_min)#45,220

        label_line= tk.Label(window, text= "--")
        label_line.config(font=('helvetica', 10), bg = "#d1d1d1")
        label_line.place(x=320, y=210, height=10)
       

        entry_longBrokenMax = Entry(window,width=10 , highlightthickness=1, highlightbackground="#fff", highlightcolor= mustard_color)
        entry_longBrokenMax.place(x=350, y=200, height=35)
        entry_longBrokenMax.insert(0, globals.l1_max)
        entry_longBrokenMax.config(disabledbackground="#d1d1d1", state=DISABLED)

        label_min= tk.Label(window, text= "max")
        label_min.config(font=('helvetica', 10),bg = "#d1d1d1",width=7)
        label_min.place(x=352, y=235)

##                label_max= Label(self.window, text= "max")
##                label_max.config(font=('helvetica', 10))
##                canvas1.create_window(95, 220, window=label_max)
        ###
        
        edit_btn_long_broken = Button(window, text="Edit", width=7, height=1, command=long_broken_func, bd=2, highlightcolor='grey48',
                        relief=GROOVE)
        edit_btn_long_broken.place(x=510, y=200)

        p_med_broken = Label(window, text="Medium Broken", fg='black', bg ='floral white', font=("Helvetica", 12))
        p_med_broken.place(x=80, y=275)
##                self.p_txtfld_med_broken = Entry(self.window, width=40, highlightthickness=1, highlightbackground="#fff", highlightcolor="#F1C40F")
##                self.p_txtfld_med_broken.place(x=250, y=250, height=35)
##                self.p_txtfld_med_broken.insert(0, globals.m1)
##                self.p_txtfld_med_broken.config(disabledbackground="#d1d1d1", state=DISABLED)
        ##
        entry_MediumBrokenMin = Entry(window,width=10 , highlightthickness=1, highlightbackground="#fff", highlightcolor= mustard_color)
        entry_MediumBrokenMin.place(x=250, y=270, height=35)
        entry_MediumBrokenMin.insert(0, globals.m1_min)
        entry_MediumBrokenMin.config(disabledbackground="#d1d1d1", state=DISABLED)

        label_min= tk.Label(window, text= "min")
        label_min.config(font=('helvetica', 10), bg = "#d1d1d1",width=7)
        label_min.place(x=252, y=305)
        
        label_line= tk.Label(window, text= "--")
        label_line.config(font=('helvetica', 10), bg = "#d1d1d1")
        label_line.place(x=320, y=280, height=10)
        
        entry_MediumBrokenMax = Entry(window,width=10 , highlightthickness=1, highlightbackground="#fff", highlightcolor= mustard_color)
        entry_MediumBrokenMax.place(x=350, y=270, height=35)
        entry_MediumBrokenMax.insert(0, globals.m2_max)
        entry_MediumBrokenMax.config(disabledbackground="#d1d1d1", state=DISABLED)
        ##

        label_min= tk.Label(window, text= "max")
        label_min.config(font=('helvetica', 10),bg = "#d1d1d1",width=7)
        label_min.place(x=352, y=305)

        edit_btn_med_broken = Button(window, text="Edit", width=7, height=1, command=med_broken_func, bd=2, highlightcolor='grey48',
                        relief=GROOVE)
        edit_btn_med_broken.place(x=510, y=270)

        ##for small broken
        p_small_broken = Label(window, text="Small Broken", fg='black', bg ='floral white', font=("Helvetica", 12))
        p_small_broken.place(x=80, y=345)

        entry_SmallBrokenMin = Entry(window,width=10 , highlightthickness=1, highlightbackground="#fff", highlightcolor= mustard_color)
        entry_SmallBrokenMin.place(x=250, y=340, height=35)
        entry_SmallBrokenMin.insert(0, globals.s1_min)
        entry_SmallBrokenMin.config(disabledbackground="#d1d1d1", state=DISABLED)

        label_min= tk.Label(window, text= "min")
        label_min.config(font=('helvetica', 10), bg = "#d1d1d1",width=7)
        label_min.place(x=252, y=375)
        
        label_line= tk.Label(window, text= "--")
        label_line.config(font=('helvetica', 10), bg = "#d1d1d1")
        label_line.place(x=320, y=350, height=10)

        entry_SmallBrokenMax = Entry(window,width=10 , highlightthickness=1, highlightbackground="#fff", highlightcolor= mustard_color)
        entry_SmallBrokenMax.place(x=350, y=340, height=35)
        entry_SmallBrokenMax.insert(0, globals.s1_max)
        entry_SmallBrokenMax.config(disabledbackground="#d1d1d1", state=DISABLED)
        ##

        label_min= tk.Label(window, text= "max")
        label_min.config(font=('helvetica', 10),bg = "#d1d1d1",width=7)
        label_min.place(x=352, y=375)

        edit_btn_small_broken = Button(window, text="Edit", width=7, height=1, command=small_broken_func, bd=2, highlightcolor='grey48',
                        relief=GROOVE)
        edit_btn_small_broken.place(x=510, y=340)
        

        #self.iimage = tk.PhotoImage(file="img/iconb.png",  master=profile_form_root)
        #self.ok_btn = Button(self.window, text="OK", image=self.iimage,compound="top",  width=80, height=50, command=ok, bd=5, highlightcolor='grey48', relief=RIDGE)
        ok_btn = Button(window, text="OK",  width=20, height=2, command=ok, bd=2, highlightcolor='grey48',  bg = "#62d18f", fg="black",
                        relief=GROOVE)
        ok_btn.place(x=120, y=420)

        cancel_btn = Button(window, text="CANCEL", width=20, command=window_close, height=2, bd=2, bg= "#aaadaa", fg="black",
                            highlightcolor='grey48',
                            relief=GROOVE)
        cancel_btn.place(x=320, y=420)

        window.protocol('WM_DELETE_WINDOW',window_close) #to perform functionality when user close from title bar



    profile_form_user(profile_form_root)
    profile_form_root.mainloop()
##########profile function ends here#########



def background_image(my_masterr):
    image1 = Image.open("img/rice_bg.jpg")
    image1 = image1.resize((Image_screen_width, Image_screen_height), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(image1, master= my_masterr)
    label2 = tk.Label(my_masterr,image=photo2)
    label2.image = photo2 # keep a reference!
    label2.grid(row=0, column=0)
    my_masterr.columnconfigure(0, weight=1)
    my_masterr.rowconfigure(0, weight=1)
    #label2.pack(side="left" ,padx=0, pady=0, fill=BOTH)

def pdf_view():
    #leena
    #this is where if user first click on summarize tab without input
    #globals.no_value_selected is 3 or 
    if globals.no_user_input is 3 or globals.browse_image is 3:
       # globals.no_type_selected=0
        globals.no_value_selected=0
        globals.no_user_input=0
        globals.browse_image=0
        
    #from report import no_type_selected,no_value_selected,no_user_input
    #print(str(no_type_selected))
    #this is where user input something null
    #globals.no_value_selected is 0 or    
    if  globals.no_user_input is 0 or globals.browse_image is 0:
        tkinter.messagebox.showerror(title='Summarized Report Fail',message='No Report is generated')
    ####
    else:
        #print(nofile)
        statusbar['text'] ="Summarized Report"
        webbrowser.open_new(globals.S_Report)

################################
# To reset all        
################################

#this below function is  to reset form values when reset button is clicked
def reset_form_values():
    # import reportnew
    # import report
    
    
    report.get_sampleNo("")
    report.get_date("")
    report.get_day("")
    report.get_arrivalNo("")
    report.get_partyName("")
    report.get_vehicleNo("")
    report.get_riceType("")
    report.get_moisture("")
    report.get_look("")

    reportnew.get_sampleNo("")
    reportnew.get_date("")
    reportnew.get_day("")
    reportnew.get_arrivalNo("")
    reportnew.get_partyName("")
    reportnew.get_vehicleNo("")
    reportnew.get_riceType("")
    reportnew.get_moisture("")
    reportnew.get_look("")
    
    
def reset_button():
    globals.reset=0
    #from report import no_type_selected,no_value_selected,no_user_input
    #globals.no_type_selected=0
    #globals.no_value_selected=0
    globals.chart_condition = 0
    globals.no_user_input=0
    globals.browse_image=0
    globals.direct_clicked=0 # this is for browse or scan should not be clicked before 10g
    globals.need_to_reset=0
    reset_form_values() #form values destroy
    global viewSample_counter
    viewSample_counter=0

    #the condition below is to check if the variable is not a string
    #this condition was necessary incase if we click on reset button before doing test
    if not isinstance(globals.label,str): 
        #this is to clear the view sample by destroying elements in it
##        globals.label_input.destroy()
##        globals.label_processed.destroy()
        #globals.button_to_open_new_window.destroy()
        globals.label2.destroy()
        globals.label.destroy()
        global arrow_label1
        arrow_label1.destroy()
        

    if not isinstance(globals.canvas_piechart,str): 
        #to destroy pie chart when reset
        globals.canvas_piechart.get_tk_widget().destroy()

    if os.path.exists("scan"): 
        # Muzammil adding these lines for deleting our temp imgs
        shutil.rmtree("scan")

    if os.path.exists("yellowTemp"):    
        shutil.rmtree("yellowTemp")

    if os.path.exists("paddy"):    
        shutil.rmtree("paddy")

    if os.path.exists("scan_copy"):    
        shutil.rmtree("scan_copy")

    if os.path.exists("yellow"):    
        shutil.rmtree("yellow")
    
    if os.path.exists("chaly_temp"):    
        shutil.rmtree("chaly_temp")

    if os.path.exists("chaly_temp3"):    
        shutil.rmtree("chaly_temp3")
            
    #print("lets checkkk"+str(no_type_selected))
    #this below condition is when user cross and don't save changes then it should not show this below message box it should quit and reset only
    if not no_func is 1:
        tkinter.messagebox.showinfo(title='Reset',message='Data Reset Successfully')

####################################
#to get unique filename for summarize report
####################################
def get_currentDir():
    
    #leena
    #getting current directory
    current_path = os.getcwd()
    #print(path)

    global history_directory
    history_directory = os.path.join(current_path,"History")
    if not os.path.exists(history_directory):
        os.mkdir(history_directory)
        
    from datetime import date
    today = str(date.today())

    global datewise_directory
    datewise_directory = os.path.join(history_directory,today)
    if not os.path.exists(datewise_directory):
        os.mkdir(datewise_directory)

    i=0
    sampleNo_directory= os.path.join(datewise_directory,"Sample-"+ str(i))
##    if not os.path.exists(sampleNo_directory):
##        os.mkdir(sampleNo_directory)

    bool_value= 0
    while os.path.exists(sampleNo_directory):
        i += 1
        sampleNo_directory= os.path.join(datewise_directory,"Sample-"+ str(i))
        bool_value=1
    
    os.mkdir(sampleNo_directory)    
    
    #combine_path= datewise_directory +'\\'+"Summarized Report.pdf"
    #combine_path_detailed_report= datewise_directory +'\\'+"Detailed Report.pdf"
    ###
    return sampleNo_directory


######merge pdf starts here###########
def merge_pdf():
    from PyPDF2 import PdfFileMerger
    import datetime
    now=datetime.datetime.now()
    a=now.strftime('%Y-%m-%d')
    global datewise_directory
    s_dir= datewise_directory
    merger_s = PdfFileMerger()
    merger_y = PdfFileMerger()

    count=0
    for base, dirs, files in os.walk(s_dir):
        for directories in dirs:
            if directories.startswith("Sample"):
                #print("before count",count)
                source_dir = s_dir+"\\"+"Sample-"+str(count)
                    
                x = [item for item in os.listdir(source_dir) if item.startswith("Summarized") & item.endswith("pdf")]
                y=[item for item in os.listdir(source_dir) if item.startswith("Detailed") & item.endswith("pdf")]
                for pdf in x:
                    newfile = os.path.join(source_dir, pdf) 
                    merger_s.append(newfile)
                for pdf in y:
                    newfile = os.path.join(source_dir, pdf)
                    merger_y.append(newfile)
                    
                count= count+1
                #print("after count",count)

    final_directory = os.path.join(s_dir,"Daily Final Reports")
    if not os.path.exists(final_directory):
        os.mkdir(final_directory)
        
    merger_s.write(final_directory + '/Daily_Summarized_Report.pdf')
    merger_s.close()
        
    merger_y.write(final_directory + '/Daily_Detailed_Report.pdf')
    merger_y.close()

#######merge pdf ends here ############
    

def get_nonexistant_path(fname_path):
    
    
    """
    Get the path to a filename which does not exist by incrementing path.

    Examples
    --------
    >>> get_nonexistant_path('/etc/issue')
    '/etc/issue-1'
    >>> get_nonexistant_path('whatever/1337bla.py')
    'whatever/1337bla.py'
    """
    if not os.path.exists(fname_path):
        return fname_path
    filename, file_extension = os.path.splitext(fname_path)
    i = 1
    new_fname = "{}-{}{}".format(filename, i, file_extension)
    while os.path.exists(new_fname):
        i += 1
        new_fname = "{}-{}{}".format(filename, i, file_extension)
    return new_fname

def center_widget(width,height):
    
    global screen_width,screen_height,x_cordinate,y_cordinate,window_height,window_width
    window_height = height
    window_width = width

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    
#######    
    
#-----------------------------------------------------------#
# Vertical Scroll Section Class Definition
# Vertical Scroll Section Class Definition
#-----------------------------------------------------------#

class VerticalScrolledFrame(tk.Frame):

    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)

#-----------------------------------------------------------#
# Home Page Definition
# Home Page Definition
#-----------------------------------------------------------#
class Home(tk.Frame):
    def __init__(self, parent, controller):

        ######for 100 grain
        def first_test():
        
            global rice_image
            global objects
            
            
            # root.geometry("400x400")
                       #Scanning the sample & checking if 100 grains are on bed
            

            def scan_loading_func():
        
                #disable all button when it is processing
                Sample_button["state"] = "disabled"
                First_test["state"] = "disabled"
                Select_type["state"] = "disabled"
                Select_button["state"] = "disabled"
                Scan_button["state"] = "disabled"
                Repor_button["state"] = "disabled"
                DRepor_button["state"] = "disabled"
                Display_button["state"] = "disabled"
                #pieChart_button["state"] = "disabled"
                Reset_button["state"] = "disabled"
                #####
                
                global prog_bar
                global top_progBar
                top_progBar = Toplevel()

                #these two lines of code are to bring on top this progress bar
                top_progBar.lift()
                top_progBar.attributes("-topmost",True)

                center_widget(360,100)
                top_progBar.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
                top_progBar.title("Loading..")

                prog_bar = ttk.Progressbar(top_progBar,
                                            orient="horizontal",
                                            length=500, mode = "indeterminate")
                prog_bar.pack(side=tk.TOP, pady=8)
                global wait_label
                wait_label = Label(top_progBar, text = "Processing, please wait..", font = ("Arial",13))
                wait_label.pack()
                prog_bar.start()

            def scan_100G_process():
                #try:
                #import reportnew
                globals.no_value_selected= 1
                globals.no_user_input=1
                globals.browse_image=1
                
                #these below lines are necessary for threading operation
                import pythoncom
                pythoncom.CoInitialize()
                ###
                
                statusbar['text'] ="Scanning Image"
                global rice_image
                global objects
            
                wia_dev_manager = Dispatch("WIA.DeviceManager")
                for ix, device in enumerate(wia_dev_manager.DeviceInfos):
                    print(ix,"|",device.Properties("Name").Value,"|",device.DeviceID)
                
                #
                # 0 | Lexmark Pro200-S500 Series | {6BDD1FC6-810F-11D0-BEC7-08002BE2092F}\0000
                #

            # Select a device per gui if there are more than one device
                wia = Dispatch("WIA.CommonDialog")
            
            
                dev = wia.ShowSelectDevice()
            
                dev.Properties("Name").Value
            
        # 'Lexmark Pro200-S500 Series'
        
        # # List Items of device
                for ix, item in enumerate(dev.Items):
                    print(ix,item.ItemID)

            # 0 0000\Root\Flatbed
            # 1 0000\Root\Feeder
            # 2 0002\Root\Top

            # Select per number 
                scanner = dev.Items[1]
                scanner.ItemID
            # '0000\\Root\\Flatbed'
        

            # Set resolution
                scanner.Properties("Vertical Resolution").Value   = 300
                scanner.Properties("Horizontal Resolution").Value = 300
        
                WIA_IMG_FORMAT_PNG       = "{B96B3CAF-0728-11D3-9D7B-0000F81EF32E}"
                image=scanner.Transfer(WIA_IMG_FORMAT_PNG)
                our_path=get_currentDir()
                a=str(random.randint(1,1000))
                filename= str(our_path+'\\scan_'+a)
                image.SaveFile(filename+".png")
        
                im = Image.open(filename + '.png')
                im.save(filename + '.jpg')
            
                #os.remove(filename + '.png')
                path = str(filename+'.png')
                rice_image = cv2.imread(path)

                #leena
                
                globals.D_Report = get_nonexistant_path(our_path +'\\'+"Detailed Report.pdf")
                #####

                if globals.rice_type_selected == "irri-6":
                    objects=analysis_irri6.analyze(rice_image,globals.D_Report)
                elif globals.rice_type_selected == "1121":
                    objects=analysis_1121.analyze(rice_image,globals.D_Report)
                elif globals.rice_type_selected == "pk386":
                    objects=analysis_pk386.analyze(rice_image,globals.D_Report)
                elif globals.rice_type_selected == "brown":
                    objects=analysis_brown.analyze(rice_image,globals.D_Report)
                elif globals.rice_type_selected == "super kernel basmati white":
                    objects=analysis_super_kernel_basmati_white.analyze(rice_image,globals.D_Report)
                elif globals.rice_type_selected == "super kernel basmati brown":
                    objects=analysis_super_kernel_basmati_brown.analyze(rice_image,globals.D_Report)
                elif globals.rice_type_selected == "1121 sela":
                    objects=analysis_1121_sela.analyze(rice_image,globals.D_Report)
            
                
                os.remove(path)
                reportnew.calculate_no_of_grains(objects)
                grains = len(objects)
                if(grains != 100):
                    os.remove(our_path +'\\'+"Detailed Report.pdf")
                
                #leena
                #globals.S_Report=get_nonexistant_path(our_path +'\\'+"Summarized Report.pdf")
                #####

                #reportnew.gen_report(objects,globals.S_Report)
                #from reportnew import ldata, cdata, tdata, Date, Time
                #from reportnew import AGL
            # print(reportnew.ldata,reportnew.cdata,reportnew.tdata)


                stop=prog_bar.stop()
                    
                if stop is None:
                
                    top_progBar.destroy()

                    #enable all buttons when the processing is completed
                    Sample_button["state"] = "active"
                    First_test["state"] = "normal"
                    Select_type["state"] = "normal"
                    Select_button["state"] = "normal"
                    Scan_button["state"] = "normal"
                    Repor_button["state"] = "active"
                    DRepor_button["state"] = "active"
                    Display_button["state"] = "normal"
                    #pieChart_button["state"] = "normal"
                    Reset_button["state"] = "normal"
                    ###

                    globals.need_to_reset=1
                    
                    #tkinter.messagebox.showinfo("Processing Completed","Please click on View Sample Tab to see results.")
                    
                
                #except clause to check for 100 grains
                if(reportnew.calculate_no_of_grains.no_of_grains != 100):
                    print(reportnew.calculate_no_of_grains.no_of_grains)
                    tk.messagebox.showinfo("Grains Quantity =", grains)
                    statusbar['text'] ="Error!"
                    tkinter.messagebox.showerror(title='Error!',
                    message='Please put 100 grains on scanner bed then scan again')
                    #root2.destroy()
                else:
                    #print("Before changing the flag",runflag)
                    #global runflag
                    runflag = 1
                    print("After changing the flag",runflag)

                    #leena
                    #globals.D_Report = get_nonexistant_path(our_path +'\\'+"Detailed Report.pdf")
                    globals.S_Report=get_nonexistant_path(our_path +'\\'+"Summarized Report.pdf")
                    #####
                    if globals.rice_type_selected == "irri-6":
                        reportnew.gen_report_irri6(objects,globals.S_Report)
                    elif globals.rice_type_selected == "1121":
                        reportnew.gen_report_1121(objects,globals.S_Report)
                    elif globals.rice_type_selected == "pk386":
                        reportnew.gen_report_pk386(objects,globals.S_Report)
                    elif globals.rice_type_selected == "brown":
                        reportnew.gen_report_brown(objects,globals.S_Report)
                    elif globals.rice_type_selected == "super kernel basmati white":
                        reportnew.gen_report_super_kernel_basmati_white(objects,globals.S_Report)
                    elif globals.rice_type_selected == "super kernel basmati brown":
                        reportnew.gen_report_super_kernel_basmati_brown(objects,globals.S_Report)
                    elif globals.rice_type_selected == "1121 sela":
                        reportnew.gen_report_1121_sela(objects,globals.S_Report)
                    
                    #reportnew.gen_report(objects,globals.S_Report)
                    from reportnew import ldata, cdata, tdata, Date, Time
                    from reportnew import AGL
                    merge_pdf()
                    print(reportnew.ldata,reportnew.cdata,reportnew.tdata)
                    statusbar['text'] ="Processing Completed"
                    globals.chart_condition = 1
                    tkinter.messagebox.showinfo("Processing Completed","Please click on View Sample Tab to see results.")
                # except:
                #     print("except condition true")
                #     stop=prog_bar.stop()
                #     if stop is None:
                    
                #         top_progBar.destroy()

                #         #enable all buttons when the processing is completed
                #         Sample_button["state"] = "active"
                #         First_test["state"] = "normal"
                #         Select_type["state"] = "normal"
                #         Select_button["state"] = "normal"
                #         Scan_button["state"] = "normal"
                #         Repor_button["state"] = "active"
                #         DRepor_button["state"] = "active"
                #         Display_button["state"] = "normal"
                #         #pieChart_button["state"] = "normal"
                #         Reset_button["state"] = "normal"
                #         ###

                #         globals.need_to_reset=1
                #     tkinter.messagebox.showerror("Scanner not connected","Please Connect the scanner.")
                    
                    #root2.destroy()

                    ###leena#################

##                    stop=prog_bar.stop()
##                     
##                    if stop is None:
##                    
##                        top_progBar.destroy()
##
##                        #enable all buttons when the processing is completed
##                        Sample_button["state"] = "active"
##                        First_test["state"] = "normal"
##                        Select_type["state"] = "normal"
##                        Select_button["state"] = "normal"
##                        Scan_button["state"] = "normal"
##                        Repor_button["state"] = "active"
##                        DRepor_button["state"] = "active"
##                        Display_button["state"] = "normal"
##                        Reset_button["state"] = "normal"
##                        ###
##
##                        globals.need_to_reset=1
                            
                    #statusbar['text'] ="Processing Completed"
            
##                except:
##                    stop=prog_bar.stop()
##                    if stop is None:
##
##                        top_progBar.destroy()
##
##                        #enable all buttons when the processing is completed
##                        Sample_button["state"] = "active"
##                        First_test["state"] = "normal"
##                        Select_type["state"] = "normal"
##                        Select_button["state"] = "normal"
##                        Scan_button["state"] = "normal"
##                        Repor_button["state"] = "active"
##                        DRepor_button["state"] = "active"
##                        Display_button["state"] = "normal"
##                        Reset_button["state"] = "normal"
##                        ###
##
##                    
##                    #root2.destroy()
##                    #except clause
##                    statusbar['text'] ="Error!"
##                    tkinter.messagebox.showerror(title='Scanner Not Found',
##                                            message='Check Your Scanner! Whether Its Connected or Not!')

            def scan_for_100_grains():
                #myLabel = Label(canvas1, text=clicked.get()).pack()
                
                #selected_type = clickednew.get()
                #x1 = entry1.get()
                #x2 = entry2.get()
                # Variable for chalky input
                #myLabel2 = Label(canvas1, text=clickednew.get()).pack()
                selected_value_chalky = clickednew.get()
                print("The selected value for seleted type input is",selected_value_chalky)
                globals.rice_type_selected = selected_value_chalky
                root1.destroy()
                
                #reportnew.calculate_type(selected_value_chalky)
                
                threading.Thread(target=scan_100G_process).start()
                threading.Thread(target=scan_loading_func).start()

                
##            def shownew():
##        
##                myLabel = Label(canvas1, text=clicked.get()).pack()
##                
##                selected_type = clicked.get()
##                #x1 = entry1.get()
##                #x2 = entry2.get()
##                
##                root1.destroy()
##                
##                reportnew.calculate_type(selected_type)
##                #reportnew.get_user_input(x1)
##                #reportnew.get_user_input2(x2)
##                
##                #Executing 100 grains test code here
##                #Initializing the root again
##                global root2
##                root2 = tk.Tk()
##                root2.title("Test for AGL & AGW")
##
##                #Initializing Canvas
##                canvas2 = tk.Canvas(root2, width =400, height = 100)
##                canvas2.pack()
##                
##              
##                label1 = tk.Label(root2, text='Put 100 Grains on Scanner than Scan')
##                label1.config(font=('helvetica', 10))
##                canvas2.create_window(200, 20, window=label1)
##               
##                # Scan button to scan for exactly 100 grains
##                myButton = Button(canvas2,text = "Scan", command=scan_for_100_grains)
##                canvas2.create_window(200, 60, window=myButton)

              
            
             #leena
            if globals.need_to_reset is not 1:
                root1 = tk.Tk()
                root1.title("100 Grains Testing")
                root1.geometry("400x400")
            
                #canvas1 = tk.Canvas(root1, width =300, height = 300)
                #canvas1.config(bg="floral white")
                
                #canvas1.pack()

                background_image(root1)
                # Initializing the button for selection of Rice Type & Drop Down for Rice Types
                #clicked = StringVar(root1)
                #clicked.set("Basmati")
                
                # label1 = tk.Label(root1, text='Please Click on Scan Button')
                # label1.config(font=('helvetica', 10))
                # canvas1.create_window(150, 20, window=label1)

                #drop = OptionMenu(canvas1, clicked, "Basmati", "Non-Basmati")
                #canvas1.create_window(150, 50, window=drop)

                #Check box for chalky% input
                clickednew = StringVar(root1)
                clickednew.set("irri-6")

                label4 = tk.Label(root1, text='Please Select Your Rice Type ')
                label4.config(font=('helvetica', 10), bg = "floral white")
                label4.place(relx=.5,rely=.15, anchor="center")
                #canvas1.create_window(150, 30, window=label4)

##                labell4 = tk.Label(root1, text='"Percentage"')
##                labell4.config(font=('helvetica', 14), bg = "floral white")
##                labell4.place(relx=.5,rely=.23, anchor="center")
                #canvas1.create_window(150, 60, window=labell4)
                
                dropnew = OptionMenu(root1, clickednew, "irri-6", "1121", "pk386","brown","super kernel basmati white","super kernel basmati brown","1121 sela")
                dropnew.place(relx=.5,rely=.33, anchor="center")
                #canvas1.create_window(150,100, window=dropnew)
                

                # Closing the Canvas & executing functions in report file
                myButton = Button(root1,text = "Scan", command=scan_for_100_grains,width=20, height=2,bd=2, highlightcolor='grey48',  bg = "#62d18f", fg="black",
                        relief=GROOVE)
                myButton.place(relx=.5,rely=.53, anchor="center")
                #canvas1.create_window(150, 170, window=myButton)

                #leena
                #root1.protocol('WM_DELETE_WINDOW',scan_for_100_grains) #to perform functionality when close from title bar
                ###
                
                # on change dropdown value
                # def change_dropdown(*args):
                #     print(clicked.get())
                
                # clicked.trace('w', change_dropdown)
                
                root1.mainloop()

            else:
                tkinter.messagebox.showwarning("Reset","Please click on Reset Button.")

############################## For 100 Grains end here #####################################
             
        def select_type():
            # import report
            # import reportnew

            global rice_image
            global objects
            
            
            def show():
                def TenG_yes():
                    #import report

                    yes_userInformation()
                    
                    globals.direct_clicked=1
                    #myLabel = Label(canvas1, text=clicked.get()).pack()

                    #selected_type = clicked.get()
                    
                    #x1 = entry1.get()
                    
##                    x2 = entry2.get()

                    #rice type
                    #global rice_type_selected
                    globals.rice_type_selected =type_selection.get()
                    print("The selected rice type is:", globals.rice_type_selected)

                    #leena
                    #sqlite database select
                    cursor = conn.execute("SELECT BROKEN, LONG_BROKEN_MIN, LONG_BROKEN_MAX, MEDIUM_BROKEN_MIN, MEDIUM_BROKEN_MAX, SMALL_BROKEN_MIN, SMALL_BROKEN_MAX from profile_table where TYPE_RICE LIKE ?",(globals.rice_type_selected,))
                    for row in cursor:
                        x1 = str(row[0])                #broken
                        x4_longBrokenMin = row[1] #long broken min
                        x3_longBrokenMax = row[2] #long broken max
                        x6_MediumBrokenMin = row[3] #med broken min
                        x5_MediumBrokenMax = row[4] #med broken max
                        x8_SmallBrokenMin = row[5]  #small broken min
                        x7_SmallBrokenMax = row[6] #small broken max
                        
                    ####

                    #leena
##                    x3_longBrokenMax = entry_longBrokenMax.get()
##                    x4_longBrokenMin = entry_longBrokenMin.get()
##                    x5_MediumBrokenMax = entry_MediumBrokenMax.get()
##                    x6_MediumBrokenMin = entry_MediumBrokenMin.get()
##                    x7_SmallBrokenMax = entry_SmallBrokenMax.get()
##                    x8_SmallBrokenMin = entry_SmallBrokenMin.get()
                    ###

                    # Variable for chalky input
                    #myLabel2 = Label(canvas1, text=clickednew.get()).pack()
                    # selected_value_chalky = clickednew.get()
                    # print("The selected value for chalky input is",selected_value_chalky)

                    #root.destroy()


                    #report.calculate_type(selected_type)
                    #print("x1:broken:",x1)
                    #analysis.chalky_input(selected_value_chalky)
                    report.get_user_input(x1)
##                    report.get_user_input2(x2)

                    #leena
                    report.get_input_LongBroken(x3_longBrokenMax, x4_longBrokenMin)
                    report.get_input_MediumBroken(x5_MediumBrokenMax, x6_MediumBrokenMin)
                    report.get_input_SmallBroken(x7_SmallBrokenMax, x8_SmallBrokenMin)
                    ###
 
                    #if no_type_selected is 0 or no_value_selected is 0 or no_user_input is 0:
                    #tkinter.messagebox.showerror(title='Detailed Report Fail',message='No Report is generated')
                    
                    #from reportnew import AGL
                    if (runflag == 0):
                        temp_AGL = 0
                        print("100 Grain test not run",temp_AGL)
                    else:
                        temp_AGL = AGL
                        print("100 Grain test run",temp_AGL)
                        print("yes")
                        
                    TenG_cancel()
                    TenG_no()

                #leena
                def TenG_cancel():
                    no_userInformation()
                    neww_win.destroy()

                def TenG_no():
                    no_userInformation()
                    TenG_cancel()
                    root_10g.destroy()
                ###
                    

                #leena 
                neww_win = Toplevel()
                neww_win.geometry('320x100')#300x100
                neww_win.title('Grain Testing')
                message = "Changes have been made in the form.\n Save changes?"
                Label(neww_win, text=message, fg='grey', font=("Helvetica", 12)).place(x=40, y=10)
                Button(neww_win, text='Yes',command=TenG_yes, width=5, height=1).place(x=50, y=60)
                Button(neww_win, text='No', command=TenG_no, width=5, height=1).place(x=120, y=60)
                Button(neww_win, text='Cancel', command=TenG_cancel, width=6, height=1).place(x=190, y=60)
                ###

            ###user information##
            def yes_userInformation():
                get_sampleNo=self.entry_sampleNo.get() #sample no
                a = self.txtfld.get() #date
                b = self.txtfld1.get() #day
                c = self.txtfld2.get() #arrival number
                d = self.txtfld3.get() #party name
                e = self.txtfld4.get()  #vehicle number
                get_riceType = self.entry_riceType.get() #rice type
                f = self.txtfld5.get() #moisture
                g = self.txtfld6.get() #look
                print(get_sampleNo,a, b, c, d, e,get_riceType, f, g)


                report.get_sampleNo(get_sampleNo)
                report.get_date(a)
                report.get_day(b)
                report.get_arrivalNo(c)
                report.get_partyName(d)
                report.get_vehicleNo(e)
                report.get_riceType(get_riceType)
                report.get_moisture(f)
                report.get_look(g)

                reportnew.get_sampleNo(get_sampleNo)
                reportnew.get_date(a)
                reportnew.get_day(b)
                reportnew.get_arrivalNo(c)
                reportnew.get_partyName(d)
                reportnew.get_vehicleNo(e)
                reportnew.get_riceType(get_riceType)
                reportnew.get_moisture(f)
                reportnew.get_look(g)

                #win_destroy()
                #window_close()

            def no_userInformation():
                self.entry_sampleNo.delete(0,'end')
                #self.txtfld.delete(0, 'end')
                #self.txtfld1.delete(0, 'end')
                self.txtfld2.delete(0, 'end')
                self.txtfld3.delete(0, 'end')
                self.txtfld4.delete(0, 'end')
                self.entry_riceType.delete(0,'end')
                self.txtfld5.delete(0, 'end')
                self.txtfld6.delete(0, 'end')
                #win_destroy()

            def ok_userInformation():
                self.win = Toplevel()
                self.win.geometry('250x100')
                self.win.title('Continue')
                message = "Do you want to save changes?"
                Label(self.win, text=message, fg='grey', font=("Helvetica", 12)).place(x=20, y=10)
                Button(self.win, text='Yes', command=yes_userInformation, width=5, height=1).place(x=50, y=60)
                Button(self.win, text='No', command=no_userInformation, width=5, height=1).place(x=150, y=60)

            def window_close():
                root_10g.destroy()
                
            def win_destroy():
                self.win.destroy()
    
            ##user information end##
        
            if globals.need_to_reset is not 1:
                
                root_10g = tk.Tk()
                root_10g.title("Rice Type Selection")
                root_10g.geometry("600x700")

                root_10g.columnconfigure(0, weight=1)
                root_10g.rowconfigure(0, weight=1)

               
                #leena
                #for tab window
                style_10g = ttk.Style(root_10g)

                #parent alt change to classic so that dashed border can disappear
                style_10g.theme_create( "tabStyle", parent="classic", settings={
                "TNotebook": {"configure": {"tabmargins": [20, 7, 20, 5] } },
                "TNotebook.Tab": {
                "configure": {"padding": [10, 10], "background": "#ffffff", "width": root_10g.winfo_screenwidth(), "anchor": "center", "font": (mfont_family,12,"bold")},
                "map":       {"background": [("selected", mustard_color)] } } } )

                style_10g.theme_use("tabStyle")
                
##                style_10g.configure('TNotebook.Tab', width=root_10g.winfo_screenwidth(), padding=[10, 10], foreground="#dd0202")
##                #style_10g.map("TNotebook.Tab",  background=[("selected", "#dd0202")]);
##                                
                tabControl = ttk.Notebook(root_10g)
                #tabControl.grid(row=0, column=0, sticky='nsew')


                #for 10g test
                tab1 = ttk.Frame(tabControl)
                #for user information form
                tab2 = ttk.Frame(tabControl)

                tabControl.add(tab1, text ='10g Test')
                tabControl.add(tab2, text ='User Information')
                tabControl.pack(expand = 1, fill ="both")

                
                #canvas1 = Canvas(tab1, height = 400, width = 400 ) #height = 280, width = 400, bg ="lavender"
                #canvas1.grid(row=0, column=0)
                #canvas1.pack()

                background_image(tab1)



##                # Code to Enter the Rice Size directly for broken rice detection
##                label2 = tk.Label(root, text='Option 1:  Insert the number in mm for broken size')
##                label2.config(font=('helvetica', 10))
##                canvas1.create_window(200, 100, window=label2)#200,100
##
##                entry1 = tk.Entry(root)
##                canvas1.create_window(200, 130, window=entry1) #200,130


                #leena
                #Check box for chalky% input
                #clickednew = StringVar(tab1)
                #clickednew.set("less than 50%")

                label4 = tk.Label(tab1, text='Start Your Test' ,fg="#336699")
                label4.config(font=(mfont_family, 24,"bold"))
                label4.place(relx=.5,rely=.15, anchor="center")
                # #canvas1.create_window(200, 30, window=label4)

                # dropnew = OptionMenu(tab1, clickednew, "less than 50%", "greater than 50%")
                # dropnew.place(relx=.5,rely=.23, anchor="center")
                # #canvas1.create_window(200,60, window=dropnew)

                #for type selection
                type_selection = StringVar(tab1)
                globals.rice_type_selected = "irri-6"
                type_selection.set(globals.rice_type_selected)

                label4_ty = tk.Label(tab1, text='Please choose your rice type ')
                label4_ty.config(font=(mfont_family, 14))
                label4_ty.place(relx=.5,rely=.35, anchor="center")
                #canvas1.create_window(200, 120, window=label4)

                #from tkinter import font as tkFont
                #helv20 = tkFont.Font(family='Helvetica', size=4, underline = True)
                dropnew_ty = OptionMenu(tab1, type_selection, "irri-6", "1121", "pk386","brown","super kernel basmati white","super kernel basmati brown","1121 sela")
                dropnew_ty.config(font=(mfont_family,15))
                menu = tab1.nametowidget(dropnew_ty.menuname)
                menu.config(font=(mfont_family,15,"underline"))  # Set the dropdown menu's font
                dropnew_ty.place(relx=.5,rely=.43, anchor="center")
                #canvas1.create_window(200,160, window=dropnew)


                # Closing the Canvas & executing functions in report file
                Edit_btnn = Button(tab1,text = "EDIT", command=profile_edit, width=17, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE, font=(mfont_family, '13'), takefocus=False) #take focus false will remove dashed line
                Edit_btnn.place(relx=.5,rely=.64, anchor="center")
                #canvas1.create_window(190, 250, window=myButton)
                ####


                #leena
                root_10g.protocol('WM_DELETE_WINDOW',show) #to perform functionality when close from title bar
                ###
            
                # Closing the Canvas & executing functions in report file
                myButton = Button(tab1,text = "SUBMIT", command=show, width=17, height=2, bd=2,  bg = "#62d18f", fg="black",
                                relief=GROOVE, font=(mfont_family, '13'), takefocus=False) #take focus false will remove dashed line
                myButton.place(relx=.5,rely=.75, anchor="center")
                #canvas1.create_window(190, 250, window=myButton)

                
                
                ###for user information form###
                background_image(tab2)
                
                x = datetime.now()
                print(x.strftime("%A"))
                self.window = tab2
##                self.window.title("Form")
##                self.window.geometry('600x670')
                self.title_lbl = Label(self.window, text="Sample Information",font=(mfont_family, 28),fg="#336699")
                self.title_lbl.place(x=150, y=0)

                self.sampleNo = Label(self.window, text="Sample No",font=("Helvetica", 12))
                self.sampleNo.place(x=80, y=105)
                self.entry_sampleNo = Entry(self.window, bd=2, width=40, highlightthickness=1,relief=RIDGE, highlightcolor= mustard_color)
                self.entry_sampleNo.place(x=250, y=100, height=35)

                self.lbl = Label(self.window, text="Date", font=("Helvetica", 12))
                self.lbl.place(x=80, y=155)
                self.txtfld = Entry(self.window, bd=2, width=40, highlightthickness=1,relief=RIDGE, highlightcolor= mustard_color)
                self.txtfld.place(x=250, y=150, height=35)
                self.txtfld.insert(0, x.strftime("%d/%m/%Y"))
                self.txtfld.config(disabledbackground="#d1d1d1", state=DISABLED)

                self.lbl1 = Label(self.window, text="Time", font=("Helvetica", 12))
                self.lbl1.place(x=80, y=205)
                self.txtfld1 = Entry(self.window, bd=2, width=40, highlightthickness=1,relief=RIDGE, highlightcolor= mustard_color)
                self.txtfld1.place(x=250, y=200, height=35)
                self.txtfld1.insert(0, x.strftime("%I:%M:%S %p"))
                self.txtfld1.config(disabledbackground="#d1d1d1", state=DISABLED)

                self.lbl2 = Label(self.window, text="Arrival Number", font=("Helvetica", 12))
                self.lbl2.place(x=80, y=255)
                self.txtfld2 = Entry(self.window, bd=2, width=40, highlightthickness=1,relief=RIDGE, highlightcolor= mustard_color)
                self.txtfld2.place(x=250, y=250, height=35)

                self.lbl3 = Label(self.window, text="Party Name", font=("Helvetica", 12))
                self.lbl3.place(x=80, y=305)
                self.txtfld3 = Entry(self.window, bd=2, width=40, highlightthickness=1,relief=RIDGE, highlightcolor= mustard_color)
                self.txtfld3.place(x=250, y=300, height=35)

                self.lbl4 = Label(self.window, text="Vehicle Number", font=("Helvetica", 12))
                self.lbl4.place(x=80, y=355)
                self.txtfld4 = Entry(self.window, bd=2, width=40, highlightthickness=1,relief=RIDGE, highlightcolor= mustard_color)
                self.txtfld4.place(x=250, y=350, height=35)

                self.riceType = Label(self.window, text="Rice Type", font=("Helvetica", 12))
                self.riceType.place(x=80, y=405)
                self.entry_riceType = Entry(self.window, bd=2, width=40, highlightthickness=1,relief=RIDGE, highlightcolor= mustard_color)
                self.entry_riceType.place(x=250, y=400, height=35)

                self.lbl5 = Label(self.window, text="Moisture", font=("Helvetica", 12))
                self.lbl5.place(x=80, y=455)
                self.txtfld5 = Entry(self.window, bd=2, width=40, highlightthickness=1,relief=RIDGE, highlightcolor= mustard_color)
                self.txtfld5.place(x=250, y=450, height=35)

                self.lbl6 = Label(self.window, text="Look", font=("Helvetica", 12))
                self.lbl6.place(x=80, y=505)
                self.txtfld6 = Entry(self.window, bd=2, width=40, highlightthickness=1,relief=RIDGE, highlightcolor= mustard_color)
                self.txtfld6.place(x=250, y=500, height=35)

                ok_btn = Button(self.window, text="SUBMIT", width=20, height=2, command=show, bd=2, highlightcolor='grey48',  bg = "#62d18f", fg="black",
                        relief=GROOVE)
                ok_btn.place(x=230, y=555)

                cancel_btn = Button(self.window, text="CANCEL", width=20, command=window_close,height=2, bd=2, bg= "#aaadaa", fg="black",
                            highlightcolor='grey48',relief=GROOVE)
                cancel_btn.place(x=230, y=605)

                root_10g.protocol('WM_DELETE_WINDOW',window_close) #to perform functionality when user close from title bar
                ####user information form ends here
                

##                # on change dropdown value
##                def change_dropdown(*args):
##                    print( clicked.get() )
##
                def change_dropdownnew(*args):
                    print( clickednew.get() )
##
##                #link function to change dropdown
##                #clicked.trace('w', change_dropdown)
                #clickednew.trace('w', change_dropdownnew)

                root_10g.mainloop()
                
            else:
                tkinter.messagebox.showwarning("Reset","Please click on Reset Button.")
                
        
        
        def resize_image(event):
            new_width = event.width
            new_height = event.height
            image = copy_of_image.resize((new_width, 120))
            photo = ImageTk.PhotoImage(image)
            label.config(image = photo)
            label.image = photo #avoid garbage collection

        tk.Frame.__init__(self,parent, bg =  "#2D2D2D")
        image = Image.open("img/cv3.jpg")
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo)
        label.bind('<Configure>', resize_image)
        label.image = photo # keep a reference!
        label.pack(side="top" ,padx=0, pady=0)

        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.BOTH, side="top")
        
        image1 = Image.open("img/line.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="top" ,padx=0, pady=0)

 
        image1 = Image.open("img/pi38.jpg")
        image1 = image1.resize((Image_screen_width, Image_screen_height), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="left" ,padx=0, pady=0, fill=BOTH)
        
        ###################################################################
        # Scanning function Definition
        ###################################################################

        def Scan_Image():

            def scan_loading_func():
            
                #disable all button when it is processing
                Sample_button["state"] = "disabled"
                First_test["state"] = "disabled"
                Select_type["state"] = "disabled"
                Select_button["state"] = "disabled"
                Scan_button["state"] = "disabled"
                Repor_button["state"] = "disabled"
                DRepor_button["state"] = "disabled"
                Display_button["state"] = "disabled"
                #pieChart_button["state"] = "disabled"
                Reset_button["state"] = "disabled"
                #####
                
                global prog_bar
                global top_progBar
                top_progBar = Toplevel()

                #these two lines of code are to bring on top this progress bar
                top_progBar.lift()
                top_progBar.attributes("-topmost",True)

                center_widget(360,100)
                top_progBar.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
                top_progBar.title("Loading..")

                prog_bar = ttk.Progressbar(top_progBar,
                                            orient="horizontal",
                                            length=500, mode = "indeterminate")
                prog_bar.pack(side=tk.TOP, pady=8)
                global wait_label
                wait_label = Label(top_progBar, text = "Processing, please wait..", font = ("Arial",13))
                wait_label.pack()
                prog_bar.start()

          
            
            def scan_processing():

                #try:

                #these below lines are necessary for threading operation
                
                import pythoncom
                pythoncom.CoInitialize()
            ###
            
            #try:
            #statusbar['text'] ="Scanning Image"
                global rice_image
                global objects
            
            #Ahsan adding pop up in scanning
            
            #tkinter.messagebox.showinfo("Loading","Please wait..")
                # try:
                wia_dev_manager = Dispatch("WIA.DeviceManager")
                for ix, device in enumerate(wia_dev_manager.DeviceInfos):
                    print(ix,"|",device.Properties("Name").Value,"|",device.DeviceID)
                    
                    #
                    # 0 | Lexmark Pro200-S500 Series | {6BDD1FC6-810F-11D0-BEC7-08002BE2092F}\0000
                    #
    
                # Select a device per gui if there are more than one device
                wia = Dispatch("WIA.CommonDialog")
            
                
                dev = wia.ShowSelectDevice()
                dev.Properties("Name").Value
                # 'Lexmark Pro200-S500 Series'
                
                # List Items of device
                for ix, item in enumerate(dev.Items):
                    print(ix,item.ItemID)
    
                # Select per number 
                scanner = dev.Items[1]
                scanner.ItemID
                # '0000\\Root\\Flatbed'
            
    
                # Set resolution
                scanner.Properties("Vertical Resolution").Value   = 300
                scanner.Properties("Horizontal Resolution").Value = 300

            
                WIA_IMG_FORMAT_PNG       = "{B96B3CAF-0728-11D3-9D7B-0000F81EF32E}"
                image=scanner.Transfer(WIA_IMG_FORMAT_PNG)
                
                a=str(random.randint(1,1000))
                our_path = get_currentDir()
                filename= str(our_path + '\\scan_'+a)
                image.SaveFile(filename+".png")
            
                im = Image.open(filename + '.png')
                im.save(filename + '.jpg')


                #leena
                #our_path = get_currentDir()
                path = str(our_path+'\\scan_'+a+'.png')
                rice_image = cv2.imread(path)
                
                globals.browse_image=1

                #leena
                globals.S_Report = get_nonexistant_path(our_path +'\\'+"Summarized Report.pdf")
                globals.D_Report = get_nonexistant_path(our_path +'\\'+"Detailed Report.pdf")  
                ####
                #import report
                #import reportnew

                if globals.rice_type_selected == "irri-6":
                    t1_start = time.time()
                    objects=analysis_irri6.analyze(rice_image, globals.D_Report)
                    t1_stop = time.time()
                    print("The Total time of Analysis: ", 
                                         t1_stop-t1_start)
                    t1_start = time.time()
                    report.gen_report_irri6(objects,globals.S_Report)
                    t1_stop = time.time()
                    print("The Total time of Report : ", 
                                         t1_stop-t1_start)
                elif globals.rice_type_selected == "1121":
                    objects=analysis_1121.analyze(rice_image, globals.D_Report)
                    report.gen_report_1121(objects,globals.S_Report)
                elif globals.rice_type_selected == "pk386":
                    objects=analysis_pk386.analyze(rice_image, globals.D_Report)
                    report.gen_report_pk386(objects,globals.S_Report)

                elif globals.rice_type_selected == "brown":
                    objects=analysis_brown.analyze(rice_image, globals.D_Report)
                    report.gen_report_brown(objects,globals.S_Report)

                elif globals.rice_type_selected == "super kernel basmati white":
                    objects=analysis_super_kernel_basmati_white.analyze(rice_image, globals.D_Report)
                    report.gen_report_super_kernel_basmati_white(objects,globals.S_Report)
                
                elif globals.rice_type_selected == "super kernel basmati brown":
                    objects=analysis_super_kernel_basmati_brown.analyze(rice_image, globals.D_Report)
                    report.gen_report_super_kernel_basmati_brown(objects,globals.S_Report)

                elif globals.rice_type_selected == "1121 sela":
                    objects=analysis_1121_sela.analyze(rice_image, globals.D_Report)
                    report.gen_report_1121_sela(objects,globals.S_Report)
                os.remove(path)

                merge_pdf()
                
                from report import ldata, cdata, tdata, Date, Time
                print(report.ldata,report.cdata,report.tdata)                

                statusbar['text'] ="Processing Completed"
                    
                stop=prog_bar.stop()
                if stop is None:
                
                    top_progBar.destroy()

                    #enable all buttons when the processing is completed
                    Sample_button["state"] = "active"
                    First_test["state"] = "normal"
                    Select_type["state"] = "normal"
                    Select_button["state"] = "normal"
                    Scan_button["state"] = "normal"
                    Repor_button["state"] = "active"
                    DRepor_button["state"] = "active"
                    Display_button["state"] = "normal"
                    #pieChart_button["state"] = "normal"
                    Reset_button["state"] = "normal"
                    ###

                    globals.need_to_reset=1
                    
                    tkinter.messagebox.showinfo("Processing Completed","Please click on View Sample Tab to see results.")
                    
                # except:
                #     print("condition true")
                #     stop=prog_bar.stop()
                #     if stop is None:
                    
                #         top_progBar.destroy()

                #         #enable all buttons when the processing is completed
                #         Sample_button["state"] = "active"
                #         First_test["state"] = "normal"
                #         Select_type["state"] = "normal"
                #         Select_button["state"] = "normal"
                #         Scan_button["state"] = "normal"
                #         Repor_button["state"] = "active"
                #         DRepor_button["state"] = "active"
                #         Display_button["state"] = "normal"
                #         #pieChart_button["state"] = "normal"
                #         Reset_button["state"] = "normal"
                #         ###

                #         globals.need_to_reset=1
                        
                #     tkinter.messagebox.showerror("Failed Test","Try the following methods \n 1. Please separate all rice on scanner properly \n 2. Please check if the scanner is connected \n 3. Please check if the scanner lid is closed \n 4. Restart the system")
                    
            
            if globals.direct_clicked is 1 and globals.need_to_reset is not 1:
                
                threading.Thread(target=scan_processing).start()
                threading.Thread(target=scan_loading_func).start()


            else:
                tkinter.messagebox.showerror("Test Sample Failed","There is no entry in 10g Sample Test.\n Please click on 10g Grain Test")
            

        ###################################################################
        #Select Image from Directory Function
        ###################################################################

        def select_image():
           
#            try:

            if globals.direct_clicked is 1 and globals.need_to_reset is not 1:

                statusbar['text'] ="Selecting Image"
                # open a file chooser dialog and allow the user to select an input image
                
                path = filedialog.askopenfilename()

                #leena
                globals.browse_image=0 #if the browse image is not selected 
                ##

             ######leenaaaa########        
                def processing(path):
                    global rice_image
                    global objects
                    # import report
                    rice_image = cv2.imread(path)
                    statusbar['text'] ="Processing Image"
                    #rice_image = cv2.resize(rice_image, (2466,2650), interpolation = cv2.INTER_AREA)
                    t1_start = process_time()
                    #p = Pool()
                    
                    pool = ThreadPool(processes=6)
                    
                    if globals.rice_type_selected == "irri-6":
                         async_result = pool.apply_async(analysis_irri6.analyze, (rice_image,globals.D_Report)) # tuple of args for foo
                    elif globals.rice_type_selected == "1121":
                        async_result = pool.apply_async(analysis_1121.analyze, (rice_image,globals.D_Report))
                    elif globals.rice_type_selected == "pk386":
                        async_result = pool.apply_async(analysis_pk386.analyze, (rice_image,globals.D_Report))
                    elif globals.rice_type_selected == "brown":
                        async_result = pool.apply_async(analysis_brown.analyze, (rice_image,globals.D_Report))
                    elif globals.rice_type_selected == "super kernel basmati white":
                        async_result = pool.apply_async(analysis_super_kernel_basmati_white.analyze, (rice_image,globals.D_Report))
                    elif globals.rice_type_selected == "super kernel basmati brown":
                        async_result = pool.apply_async(analysis_super_kernel_basmati_brown.analyze, (rice_image,globals.D_Report))
                    elif globals.rice_type_selected == "1121 sela":
                        async_result = pool.apply_async(analysis_1121_sela.analyze, (rice_image,globals.D_Report))

                    objects = async_result.get()
                    
                    
                    #objects = analysis.analyze(rice_image,globals.D_Report)
                    #objects = p.map(analysis.analyze,rice_image,globals.D_Report)
                    t1_stop = process_time()
                    print("Elapsed time:", t1_stop, t1_start)
                    print("Elapsed time during the ANALYSIS program in seconds:", 
                                         t1_stop-t1_start)
                    if globals.rice_type_selected == "irri-6":
                        report.gen_report_irri6(objects,globals.S_Report)
                    elif globals.rice_type_selected == "1121":
                        report.gen_report_1121(objects,globals.S_Report)
                    elif globals.rice_type_selected == "pk386":
                        report.gen_report_pk386(objects,globals.S_Report)
                    elif globals.rice_type_selected == "brown":
                        report.gen_report_brown(objects,globals.S_Report)
                    elif globals.rice_type_selected == "super kernel basmati white":
                        report.gen_report_super_kernel_basmati_white(objects,globals.S_Report)
                    elif globals.rice_type_selected == "super kernel basmati brown":
                        report.gen_report_super_kernel_basmati_brown(objects,globals.S_Report)
                    elif globals.rice_type_selected == "1121 sela":
                        report.gen_report_1121_sela(objects,globals.S_Report)

                    merge_pdf()
                    from report import ldata, cdata, tdata, Date, Time
                    print(report.ldata,report.cdata,report.tdata)

                    stop=prog_bar.stop()
                    if stop is None:
                        #wait_label.destroy()
                        top_progBar.destroy()

                        #enable all buttons when the processing is completed
                        Sample_button["state"] = "active"
                        First_test["state"] = "normal"
                        Select_type["state"] = "normal"
                        Select_button["state"] = "normal"
                        Scan_button["state"] = "normal"
                        Repor_button["state"] = "active"
                        DRepor_button["state"] = "active"
                        Display_button["state"] = "normal"
                        #pieChart_button["state"] = "normal"
                        Reset_button["state"] = "normal"
                        ###

                        globals.need_to_reset=1
                        
                        tkinter.messagebox.showinfo("Processing Completed","Please click on View Sample Tab to see results.")

               
    
                def loading_func():

                    #disable all button when it is processing
                    Sample_button["state"] = "disabled"
                    First_test["state"] = "disabled"
                    Select_type["state"] = "disabled"
                    Select_button["state"] = "disabled"
                    Scan_button["state"] = "disabled"
                    Repor_button["state"] = "disabled"
                    DRepor_button["state"] = "disabled"
                    Display_button["state"] = "disabled"
                    #pieChart_button["state"] = "disabled"
                    Reset_button["state"] = "disabled"
                    #####
                    
                    global prog_bar
                    global top_progBar
                    top_progBar = Toplevel()
                    center_widget(360,100)
                    top_progBar.resizable(0, 0)
                    top_progBar.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
                    #top_progBar.geometry("360x100")
                    top_progBar.title("Loading..")

                    prog_bar = ttk.Progressbar(top_progBar,
                                               orient="horizontal",
                                               length=500, mode = "indeterminate")
                    prog_bar.pack(side=tk.TOP, pady=8)
                    global wait_label
                    wait_label = Label(top_progBar, text = "Processing, please wait..", font = ("Arial",13))
                    wait_label.pack()
                    prog_bar.start()
                    
               #####################
                
                if len(path) > 0:

                    #leena
                    global our_path
                    our_path= get_currentDir()
                    globals.S_Report = get_nonexistant_path(our_path +'\\'+"Summarized Report.pdf")
                    globals.D_Report = get_nonexistant_path(our_path +'\\'+"Detailed Report.pdf")
                    #DetailReport = globals.D_Report
                    
                    #leena
                    globals.browse_image=1 #if browse image is selected
                    ##
   
                    #leena
                    threading.Thread(target=processing,args=(path,)).start()
                    threading.Thread(target=loading_func).start()
                    ####
         
                
                statusbar['text'] ="Processing Completed"

            else:
                tkinter.messagebox.showerror("Test Sample Failed","There is no entry in 10g Sample Test.\n Please click on 10g Grain Test")
            
        self.image_g = tk.PhotoImage(file="img/grain.png")
        First_test = ttk.Button(button_frame, text="100g Grain Test" ,
        image=self.image_g, compound="left",command=first_test)
        
        
        self.image_b = tk.PhotoImage(file="img/type.png")
        Select_type = ttk.Button(button_frame, text="10g Grain Test", 
                                   image=self.image_b, compound="left",
                                   command=select_type)
            
        # initialize the window toolkit along with the two image panels
        self.image_t = tk.PhotoImage(file="img/iconb.png")
        Select_button = ttk.Button(button_frame, text="Browse Image", 
                                   image=self.image_t, compound="left",
                                   command=select_image)    


        self.image_v = tk.PhotoImage(file="img/iconv.png")
        Sample_button = ttk.Button(button_frame,text="View Sample", 
                                   image=self.image_v, compound="left", 
                                   command=lambda: controller.show_frame(Sample))

        self.image_a = tk.PhotoImage(file="img/icona.png")
        Analyses_button = ttk.Button(button_frame, text="Analyses",
                                     image=self.image_a, compound="left",
                                     command=lambda: controller.show_frame(LGraph))

        self.image_r = tk.PhotoImage(file="img/iconr.png")
        Repor_button = ttk.Button(button_frame, text="Summarized Report",
                                  image=self.image_r, compound="left",
                                  command= pdf_view)
        
        self.image_dr = tk.PhotoImage(file="img/detailed.png")
        DRepor_button = ttk.Button(button_frame, text="Detailed Report",
                                  image=self.image_dr, compound="left",
                                  command= pdf1_view)
        
        self.image_s = tk.PhotoImage(file="img/iconss.png")
        Scan_button = ttk.Button(button_frame, text="Scan Image",
                                 image=self.image_s, compound="left",
                                 command=Scan_Image)

        self.display_icon = tk.PhotoImage(file="img/display.png")
        Display_button = ttk.Button(button_frame, text="Display All",image=self.display_icon, compound="left",command=Display)


        self.reset_icon = tk.PhotoImage(file="img/reset.png")
        Reset_button = ttk.Button(button_frame, text="Reset",
                                 image=self.reset_icon, compound="left",
                                 command=reset_button)


        
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)
        button_frame.columnconfigure(6, weight=1)
        button_frame.columnconfigure(7, weight=1)
        button_frame.columnconfigure(8, weight=1)
      
        First_test.grid(row=2, column=0, sticky=tk.W+tk.E)
        Select_type.grid(row=2, column=1, sticky=tk.W+tk.E)
        Select_button.grid(row=2, column=2, sticky=tk.W+tk.E)
        #Capture_button.grid(row=2, column=3, sticky=tk.W+tk.E)
        Scan_button.grid(row=2, column=3, sticky=tk.W+tk.E) #4
        Sample_button.grid(row=2, column=4, sticky=tk.W+tk.E) #5
        Repor_button.grid(row=2, column=5, sticky=tk.W+tk.E) #7
        DRepor_button.grid(row=2, column=6, sticky=tk.W+tk.E) #8
        Display_button.grid(row=2, column=7, sticky=tk.W+tk.E)
        Reset_button.grid(row=2, column=8, sticky=tk.W+tk.E)
       

        
        
    ###################################################################
    ###################################################################
            
    def updateFrame(self):
        print('Sample')
        #print("Objects",objects)


############################ For display Tab ###########################################
def myfunc():
    print('Function created')
#leena
def Display():
    from pandas import DataFrame
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    
    print('Function created')
    root = Tk()
    root.state('zoomed')
    #root.geometry('1200x600')
    # root.resizable(0, 0)
    root.title("Display Window")
    root.config(bg='#336699')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    
    #these None are for to check if they doesn't exists then don't show them 
    canvas=None
    btn_all=None
    yellow=None
    damage=None
    paddy = None
    chalky=None
    vsb=None
    hsb=None
    label_error=None
    #self.nback=None


    def ss():
        win = FindWindow(None, "Display Window")
        rect = GetWindowRect(win)
        list_rect = list(rect)
        list_frame = [8, -5, 8, 8]  # change -5 to -8 to not capture the titlebar
        final_rect = tuple((map(lambda x, y: x - y, list_rect, list_frame)))  # subtracting two lists
        print(rect)
        print(list_rect)
        print(final_rect)
        img = ImageGrab.grab(bbox=final_rect)
        img.save('Image.jpg')

    def my_all():
        nonlocal All
        nonlocal frame_all
        nonlocal frame_yellow
        nonlocal frame_damage
        nonlocal frame_chalky
        nonlocal frame_paddy

        nonlocal vsb, hsb
        nonlocal canvas

        btn_all.configure(bg=mustard_color)
        yellow.configure(background=orig_color)
        damage.configure(background=orig_color)
        chalky.configure(background=orig_color)
        paddy1.configure(background=orig_color)

        i = 0
        columns = 15
        all_count = 0
        if frame_all is not None:
            frame_all.destroy()
            frame_yellow.destroy()
            frame_damage.destroy()
            frame_paddy.destroy()
            frame_chalky.destroy()
            frame_all = Frame(canvas)
            frame_all.grid(row=0, column=0, sticky="news")
            canvas.create_window((0, 0), window=frame_all, anchor="nw")
            frame_all.grid_columnconfigure(0, weight=1)
            frame_all.grid_rowconfigure(0, weight=1)
            
        if len(All) == 0:
            label_error = Label(frame_all, foreground="black", background="azure", text="No Rice",
                                relief=RAISED, font=("Courier", 44))
            label_error.grid(row=0, column=0)
            
        for name in All:
            i += 1
            all_count += 1
            r, c = divmod(all_count - 1, columns)
            current_path = os.getcwd() # to get the current directory path
            im = Image.open(current_path+"\\scan_copy\\" + str(name))
            resized = im.resize((columns * 5, columns * 8), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(resized, master=canvas)
            myvar = Label(frame_all, text='All' + str(i), image=tkimage, compound='top')
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
            root.update()
            canvas.config(bg='white', yscrollcommand=vsb.set, xscrollcommand=hsb.set,
                          scrollregion=frame_all.bbox(ALL))

        root.mainloop()
        
    def yellow():
        nonlocal Yellow
        nonlocal frame_all
        nonlocal frame_yellow
        nonlocal frame_damage
        nonlocal frame_chalky
        nonlocal frame_paddy

        nonlocal vsb, hsb
        nonlocal canvas

        yellow.configure(bg=mustard_color)
        btn_all.configure(background=orig_color)
        damage.configure(background=orig_color)
        chalky.configure(background=orig_color)
        paddy1.configure(background=orig_color)
        
        columns = 15
        image_count = 0
        i = 0
        if frame_yellow is not None:
            frame_yellow.destroy()
            frame_damage.destroy()
            frame_paddy.destroy()
            frame_all.destroy()
            frame_chalky.destroy()
            frame_yellow = Frame(canvas)
            frame_yellow.grid(row=0, column=0, sticky="news")
            canvas.create_window((0, 0), window=frame_yellow, anchor="nw")
            frame_yellow.grid_columnconfigure(0, weight=1)
            frame_yellow.grid_rowconfigure(0, weight=1)
            
        if len(Yellow) == 0:
            label_error = Label(frame_yellow, foreground="black", background="azure", text="No Yellow Rice",
                                relief=RAISED, font=("Courier", 44))
            label_error.grid(row=0, column=0)
            
        for name in Yellow:
            i += 1
            image_count += 1
            r, c = divmod(image_count - 1, columns)
            current_path = os.getcwd() # to get the current directory path
            im = Image.open(current_path+"\\scan_copy\\" + str(name))
            resized = im.resize((columns * 5, columns * 8), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(resized, master=canvas)
            myvar = Label(frame_yellow, text='Yellow/Red' + str(i), image=tkimage, compound='top')
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
            root.update()
            canvas.config(bg='white',yscrollcommand=vsb.set, xscrollcommand=hsb.set,
                          scrollregion=frame_yellow.bbox(ALL))

        root.mainloop()

    def damage():
        nonlocal damages
        nonlocal frame_all
        nonlocal frame_yellow
        nonlocal frame_damage
        nonlocal frame_chalky
        nonlocal frame_paddy

        nonlocal vsb, hsb
        nonlocal canvas

        damage.configure(bg=mustard_color)
        btn_all.configure(background=orig_color)
        yellow.configure(background=orig_color)
        chalky.configure(background=orig_color)
        paddy1.configure(background=orig_color)
        
        i = 0
        columns = 15
        damage_count = 0
        if frame_damage is not None:
            frame_damage.destroy()
            frame_yellow.destroy()
            frame_paddy.destroy()
            frame_all.destroy()
            frame_chalky.destroy()

            frame_damage = Frame(canvas)
            frame_damage.grid(row=0, column=0, sticky="news")
            canvas.create_window((0, 0), window=frame_damage, anchor="nw")
            frame_damage.grid_columnconfigure(0, weight=1)
            frame_damage.grid_rowconfigure(0, weight=1)

        if len(damages) == 0:
            label_error = Label(frame_damage, foreground="black", background="azure", text="No Damage Rice",
                                relief=RAISED, font=("Courier", 44))
            label_error.grid(row=0, column=0)
            
        for name in damages:
            i += 1
            damage_count += 1
            r, c = divmod(damage_count - 1, columns)
            current_path = os.getcwd() # to get the current directory path
            im = Image.open(current_path+"\\scan_copy\\" + str(name))
            resized = im.resize((columns * 5, columns * 8), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(resized, master=canvas)
            myvar = Label(frame_damage, text='Damage' + str(i), image=tkimage, compound='top')
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
            root.update()

            canvas.config(bg='white', yscrollcommand=vsb.set, xscrollcommand=hsb.set,
                          scrollregion=canvas.bbox(ALL))

        root.mainloop()

    def chalky():
        nonlocal Chalky
        nonlocal frame_all
        nonlocal frame_yellow
        nonlocal frame_damage
        nonlocal frame_chalky
        nonlocal frame_paddy

        nonlocal vsb, hsb
        nonlocal canvas

        chalky.configure(bg=mustard_color)
        btn_all.configure(background=orig_color)
        yellow.configure(background=orig_color)
        damage.configure(background=orig_color)
        paddy1.configure(background=orig_color)
        
        i = 0
        columns = 15
        chalky_count = 0
        if frame_chalky is not None:
            frame_chalky.destroy()
            frame_yellow.destroy()
            frame_all.destroy()
            frame_paddy.destroy()
            frame_damage.destroy()
            frame_chalky = Frame(canvas)
            frame_chalky.grid(row=0, column=0, sticky="news")
            canvas.create_window((0, 0), window=frame_chalky, anchor="nw")
            frame_chalky.grid_columnconfigure(0, weight=1)
            frame_chalky.grid_rowconfigure(0, weight=1)

        if len(Chalky) == 0:
            label_error = Label(frame_chalky, foreground="black", background="azure", text="No Chalky Rice",
                                relief=RAISED, font=("Courier", 44))
            label_error.grid(row=0, column=0)
            
        for name in Chalky:
            i += 1
            chalky_count += 1
            r, c = divmod(chalky_count - 1, columns)
            current_path = os.getcwd() # to get the current directory path
            im = Image.open(current_path+"\\scan_copy\\" + str(name))
            resized = im.resize((columns * 5, columns * 8), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(resized, master=canvas)
            myvar = Label(frame_chalky, text='Chalky/Green' + str(i), image=tkimage, compound='top')
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
            root.update()
            canvas.config(bg='white', yscrollcommand=vsb.set, xscrollcommand=hsb.set,
                          scrollregion=frame_chalky.bbox(ALL))
        root.mainloop()
    
    def Paddy():
        nonlocal paddy
        nonlocal frame_all
        nonlocal frame_yellow
        nonlocal frame_damage
        nonlocal frame_chalky
        nonlocal frame_paddy

        nonlocal vsb, hsb
        nonlocal canvas

        paddy1.configure(bg=mustard_color)
        btn_all.configure(background=orig_color)
        yellow.configure(background=orig_color)
        damage.configure(background=orig_color)
        chalky.configure(background=orig_color)
        
        i = 0
        columns = 15
        paddy_count = 0
        if frame_paddy is not None:
            frame_chalky.destroy()
            frame_yellow.destroy()
            frame_paddy.destroy()
            frame_all.destroy()
            frame_damage.destroy()
            frame_paddy = Frame(canvas)
            frame_paddy.grid(row=0, column=0, sticky="news")
            canvas.create_window((0, 0), window=frame_paddy, anchor="nw")
            frame_paddy.grid_columnconfigure(0, weight=1)
            frame_paddy.grid_rowconfigure(0, weight=1)
            
        if len(paddy) == 0:
            label_error = Label(frame_paddy, foreground="black", background="azure", text="No Paddy Rice",
                                relief=RAISED, font=("Courier", 44))
            label_error.grid(row=0, column=0)
            
        for name in paddy:
            i += 1
            paddy_count += 1
            r, c = divmod(paddy_count - 1, columns)
            current_path = os.getcwd() # to get the current directory path
            im = Image.open(current_path+"\\paddy\\" + str(name))
            resized = im.resize((columns * 5, columns * 8), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(resized, master=canvas)
            myvar = Label(frame_paddy, text='Paddy' + str(i), image=tkimage, compound='top')
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
            root.update()
            canvas.config(bg='white', yscrollcommand=vsb.set, xscrollcommand=hsb.set,
                          scrollregion=frame_paddy.bbox(ALL))
        root.mainloop()


    current_path = os.getcwd()
    if os.path.exists(current_path+"\\scan_copy"):
        if globals.rice_type_selected == "irri-6":
            from analysis_irri6 import yellow_filename , new_damage1_name, chalky_name, paddy_name
        elif globals.rice_type_selected == "1121":
            from analysis_1121 import yellow_filename , new_damage1_name, chalky_name, paddy_name
        elif globals.rice_type_selected == "pk386":
            from analysis_pk386 import yellow_filename , new_damage1_name, chalky_name, paddy_name
        elif globals.rice_type_selected == "brown":
            from analysis_brown import yellow_filename , new_damage1_name, chalky_name, paddy_name

        elif globals.rice_type_selected == "super kernel basmati white":
            from analysis_super_kernel_basmati_white import yellow_filename , new_damage1_name, chalky_name, paddy_name

        elif globals.rice_type_selected == "super kernel basmati brown":
            from analysis_super_kernel_basmati_brown import yellow_filename , new_damage1_name, chalky_name, paddy_name
        elif globals.rice_type_selected == "1121 sela":
            from analysis_1121_sela import yellow_filename , new_damage1_name, chalky_name, paddy_name
        All = os.listdir(current_path+"\\scan_copy")
        Yellow = yellow_filename
        damages = new_damage1_name
        Chalky = chalky_name
        paddy = paddy_name
        #check if the error message appears then destroy it
    #    this situation is true when first clicked on display button and then tested sample and then again clicked on display button
        if label_error is not None:
            label_error.destroy()
    #             self.nback.destroy()
        canvas = Canvas(root, bg='grey48', relief=SUNKEN)
        canvas.grid(row=0, column=0, sticky="news")
        frame_all = Frame(canvas)
        frame_all.grid(row=0, column=0, sticky="news")
        canvas.create_window((0, 0), window=frame_all, anchor="nw")
        frame_yellow = Frame(canvas)
        frame_yellow.grid(row=0, column=0, sticky="news")
        canvas.create_window((0, 0), window=frame_yellow, anchor="nw")
        frame_damage = Frame(canvas)
        frame_damage.grid(row=0, column=0, sticky="news")
        canvas.create_window((0, 0), window=frame_damage, anchor="nw")
        frame_chalky = Frame(canvas)
        frame_chalky.grid(row=0, column=0, sticky="news")
        canvas.create_window((0, 0), window=frame_chalky, anchor="nw")
        frame_paddy = Frame(canvas)
        frame_paddy.grid(row=0, column=0, sticky="news")
        canvas.create_window((0, 0), window=frame_paddy, anchor="nw")
        canvas.grid_columnconfigure(0, weight=1)
        frame_all.grid_columnconfigure(0, weight=1)
        frame_yellow.grid_columnconfigure(0, weight=1)
        frame_damage.grid_columnconfigure(0, weight=1)
        frame_chalky.grid_columnconfigure(0, weight=1)
        canvas.grid_rowconfigure(0, weight=1)
        frame_all.grid_rowconfigure(0, weight=1)
        frame_yellow.grid_rowconfigure(0, weight=1)
        frame_damage.grid_rowconfigure(0, weight=1)
        frame_chalky.grid_rowconfigure(0, weight=1)
        frame_paddy.grid_columnconfigure(0, weight=1)
        frame_paddy.grid_rowconfigure(0, weight=1)




        #background image
        im = Image.open("img/rice_bg.jpg")
        filename = ImageTk.PhotoImage(im, master= root)
        background_label = Label(root, image=filename)
        background_label.grid(row=0, column=2, sticky="nsew")
        background_label.image = filename

##        canvas = Canvas(background_label, bg="black", width=700, height=400)
##        canvas.pack()

##        im = Image.open("img/image3.png")
##        photo1 = ImageTk.PhotoImage(image="img/image3.png")
##        canvas.create_image(200,200,image=photo1)
##        canvas.photo1 = photo1


        im = Image.open("img/icon1.ico")
        #resized = im.resize((int(self.screen_width/1.7),int(self.screen_height)), Image.ANTIALIAS)#1.7
        resized = im.resize((int(100),int(100)), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized, master=background_label)
        label1 = Label(background_label, image=tkimage)
        label1.image = tkimage
        label1.grid(row=0, column=2, sticky="nw", padx=90, pady=5)
        #label1.place(relx=.7,rely=.45, anchor="center")
        
        vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        hsb = Scrollbar(root, orient="horizontal", command=canvas.xview)
        hsb.grid(row=1, column=0, sticky="wes")
        
        btn_all = Button(background_label, text="ALL", width=20, command=my_all, height=2, bd=2, highlightcolor='grey48',
                 relief=GROOVE)
        btn_all.grid(row=0, column=2, sticky="nw", padx=80, pady=150)
        yellow = Button(background_label, text="Yellow/Red", command=yellow, width=20, height=2, bd=2, relief=GROOVE)
        yellow.grid(row=0, column=2, sticky="nw", padx=80, pady=200)
        chalky = Button(background_label, text="Chalky/Green ", command=chalky, width=20, height=2, bd=2, relief=GROOVE)
        chalky.grid(row=0, column=2, sticky="nw", padx=80, pady=250)
        damage = Button(background_label, text="Damage", command=damage, width=20, height=2, bd=2, relief=GROOVE)
        damage.grid(row=0, column=2, sticky="nw", padx=80, pady=300)
        paddy1 = Button(background_label, text="Paddy ", command=Paddy, width=20, height=2, bd=2, relief=GROOVE)
        paddy1.grid(row=0, column=2, sticky="nw", padx=80, pady=350)


##        image_screenshot= PhotoImage(file='img/iconc.png')
##
##        img_label= Label(image=image_screenshot)
##        
##        btn_screenshot = Button(background_label, image=img_label, command=ss)
##        btn_screenshot.grid(row=0, column=2, sticky="nw", padx=80, pady=300)

            
        
        orig_color = paddy1.cget("background")

        from tkinter.ttk import Progressbar, Style
        if globals.chart_condition == 1:
            paddy_percentage = reportnew.paddy_percentage
            damage_percentage = reportnew.damage_percentage
            chalky_percentage = reportnew.chalky_percentage
            yellow_percentage = reportnew.yellow_percentage
        else:
            paddy_percentage = report.paddy_percentage
            damage_percentage = report.damage_percentage
            chalky_percentage = report.chalky_percentage
            yellow_percentage = report.yellow_percentage
            
        s3 = Style(background_label)
        # add the label to the progressbar style
        s3.layout("LabeledProgressbar3",
                 [('LabeledProgressbar3.trough',
                   {'children': [('LabeledProgressbar3.pbar',
                                  {'side': 'left', 'sticky': 'ns'}),
                                 ("LabeledProgressbar3.label",  # label inside the bar
                                  {"sticky": ""})],
                    'sticky': 'nswe'})])
        # self.myvar1 = Label(root, text='Yellow', bg='#336699')
        # self.myvar1.grid(row=1, column=2, sticky="s", pady=0)
        progress3 = Progressbar(background_label, orient=HORIZONTAL, length=200, mode='determinate',
                               style="LabeledProgressbar3")
        progress3['value'] = (len(paddy) / len(All)) * 100
        background_label.update_idletasks()
        progress3.grid(row=0, column=2, sticky="s", pady=100)
        s3.configure("LabeledProgressbar3",thickness=20,  text='Paddy ' + str(round((paddy_percentage*100),3)) + ' %',
                    troughcolor='#d1d1d1', background='blue', relief=RIDGE, height=4, bd=5, font=('Berlin Sans FB', 13))


        
        # self.myvar2 = Label(root, text='Allienviemnviermoiejfioer', bg='#336699')
        # self.myvar2.grid(row=0, column=2, sticky="s", pady=0)
        s1 = Style(background_label)
        # add the label to the progressbar style
        s1.layout("LabeledProgressbar1",
                  [('LabeledProgressbar1.trough',
                    {'children': [('LabeledProgressbar1.pbar',
                                   {'side': 'left', 'sticky': 'ns'}),
                                  ("LabeledProgressbar1.label",  # label inside the bar
                                   {"sticky": ""})],
                     'sticky': 'nswe'})])
        progress1 = Progressbar(background_label, orient=HORIZONTAL, length=200, mode='determinate',
                                style="LabeledProgressbar1")
        progress1['value'] = (len(damages) / len(All)) * 100
        background_label.update_idletasks()
        progress1.grid(row=0, column=2, sticky="s", pady=150)
        s1.configure("LabeledProgressbar1",thickness=20, 
                     text='Damage ' + str(round((damage_percentage*100),3))+ ' %',
                     troughcolor='#d1d1d1', background='brown', relief=RIDGE, height=4, bd=5, font=('Berlin Sans FB', 13))

        
        s1 = Style(background_label)
        # add the label to the progressbar style
        s1.layout("LabeledProgressbar2",
                  [('LabeledProgressbar2.trough',
                    {'children': [('LabeledProgressbar2.pbar',
                                   {'side': 'left', 'sticky': 'ns'}),
                                  ("LabeledProgressbar2.label",  # label inside the bar
                                   {"sticky": ""})],
                     'sticky': 'nswe'})])
        
        progress2 = Progressbar(background_label, orient=HORIZONTAL, length=200, mode='determinate',
                                style="LabeledProgressbar2")
        progress2['value'] = (len(Chalky) / len(All)) * 100
        background_label.update_idletasks()
        progress2.grid(row=0, column=2, sticky="s", pady=200)
        s1.configure("LabeledProgressbar2", thickness=20, text='Chalky ' + str(round((chalky_percentage*100),3)) + ' %',
                    troughcolor='#d1d1d1', background='white', relief=GROOVE, height=4, font=('Berlin Sans FB', 13))


        s = Style(background_label)
        # add the label to the progressbar style
        s.layout("LabeledProgressbar",
                 [('LabeledProgressbar.trough',
                   {'children': [('LabeledProgressbar.pbar',
                                  {'side': 'left', 'sticky': 'ns'}),
                                 ("LabeledProgressbar.label",  # label inside the bar
                                  {"sticky": ""})],
                    'sticky': 'nswe'})])
        # self.myvar1 = Label(root, text='Yellow', bg='#336699')
        # self.myvar1.grid(row=1, column=2, sticky="s", pady=0)
        progress = Progressbar(background_label, orient=HORIZONTAL, length=200, mode='determinate',
                               style="LabeledProgressbar")
        progress['value'] = (len(Yellow) / len(All)) * 100
        background_label.update_idletasks()
        progress.grid(row=0, column=2, sticky="s", pady=250)
        
        s.configure("LabeledProgressbar", thickness=20, text='Yellow ' + str(round((yellow_percentage*100),3)) + ' %',
                    troughcolor='#d1d1d1', background='yellow', relief=GROOVE, height=4, font=('Berlin Sans FB', 13))


##        global yellow_value, chalky_value, damage_value, paddy_value 
##        yellow_value = (len(Yellow) / len(All)) * 100
##        chalky_value = (len(Chalky) / len(All)) * 100
##        damage_value = (len(damages) / len(All)) * 100
##        paddy_value = (len(paddy) / len(All)) * 100
##        data1 = {'Rice_type': ['Paddy', 'Chalky', 'Yellow', 'Damage'],
##                 'Rice_value': [paddy_value,chalky_value,yellow_value,damage_value]
##                 }
##        df1 = DataFrame(data1, columns=['Rice_type', 'Rice_value'])
##
##        figure1 = plt.Figure(figsize=(6, 5), dpi=50)
##        ax1 = figure1.add_subplot(111)
##        bar1 = FigureCanvasTkAgg(figure1, background_label)
##        bar1.get_tk_widget().grid(row=0, column=2, sticky="s", pady=10)
##        df1 = df1[['Rice_type', 'Rice_value']].groupby('Rice_type').sum()
##        df1.plot(kind='bar', legend=True, ax=ax1)
##        ax1.set_title('Display')


        
        ####
        my_all()
        

    else:
    #this below condition is true when user tested sample and then reset it after that clicked on display tab
        if canvas is not None:
            canvas.destroy()
            btn_all.destroy()
            yellow.destroy()
            damage.destroy()
            chalky.destroy()
            paddy.destroy()
            self.back.destroy()
            vsb.destroy()
            hsb.destroy()


        background_image(root)
        
        label_error=Label(root,foreground="black",background="azure",text="Please Test Sample",relief=RAISED,font=("Courier", 44))
        label_error.grid(row=0,column=0)
        

    root.mainloop()       

            
#-----------------------------------------------------------#
# Sample Window Class
# Sample Window Class
#-----------------------------------------------------------#

class Sample(tk.Frame):

    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg =  "#dbdbdb")


        def resize_image(event):
            new_width = event.width
            new_height = event.height
            image = copy_of_image.resize((new_width, 120))
            photo = ImageTk.PhotoImage(image)
            label.config(image = photo)
            label.image = photo #avoid garbage collection
    
        
        image = Image.open("img/cv3.jpg")
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo)
        label.bind('<Configure>', resize_image)
        label.image = photo # keep a reference!
        label.pack(side="top" ,padx=0, pady=0)


        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.BOTH, side=tk.TOP)
        
        # Initialize Buttons and add images to button
        self.image_h = tk.PhotoImage(file='img/iconh.png')
        Home_button = ttk.Button(button_frame, text="Home ",
                                 image=self.image_h, compound="left",
                                 command=lambda: controller.show_frame(Home))
        
        self.image_v = tk.PhotoImage(file="img/iconv.png")
        Sample_button = ttk.Button(button_frame,text="View Sample", 
                                   image=self.image_v, compound="left")
                                   
        
        self.image_r = tk.PhotoImage(file="img/iconr.png")
        Repor_button = ttk.Button(button_frame, text="Summarized Report",
                                 image=self.image_r, compound="left",
                                 command= pdf_view)
        
        self.image_dr = tk.PhotoImage(file="img/detailed.png")
        DRepor_button = ttk.Button(button_frame, text="Detailed Report",
                                 image=self.image_dr, compound="left",
                                 command= pdf1_view)
        
        self.display_icon = tk.PhotoImage(file="img/display.png")
        Display_button = ttk.Button(button_frame, text="Display All",
                         image=self.display_icon, compound="left",
                         command=Display)

        
        self.reset_icon = tk.PhotoImage(file="img/reset.png")
        Reset_button = ttk.Button(button_frame, text="Reset",
                                 image=self.reset_icon, compound="left",
                                 command= reset_button)

        self.image_pie = tk.PhotoImage(file="img/iconpie.png")
        pieChart_button = ttk.Button(button_frame, text="Pie Chart",
                                     image=self.image_pie, compound="left",
                                     command=lambda: controller.show_frame(PieChart))

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)
        button_frame.columnconfigure(6, weight=1)
        
        Home_button.grid(row=0, column=0, sticky=tk.W+tk.E)
        Sample_button.grid(row=0, column=1, sticky=tk.W+tk.E)
        Repor_button.grid(row=0, column=2, sticky=tk.W+tk.E)
        DRepor_button.grid(row=0, column=3, sticky=tk.W+tk.E)
        Display_button.grid(row=0, column=4, sticky=tk.W+tk.E)
        pieChart_button.grid(row=0, column=5, sticky=tk.W+tk.E)
        Reset_button.grid(row=0, column=6, sticky=tk.W+tk.E)
        
        
        image1 = Image.open("img/line.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="top" ,padx=0, pady=0)
        

        
    ###################################################################
    # Update frame function
    ###################################################################
    
    def updateFrame(self):

        #globals.no_value_selected is 1 and
        if  globals.no_user_input is 1 and globals.browse_image is 1: #make reset value 1
            globals.reset=1
            
        #leena
        if globals.reset is 0:
            print("reset is 0")
            tkinter.messagebox.showinfo(title='Reset',message='No Data to show')
        ###
            
        else:
            #make reset value 1
            #try:
            global viewSample_counter #leena
            #this counter is to solve bug, labels were created multiple times whenever user click on ViewSample Tab
            if viewSample_counter is 0:
                #image1 = cv2.resize(rice_image, (400,600))
                image1 = cv2.resize(rice_image,None,fx = 0.15, fy = 0.13, interpolation = cv2.INTER_LINEAR)
                #image1 = cv2.resize((int(Image_screen_width/1.7),int(Image_screen_height)), Image.ANTIALIAS)#1.7
                #image1 = cv2.resize((Image_screen_width, Image_screen_height), Image.ANTIALIAS)
                b,g,r = cv2.split(image1)
                img = cv2.merge((r,g,b))
                im1 = Image.fromarray(img)
                
##                    #leena
##                    globals.label_input=tk.Label(self,text="Input Image ->",fg = "red", bg="#fff",font=("Helvetica", 12))
##                    globals.label_input.pack(side ="left",anchor = tk.W ,padx=20,)
##                    ####
##
##                    #leena
##                    globals.label_processed=tk.Label(self,text="<- Processed Image",fg = "red", bg="#fff", font=("Helvetica", 12))
##                    globals.label_processed.pack(side="right",anchor = tk.E,padx=20)
##                    ####

                viewSample_counter = viewSample_counter +1
                #leena
                #globals.button_to_open_new_window=tk.Button(self,text='click here',command=lambda: open_new_window(im2))
                #globals.button_to_open_new_window.pack(side="right",anchor = tk.E,padx=20)
                ####

                photo1 = ImageTk.PhotoImage(image=im1)
                
                #this is for raw image
                globals.label = tk.Label(self,image=photo1, text= "Input Image", compound="top",fg = "green", bg="#dbdbdb", font=("Helvetica", 16))
                globals.label.image = photo1 # keep a reference!
                globals.label.place(relx=.2,rely=.6, anchor="center")
                #globals.label.pack(side ="left" ,anchor = tk.NW , pady=10, padx=100)

                #leena
                #arrow image
                im = Image.open("img/arrow.png")
                #resized = im.resize((int(self.screen_width/1.7),int(self.screen_height)), Image.ANTIALIAS)#1.7
                resized = im.resize((int(400),int(400)), Image.ANTIALIAS)
                global arrow_label1
                tkimage = ImageTk.PhotoImage(resized, master=self)
                arrow_label1 = Label(self, image=tkimage,bg="#dbdbdb")
                arrow_label1.image = tkimage
                arrow_label1.place(relx=.5,rely=.6, anchor="center")
                #arrow_label1.pack(anchor = tk.CENTER,side="left")
                #arrow image

                if globals.rice_type_selected == "irri-6":
                    image2 = analysis_irri6.return_final_image()
                    if len(image2) == 0:
                        image2 = rice_image
                
                elif globals.rice_type_selected == "1121":
                    image2 = analysis_1121.return_final_image()
                    if len(image2) == 0:
                        image2 = rice_image
                
                elif globals.rice_type_selected == "pk386":
                    image2 = analysis_pk386.return_final_image()
                    if len(image2) == 0:
                        image2 = rice_image

                elif globals.rice_type_selected == "brown":
                    image2 = analysis_brown.return_final_image()
                    if len(image2) == 0:
                        image2 = rice_image

                elif globals.rice_type_selected == "super kernel basmati white":
                    image2 = analysis_super_kernel_basmati_white.return_final_image()
                    if len(image2) == 0:
                        image2 = rice_image

                elif globals.rice_type_selected == "super kernel basmati brown":
                    image2 = analysis_super_kernel_basmati_brown.return_final_image()
                    if len(image2) == 0:
                        image2 = rice_image

                elif globals.rice_type_selected == "1121 sela":
                    image2 = analysis_1121_sela.return_final_image()
                    if len(image2) == 0:
                        image2 = rice_image
                
                #image2 = cv2.resize(image2, (700,700))
                image2 = cv2.resize(image2,None,fx = 0.15, fy = 0.13, interpolation = cv2.INTER_LINEAR)#0.17,0.16
                b,g,r = cv2.split(image2)
                img = cv2.merge((r,g,b))
                im2 = Image.fromarray(img)

                photo2 = ImageTk.PhotoImage(image=im2)
                
                globals.label2 = tk.Label(self,image=photo2,borderwidth=0, highlightthickness = 0, text= "Processed Image", compound="top",fg = "green", bg="#dbdbdb", font=("Helvetica", 16))
                globals.label2.image = photo2 # keep a reference!

                globals.label2.place(relx=.8,rely=.6, anchor="center")
                #globals.label2.pack(side ="right" ,anchor= tk.NE, pady=10, padx=100)

            # except:
            #      #except clause
            #      tkinter.messagebox.showwarning(title='Warning',
            #                                  message='No Sample Image Found! First Input Sample Image')
#leena
    
def saveProcessedImage(photo2):
    i = 0
    while os.path.exists(our_path +'\\'+"processed-image-%s.png" % i):
        i += 1

    photo2._PhotoImage__photo.write(our_path +'\\'+"processed-image-%s.png" % i)
    

##def open_new_window(im2):
##    ventana2=tk.Toplevel()
##    canvas = Canvas(ventana2, width = 300, height = 200)
##    canvas.pack(expand = YES, fill = BOTH)
##    ventana2.title("Image")
##    photo1 = ImageTk.PhotoImage(image=im2)
##    canvas.create_image(50, 10, image = photo1, anchor = NW)
##    canvas.photo1 = photo1
####
    

#------------------------------------------------------------#
# PIE CHART CLASS STARTS #
#------------------------------------------------------------#
class PieChart(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg =  "#ffffff")

        def resize_image(event):
            new_width = event.width
            new_height = event.height
            image = copy_of_image.resize((new_width, 120))
            photo = ImageTk.PhotoImage(image)
            label.config(image = photo)
            label.image = photo #avoid garbage collection
    
        
        image = Image.open("img/cv3.jpg")
        copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo)
        label.bind('<Configure>', resize_image)
        label.image = photo # keep a reference!
        label.pack(side="top" ,padx=0, pady=0)


        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.BOTH, side=tk.TOP)
        
        # Initialize Buttons and add images to button
        self.image_h = tk.PhotoImage(file='img/iconh.png')
        Home_button = ttk.Button(button_frame, text="Home ",
                                 image=self.image_h, compound="left",
                                 command=lambda: controller.show_frame(Home))
        
        self.image_v = tk.PhotoImage(file="img/iconv.png")
        Sample_button = ttk.Button(button_frame,text="View Sample", 
                                   image=self.image_v, compound="left")
                                   
        
        self.image_r = tk.PhotoImage(file="img/iconr.png")
        Repor_button = ttk.Button(button_frame, text="Summarized Report",
                                 image=self.image_r, compound="left",
                                 command= pdf_view)
        
        self.image_dr = tk.PhotoImage(file="img/detailed.png")
        DRepor_button = ttk.Button(button_frame, text="Detailed Report",
                                 image=self.image_dr, compound="left",
                                 command= pdf1_view)
        
        self.display_icon = tk.PhotoImage(file="img/display.png")
        Display_button = ttk.Button(button_frame, text="Display Button",
                         image=self.display_icon, compound="left",
                         command=Display)

        
        self.reset_icon = tk.PhotoImage(file="img/reset.png")
        Reset_button = ttk.Button(button_frame, text="Reset Button",
                                 image=self.reset_icon, compound="left",
                                 command= reset_button)

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)
        
        Home_button.grid(row=0, column=0, sticky=tk.W+tk.E)
        Sample_button.grid(row=0, column=1, sticky=tk.W+tk.E)
        Repor_button.grid(row=0, column=2, sticky=tk.W+tk.E)
        DRepor_button.grid(row=0, column=3, sticky=tk.W+tk.E)
        Display_button.grid(row=0, column=4, sticky=tk.W+tk.E)
        Reset_button.grid(row=0, column=5, sticky=tk.W+tk.E)
        
        
        image1 = Image.open("img/line.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="top" ,padx=0, pady=0)


    def updateFrame(self):

        #globals.no_value_selected is 1 and
        if  globals.no_user_input is 1 and globals.browse_image is 1: #make reset value 1
            globals.reset=1
            print("run")
            
        #leena
        if globals.reset is 0 or globals.no_user_input is not 1 or globals.browse_image is not 1:
        #if clicked pie chart button after reseting
            print("reset is 0")
            tkinter.messagebox.showinfo(title='Pie Chart',message='No Data to show')
        ###
        else:   
            import matplotlib.pyplot as plt

            #print("objects=>",objects)

##            for i in objects:
##                i[
            print("piechart",report.total_yellow_weight)
            fig, ax = plt.subplots(figsize=(15, 15), subplot_kw=dict(aspect="equal"))
            r=[['Yellow Grains (qty)', report.total_yellow_weight], 
            ['Chalky Grains (qty)',report.total_chalky_weight],
            ['Damage Grains (qty)', report.total_damage_weight],['Total Grains (qty)', report.Total_new_weight]]


            d={ k[0]: k[1] for k in r }
##            d={ k[0]: k[1] for k in objects }
            #print("printing d =>",d)
            ################# pi chart #################
            keys=['Yellow Grains (qty)','Chalky Grains (qty)','Damage Grains (qty)']
            s=0
            for i,j in d.items():
                if i in keys:
                    s=s+(d[i])
                White=d['Total Grains (qty)']-s
            k=['Yellow Grains','Chalky Grains ','Damage Grains ']
            p=[]
            for i,j in d.items():
                if i in keys:
                    p.append(str(d[i])+' '+i )
            p.append(str(White)+' '+'White Grains (qty)')

            data = [float(x.split()[0]) for x in p]
            ingredients = [x.split()[1] for x in p]


##            def func(pct, allvals):
##                absolute = int(pct/100.*np.sum(allvals))
##                return "{:.1f}%\n{} ".format(pct,absolute)

            colors=['#67c2b4','#f7de8b','#92a8f7','#f5675f']
            explode = (0.1, 0.1, 0.1, 0.1)

            wedges, texts, autotexts = ax.pie(data, colors=colors,explode=explode,autopct='%1.0f%%',
                                      shadow=True,
                                      radius=1,
                                      textprops=dict(color="Black"))
            #print(ingredients)
            ax.legend(wedges, ingredients,
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

            #plt.setp(autotexts, size=8, weight="bold")

            ax.set_title("PIE CHART ANALYSIS",size=18,fontweight="bold")
            #plt.savefig('pi_chart.png')

            globals.canvas_piechart = FigureCanvasTkAgg(fig, master=self)
            globals.canvas_piechart.get_tk_widget().pack()
            globals.canvas_piechart.draw()
            #plt.show()
        
######----------------Pie Chart-----------#########


#-----------------------------------------------------------#
# Analyses Window Class
# Analyses Window Class
#-----------------------------------------------------------#


class Analyses(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg =  "#ffffff")
        
        image = Image.open("img/cv3.jpg")
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(self,image=photo)
        label.image = photo # keep a reference!
        label.pack(side="top" ,padx=0, pady=0)

        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.BOTH, side=tk.TOP)
        
        # Initialize Buttons and add images to button
        self.image_h = tk.PhotoImage(file='img/iconh.png')
        Home_button = ttk.Button(button_frame, text="Home ",
                                 image=self.image_h, compound="left",
                                 command=lambda: controller.show_frame(Home))

        self.image_v = tk.PhotoImage(file="img/iconv.png")
        Sample_button = ttk.Button(button_frame,text="View Sample", 
                                   image=self.image_v, compound="left",
                                   command=lambda: controller.show_frame(Sample))

        self.image_a = tk.PhotoImage(file="img/icona.png")
        Analyses_button = ttk.Button(button_frame, text="Analyses",
                                     image=self.image_a, compound="left")

        self.image_r = tk.PhotoImage(file="img/iconr.png")
        Repor_button = ttk.Button(button_frame, text="Summarized Report",
                                 image=self.image_r, compound="left",
                                 command= pdf_view)
        
        self.image_dr = tk.PhotoImage(file="img/iconr.png")
        DRepor_button = ttk.Button(button_frame, text="Detailed Report",
                                 image=self.image_dr, compound="left",
                                 command= pdf1_view)
        
        self.image_p1 = tk.PhotoImage(file="img/iconp.png")
        LGraph_button = ttk.Button(button_frame,text="Features Graph",
                                   image=self.image_p1, compound="left",
                                   command=lambda: controller.show_frame(LGraph))

        self.image_p2 = tk.PhotoImage(file="img/iconp.png")
        CGraph_button = ttk.Button(button_frame,text="Color Graph",
                                   image=self.image_p2, compound="left",
                                   command=lambda: controller.show_frame(CGraph))

        self.image_p3 = tk.PhotoImage(file="img/iconp.png")
        TGraph_button = ttk.Button(button_frame,text="Type Graph",
                                   image=self.image_p3, compound="left",
                                   command=lambda: controller.show_frame(TGraph))

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)
        button_frame.columnconfigure(6, weight=1)
        button_frame.columnconfigure(7, weight=1)

        Home_button.grid(row=0, column=0, sticky=tk.W+tk.E)
        Sample_button.grid(row=0, column=1, sticky=tk.W+tk.E)
        Analyses_button.grid(row=0, column=2, sticky=tk.W+tk.E)
        LGraph_button.grid(row=0, column=3,sticky=tk.W+tk.E)
        CGraph_button.grid(row=0, column=4,sticky=tk.W+tk.E)
        TGraph_button.grid(row=0, column=5,sticky=tk.W+tk.E)
        Repor_button.grid(row=0, column=6, sticky=tk.W+tk.E)
        DRepor_button.grid(row=0, column=7, sticky=tk.W+tk.E)
        
        image1 = Image.open("img/line.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="top",padx=0, pady=0)

        
        label = tk.Label(self, text="Analyses", font=LARGE_FONT, bg="#ffffff")
        label.pack(pady=50,padx=10)
        self.frame = VerticalScrolledFrame(self)
        self.frame.pack( side=tk.TOP,padx=90, pady=0)
        
        image1 = Image.open("img/main1.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="bottom" ,padx=0, pady=0)
        

        # Analyses table entries
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=0)
        b.insert(END, 'Object number')
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=1)
        b.insert(END, 'Width (mm)')
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=2)
        b.insert(END, 'Length (mm)')
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=3)
        b.insert(END, 'Area (mm^2)')
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=4)
        b.insert(END, 'Perimeter (mm)')
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=5)
        b.insert(END, 'Whole/Broken')
        b = Entry(self.frame.interior, text="")
        b.grid(row=0, column=6)
        b.insert(END, 'Class')

    ###################################################################
    # Update Frame Function 
    ###################################################################
        
    def updateFrame(self):
#        try:
        
        length_seq = [x['Length'] for x in objects]
        height = len(length_seq)
        for i in range(height+1):
            if (i == 0):
                continue
            else:
                b = Entry(self.frame.interior, text="")
                b.grid(row=i, column=0)
                b.insert(END, '%d' %(objects[i-1]["Object_number"]))
                b = Entry(self.frame.interior, text="")
                b.grid(row=i, column=1)
                b.insert(END, '{:.3f}'.format(objects[i-1]["Width"]))
                b = Entry(self.frame.interior, text="")
                b.grid(row=i, column=2)
                b.insert(END, '{:.3f}'.format(objects[i-1]["Length"]))
                b = Entry(self.frame.interior, text="")
                b.grid(row=i, column=3)
                b.insert(END, '{:.3f}'.format(objects[i-1]["Area"]))
                b = Entry(self.frame.interior, text="")
                b.grid(row=i, column=4)
                b.insert(END, '{:.3f}'.format(objects[i-1]["Perimeter"]))
                b = Entry(self.frame.interior, text="")
                b.grid(row=i, column=5)
                if (objects[i-1]["WB"] == 0):
                    b.insert(END, 'Broken Grain')
                else:
                    b.insert(END, 'Whole Grain')
                b = Entry(self.frame.interior, text="", bg=objects[i-1]["color_hex"])
                b.grid(row=i, column=6)
                b.insert(END, objects[i-1]["Type"])

#-----------------------------------------------------------#
# Features Prdiction Window Class
# Features Prdiction Window Class
#-----------------------------------------------------------#


class LGraph(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg =  "#ffffff")
        
        image = Image.open("img/cv3.jpg")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo)
        label.image = photo # keep a reference!
        label.pack(side="top" ,padx=0, pady=0)
         
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.BOTH, side=tk.TOP)


        # Initialize Buttons and add images to button
        self.image_h = tk.PhotoImage(file='img/iconh.png')
        Home_button = ttk.Button(button_frame, text="Home ",
                                 image=self.image_h, compound="left",
                                 command=lambda: controller.show_frame(Home))

        self.image_v = tk.PhotoImage(file="img/iconv.png")
        Sample_button = ttk.Button(button_frame,text="View Sample", 
                                   image=self.image_v, compound="left",
                                   command=lambda: controller.show_frame(Sample))

        self.image_a = tk.PhotoImage(file="img/icona.png")
        Analyses_button = ttk.Button(button_frame, text="Analyses",
                                     image=self.image_a, compound="left",
                                     command=lambda: controller.show_frame(Analyses))

        self.image_r = tk.PhotoImage(file="img/iconr.png")
        Repor_button = ttk.Button(button_frame, text="Summarized Report",
                                 image=self.image_r, compound="left",
                                 command= pdf_view)
        
        self.image_dr = tk.PhotoImage(file="img/iconr.png")
        DRepor_button = ttk.Button(button_frame, text="Detailed Report",
                                 image=self.image_dr, compound="left",
                                 command= pdf1_view)
        
        self.image_p1 = tk.PhotoImage(file="img/iconp.png")
        LGraph_button = ttk.Button(button_frame,text="Features Graph",
                                   image=self.image_p1, compound="left",
                                   command=lambda: controller.show_frame(LGraph))

        self.image_p2 = tk.PhotoImage(file="img/iconp.png")
        CGraph_button = ttk.Button(button_frame,text="Color Graph",
                                   image=self.image_p2, compound="left",
                                   command=lambda: controller.show_frame(CGraph))

        self.image_p3 = tk.PhotoImage(file="img/iconp.png")
        TGraph_button = ttk.Button(button_frame,text="Type Graph",
                                   image=self.image_p3, compound="left",
                                   command=lambda: controller.show_frame(TGraph))
 
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)
        button_frame.columnconfigure(6, weight=1)
        button_frame.columnconfigure(7, weight=1)
        
        Home_button.grid(row=0, column=0, sticky=tk.W+tk.E)
        Sample_button.grid(row=0, column=1, sticky=tk.W+tk.E)
        Analyses_button.grid(row=0, column=2, sticky=tk.W+tk.E)
        LGraph_button.grid(row=0, column=3,sticky=tk.W+tk.E)
        CGraph_button.grid(row=0, column=4,sticky=tk.W+tk.E)
        TGraph_button.grid(row=0, column=5,sticky=tk.W+tk.E)
        Repor_button.grid(row=0, column=6, sticky=tk.W+tk.E)
        DRepor_button.grid(row=0, column=7, sticky=tk.W+tk.E)
        
        
        
        label = tk.Label(self,
                         text='Rice Quality Analysis on the basis of Features of Rice Grains', 
                         font=LARGE_FONT, bg="#ffffff" )
        label.pack(pady=10, padx=10)

        image1 = Image.open("img/main1.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="bottom", padx=0, pady=0)
        
    
    ###################################################################
    # Update Function
    # Update Function
    ###################################################################

    def updateFrame(self):
       
#       Pie Chart
        try:
        
            f = Figure(figsize=(5,5), dpi=100)
                
                
            ax = f.add_subplot(111)
            
            data =report.ldata
            
            statusbar['text'] ="Feature Graph"
            
            leg=['Whole Grains', 'Long Broken Grain', 
                 'Medium Broken Grain', 'Small Broken Grain'] # Legends of Pie Chart
            # Condition for the labels
            label=[0,1,2,3]
                # Condition for the labels
            if data[0]>2:
                label[0]='Whole Grains'
            else:
                label[0]=' '
            if data[1]>2:
                label[1]='Long Broken Grain'
            else:
                label[1]=' ' 
            if data[2]>2:
                label[2]='Medium Broken Grain'
            else:
                label[2]=' '
            if data[3]>2:
                label[3]='Small Broken Grain'
            else:
                label[3]=' '
            
            Time = report.Time
            Date = report.Date
    
            colors = ['yellowgreen', 
                      'gold', 
                      'lightskyblue', 
                      'lightcoral']
            explode = (0.2, 0.2, 0.2, 0.2)
            ax.pie(data, colors= colors, 
                   labels=label, 
                   explode=explode,
                   autopct='%1.1f%%')
            ax.set_title(Date +' '+ Time)
            ax.legend(leg,loc='best')
            ax.axis('equal')
            
            canvas = FigureCanvasTkAgg(f,self)
            canvas.draw()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)        
            
            # Navigation Toolbar
            toolbar= NavigationToolbar2Tk(canvas, self)
            toolbar.update()

        except:
            #except clause
            tkinter.messagebox.showwarning(title='Warning',
                                           message='No Sample Image Found! First Input Sample Image')
        


# =============================================================================
# Color Prdiction Window Class   
# Color Prdiction Window Class
# =============================================================================

class CGraph(tk.Frame):
    
    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent, bg =  "#ffffff")
      
        image = Image.open("img/cv3.jpg")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo)
        label.image = photo # keep a reference!
        label.pack(side="top" ,padx=0, pady=0)

        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.BOTH, side=tk.TOP)

        # Initialize Buttons and add images to button
        self.image_h = tk.PhotoImage(file='img/iconh.png')
        Home_button = ttk.Button(button_frame, text="Home ",
                                 image=self.image_h, compound="left",
                                 command=lambda: controller.show_frame(Home))

        self.image_v = tk.PhotoImage(file="img/iconv.png")
        Sample_button = ttk.Button(button_frame,text="View Sample", 
                                   image=self.image_v, compound="left",
                                   command=lambda: controller.show_frame(Sample))

        self.image_a = tk.PhotoImage(file="img/icona.png")
        Analyses_button = ttk.Button(button_frame, text="Analyses",
                                     image=self.image_a, compound="left",
                                     command=lambda: controller.show_frame(Analyses))

        self.image_r = tk.PhotoImage(file="img/iconr.png")
        Repor_button = ttk.Button(button_frame, text="Summarized Report",
                                 image=self.image_r, compound="left",
                                 command= pdf_view)
        
        self.image_dr = tk.PhotoImage(file="img/iconr.png")
        DRepor_button = ttk.Button(button_frame, text="Detailed Report",
                                 image=self.image_dr, compound="left",
                                 command= pdf1_view)

        self.image_p1 = tk.PhotoImage(file="img/iconp.png")
        LGraph_button = ttk.Button(button_frame,text="Features Graph",
                                   image=self.image_p1, compound="left",
                                   command=lambda: controller.show_frame(LGraph))

        self.image_p2 = tk.PhotoImage(file="img/iconp.png")
        CGraph_button = ttk.Button(button_frame,text="Color Graph",
                                   image=self.image_p2, compound="left",
                                   command=lambda: controller.show_frame(CGraph))

        self.image_p3 = tk.PhotoImage(file="img/iconp.png")
        TGraph_button = ttk.Button(button_frame,text="Type Graph",
                                   image=self.image_p3, compound="left",
                                   command=lambda: controller.show_frame(TGraph))
        
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)
        button_frame.columnconfigure(6, weight=1)
        button_frame.columnconfigure(7, weight=1)

        Home_button.grid(row=0, column=0, sticky=tk.W+tk.E)
        Sample_button.grid(row=0, column=1, sticky=tk.W+tk.E)
        Analyses_button.grid(row=0, column=2, sticky=tk.W+tk.E)
        LGraph_button.grid(row=0, column=3,sticky=tk.W+tk.E)
        CGraph_button.grid(row=0, column=4,sticky=tk.W+tk.E)
        TGraph_button.grid(row=0, column=5,sticky=tk.W+tk.E)
        Repor_button.grid(row=0, column=6, sticky=tk.W+tk.E)
        DRepor_button.grid(row=0, column=7, sticky=tk.W+tk.E)
        
        label = tk.Label(self,text='Rice Quality Analysis on the basis of Color of Rice Grains', 
                         font=LARGE_FONT, bg="#ffffff")
        label.pack(pady=10,padx=10)
        
        image1 = Image.open("img/main1.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="bottom" ,padx=0, pady=0)


    ###################################################################
    # Update Function
    ###################################################################

    def updateFrame(self):
        
#       Pie Chart
        try:
            
            f = Figure(figsize=(5,5), dpi=100)
            ax = f.add_subplot(111)
    
            data =report.cdata
            
            statusbar['text'] ="Color Graph"
    
            leg=['Brown Rice Grains', 'Ye_Brown Rice Grains',
                 'White Rice Grains', 'Yellow Rice Grains'] # Legends of Pie Chart
            label=[0,1,2,3]
                # Condition for the labels
            if data[0]>2:
                label[0]='Brown Rice Grain'
            else:
                label[0]=' '
            if data[1]>2:
                label[1]='Ye_Brown Rice Grains'
            else:
                label[1]=' ' 
            if data[2]>2:
                label[2]='White Rice Grains'
            else:
                label[2]=' '
            if data[3]>2:
                label[3]='Yellow Rice Grains'
            else:
                label[3]=' '
                
            Time = report.Time
            
            Date = report.Date
            
            colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
            explode = (0.2, 0.2, 0.2, 0.2)
            ax.pie(data, 
                   colors=colors, 
                   explode=explode,
                   labels=label,
                   autopct='%1.1f%%')
            
            ax.legend(leg,loc='best')
            ax.axis('equal')
            
            ax.set_title(Date +' '+ Time)
           
            
            canvas = FigureCanvasTkAgg(f,self)
            canvas.draw()
    #        # Navigation Toolbar
            toolbar= NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        except:
            #except clause
            tkinter.messagebox.showwarning(title='Warning',
                                           message='No Sample Image Found! First Input Sample Image')


# =============================================================================
# Type Prdiction Window Class
# Type Prdiction Window Class
# =============================================================================
class TGraph(tk.Frame):

        
    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent, bg =  "#ffffff")
  
        image = Image.open("img/cv3.jpg")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo)
        label.image = photo # keep a reference!
        label.pack(side="top" ,padx=0, pady=0)
         
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.BOTH, side=tk.TOP)


        # Initialize Buttons and add images to button
        self.image_h = tk.PhotoImage(file='img/iconh.png')
        Home_button = ttk.Button(button_frame, text="Home ",
                                 image=self.image_h, compound="left",
                                 command=lambda: controller.show_frame(Home))

        self.image_v = tk.PhotoImage(file="img/iconv.png")
        Sample_button = ttk.Button(button_frame,text="View Sample", 
                                   image=self.image_v, compound="left",
                                   command=lambda: controller.show_frame(Sample))

        self.image_a = tk.PhotoImage(file="img/icona.png")
        Analyses_button = ttk.Button(button_frame, text="Analyses",
                                     image=self.image_a, compound="left",
                                     command=lambda: controller.show_frame(Analyses))

        self.image_r = tk.PhotoImage(file="img/iconr.png")
        Repor_button = ttk.Button(button_frame, text="Summarized Report",
                                 image=self.image_r, compound="left",
                                 command= pdf_view)

        self.image_dr = tk.PhotoImage(file="img/iconr.png")
        DRepor_button = ttk.Button(button_frame, text="Detailed Report",
                                 image=self.image_dr, compound="left",
                                 command= pdf1_view)
        
        self.image_p1 = tk.PhotoImage(file="img/iconp.png")
        LGraph_button = ttk.Button(button_frame,text="Features Graph",
                                   image=self.image_p1, compound="left",
                                   command=lambda: controller.show_frame(LGraph))
        
        self.image_p2 = tk.PhotoImage(file="img/iconp.png")
        CGraph_button = ttk.Button(button_frame,text="Color Graph",
                                   image=self.image_p2, compound="left",
                                   command=lambda: controller.show_frame(CGraph))
        
        self.image_p3 = tk.PhotoImage(file="img/iconp.png")
        TGraph_button = ttk.Button(button_frame,text="Type Graph",
                                   image=self.image_p3, compound="left",
                                   command=lambda: controller.show_frame(TGraph))
        
 
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)
        button_frame.columnconfigure(4, weight=1)
        button_frame.columnconfigure(5, weight=1)
        button_frame.columnconfigure(6, weight=1)
        button_frame.columnconfigure(7, weight=1)
        
 
        Home_button.grid(row=0, column=0, sticky=tk.W+tk.E)
        Sample_button.grid(row=0, column=1, sticky=tk.W+tk.E)
        Analyses_button.grid(row=0, column=2, sticky=tk.W+tk.E)
        LGraph_button.grid(row=0, column=3,sticky=tk.W+tk.E)
        CGraph_button.grid(row=0, column=4,sticky=tk.W+tk.E)
        TGraph_button.grid(row=0, column=5,sticky=tk.W+tk.E)
        Repor_button.grid(row=0, column=6, sticky=tk.W+tk.E)
        DRepor_button.grid(row=0, column=7, sticky=tk.W+tk.E)
        
                
        label = tk.Label(self,text='Rice Quality Analysis on the basis of Type of Rice Grains', 
                         font=LARGE_FONT, bg="#ffffff")
        label.pack(pady=10,padx=10)
        
        image1 = Image.open("img/main1.jpg")
        photo2 = ImageTk.PhotoImage(image1)
        label2 = tk.Label(self,image=photo2)
        label2.image = photo2 # keep a reference!
        label2.pack(side="bottom" ,padx=0, pady=0)
   
        
        
    ###########################################################
    # Update Frame
    # Update Frame
    ###########################################################
    def updateFrame(self):
        
#        Pie Chart
        try:
            
            f = Figure(figsize=(5,5), dpi=100)
            ax = f.add_subplot(111)

            data =report.tdata
            
            statusbar['text'] ="Type Graph"
    
            leg=['Brown Basmati Grains', 'Super Grians',
                 'Irri6 Grains', 'Brown Grains'] # Legends of Pie Chart
            
             # Condition for the labels
            label=[0,1,2,3]
                # Condition for the labels
            if data[0]>2:
                label[0]='Brown Basmati Grains'
            else:
                label[0]=' '
            if data[1]>2:
                label[1]='Super Grians'
            else:
                label[1]=' ' 
            if data[2]>2:
                label[2]='Irri6 Grains'
            else:
                label[2]=' '
            if data[3]>2:
                label[3]='Brown Grains'
            else:
                label[3]=' '
    
            
            Time = report.Time
            
            Date = report.Date
    
            
            colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
            explode = (0.2, 0.2, 0.2, 0.2)
            ax.pie(data, colors=colors, labels=label, explode=explode,
                   autopct='%1.1f%%')
            
            ax.set_title(Date +' '+ Time)

            ax.legend(leg,loc='best')
            ax.axis('equal')
            
            
            canvas = FigureCanvasTkAgg(f,self)
            canvas.draw()
            # Navigation Toolbar
            toolbar= NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            
  
        except:
            #except clause
            tkinter.messagebox.showwarning(title='Warning',
                                           message='No Sample Image Found! First Input Sample Image')
        


        
#calling main class
app = SeaofBTCapp()
LOOP_ACTIVE = True


# create status bar
statusbar = ttk.Label(app, text='Welcome to Rice Quality Analyzer', relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X) 

#defining the geometry of window
app.state('zoomed')
#app.geometry("{}x{}".format(Image_screen_width, Image_screen_height))
#app.geometry('1300x900+0+0')
app.resizable(width=True, height=True)

#leena

    
def yes_func():
    global no_func
    no_func=1
    reset_button()
    app.destroy()

def cancel_func():
    new_win.destroy()
    
    
def close_app():
    
    global new_win
    new_win = Toplevel()

    center_widget(300,100)
    new_win.resizable(0, 0)
    new_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    new_win.title('Confirm Exit')
    message = "Are you sure you want to exit?"
    Label(new_win, text=message, fg='grey', font=("Helvetica", 12)).place(x=40, y=10)
    Button(new_win, text='Yes',command=yes_func, width=6, height=1).place(x=60, y=60)
    Button(new_win, text='Cancel', command=cancel_func, width=6, height=1).place(x=170, y=60)


app.protocol('WM_DELETE_WINDOW',close_app) #to perform functionality when close from title bar, whole app
###

tk.mainloop()
