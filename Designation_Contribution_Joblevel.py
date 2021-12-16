import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog,ttk
import tkinter.font as font
#import tkinter
#from typing_extensions import ParamSpecKwargs
import selenium.webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import openpyxl
from openpyxl import *
import os
import sys
import xlwings as xw
import pandas as pd


''' Part of the three files of Core_DCT 1.5 which consists of multiprocessing'''



# ------------ Variables which are uploaded in Designation's dropdown ------------------

Dept = "Department code"
Desg = "Designations - Alias"
Desg_code = "Designations - Alias Code"
Numb_of_position = "Number Of Position"
Not_period = "count notice period employee"
Funct_area = "Functional Area"

# ------------------------------------ CSV upload ---------------------------------------

Business_unit_up = "D:/Import Files/Business Unit.csv"
Division_up = "D:/Import Files/Division.csv"
Designation_loc = "D:/Import Files/Designation Location.csv"
Dept_master = "D:/Import Files/Department Master.csv"
Dept_mapping = "D:/Import Files/Department Mapping.csv"
Cost_center = "D:/Import Files/Cost Center.csv"

Loc_type = "D:/Import Files/Location Type.csv"
City_type = "D:/Import Files/City Type.csv"
Locations_upload = "D:/Import Files/Location.csv"
Func_area = "D:/Import Files/Functional Area.csv"
Func_area_mapping = "D:/Import Files/Functional Area Mapping.csv"
#Band_upload = "D:/Import Files/Band.csv"
Grade_upload = "D:/Import Files/Grade.csv"
JobLevel_upload = "D:/Import Files/Joblevel.csv"
Contrib_level = "D:/Import Files/Contribution Level.csv"
Designation_name = "D:/Import Files/Designation Name.csv"
Designation = "D:/Import Files/Designation.csv"
Grade_in_designation = "D:/Import Files/Grade in Designation.csv"

# --------------------------------------- functions -------------------------------------

driver = None
global relative_path

# ------------- for Chromedriver, adjustment to add it in the exe --------------------

def resource_path1(relative_path):

    global base_path

    try:
        base_path = sys.MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return base_path + relative_path

# -------------- for Image, adjustment to add it in the exe -------------------------

def resource_path_logo(relative_path_logo):
    
    global base_path_logo
    
    try:
        base_path_logo = sys._MEIPASS
        print(base_path_logo)
    except Exception:
        base_path_logo = os.path.dirname(__file__)
        print(base_path_logo)
    return base_path_logo + relative_path_logo


 #pyi-makespec Py_Selenium.py --onefile --noconsole --add-binary "driver\chromedriver.exe;driver\" --add-data "Img\Dbox4.png;Img\"  --name Core_DCT
 #pyinstaller --clean Core_DCT.spec  

 #pyi-makespec Py_Selenium_Copy.py --onefile --noconsole --add-binary "driver\chromedriver.exe;driver\" --add-data "Img\Dbox4.png;Img\"  --name Core_DCT_demo_thread
 #pyinstaller --clean Core_DCT_demo_thread.spec

    
def upload_files2():

    # ------------ Using driver2 to open Designation's import window parallely -------------
    # Adding Login & admin code here again so that driver2 can access the designation page as an admin
    # Adding 15 mins wait and later 
    #Designation

    global driver2

    #wait = WebDriverWait(driver, 30)
    driver2 = selenium.webdriver.Chrome(resource_path1("/driver/chromedriver.exe"))

    driver2.maximize_window()
    url = WebLink1.get()
    driver2.get(url)
          
    try:
    # Admin's login
        driver2.find_element_by_id("UserLogin_username").send_keys(username2.get())
        driver2.find_element_by_id("UserLogin_password").send_keys(password2.get())
        driver2.find_element_by_id("login-submit").click()
        driver2.implicitly_wait(10)
    except:
        pass
    

    # How are you feeling today?

    try:
        driver2.find_element_by_xpath('//*[@id="pulse_form"]/div/div/div')
        driver2.find_element_by_xpath('//*[@id="5"]').click()
        driver2.find_element_by_xpath('//*[@id="plus-status-btn"]').click()
    except:
        pass

    #Click on the user's profile pic and switch to admin
    driver2.find_element_by_xpath('//*[@id="dasboard-bigheader"]/header/div[4]/ul/li[3]/div/div/img').click()
    driver2.find_element_by_xpath('//*[@id="dasboard-bigheader"]/header/div[4]/ul/li[3]/div/ul/li[2]/a').click()
    driver2.implicitly_wait(30)

    time.sleep(5)

    
    # Cost center

    try:

        time.sleep(4)
        driver2.get(WebLink1.get() + '/Importnewclient/costCenters')
        driver2.find_element_by_xpath('//*[@id="csvdata"]').send_keys(Cost_center)
        driver2.implicitly_wait(20)
        time.sleep(4)
        driver2.find_element_by_xpath('/html/body/div[2]/div/section/div[1]/div[1]/div/div/form/input[2]').click()
        #driver2.find_element_by_name('upload').click()
        driver2.implicitly_wait(20)

    except:
        pass

    # Location Type

    try:

        driver2.get(WebLink1.get() + '/Importnewclient/locationType')
        driver2.find_element_by_xpath('//*[@id="csvdata"]').send_keys(Loc_type)
        driver2.implicitly_wait(20)
        time.sleep(4)
        driver2.find_element_by_xpath('/html/body/div[2]/div/section/div[1]/div[1]/div/div/form/input[2]').click()
        #driver2.find_element_by_name('upload').click()
        driver2.implicitly_wait(20)

    except:
        pass

    # City Type

    try:

        driver2.get(WebLink1.get() + '/Importnewclient/cityType')
        driver2.find_element_by_xpath('//*[@id="csvdata"]').send_keys(City_type)
        driver2.implicitly_wait(20)
        time.sleep(4)
        driver2.find_element_by_xpath('/html/body/div[2]/div/section/div[1]/div[1]/div/div/form/input[2]').click()
        #driver2.find_element_by_name('upload').click()
        driver2.implicitly_wait(20)

    except:
        pass

    # Grade

    try:

        driver2.get(WebLink1.get() + '/Importnewclient/Grade')
        driver2.find_element_by_xpath('//*[@id="csvdata"]').send_keys(Grade_upload)
        driver2.implicitly_wait(20)
        time.sleep(4)
        driver2.find_element_by_xpath('/html/body/div[2]/div/section/div[1]/div[1]/div/div/form/input[2]').click()
        #driver2.find_element_by_name('upload').click()
        driver2.implicitly_wait(20)

    except:
        pass

    # Contribution Level

    if CheckBox_Contribution_var.get() == 1:

        try:
            driver2.get(WebLink1.get() + '/settings/employees/tenprofzz')
            driver2.execute_script("window.scrollTo(0, 1600)") 
            time.sleep(4)

            if driver2.find_element_by_id("TenantProfile_neev_level_allowed").is_selected() == False:
                time.sleep(4)
                driver2.find_element_by_id("TenantProfile_neev_level_allowed").click()
                driver2.execute_script("window.scrollTo(0, -500)")
                time.sleep(4)

                driver2.find_element_by_xpath("/html/body/div[2]/div/section/div/div/div/form/div[2]/div/input").click()
                time.sleep(4)
            
            else:
                pass

            driver2.get(WebLink1.get() + '/Importnewclient/contributionLevel')
            driver2.find_element_by_xpath('//*[@id="csvdata"]').send_keys(Contrib_level)
            driver2.implicitly_wait(20)
            
            time.sleep(4)
            driver2.find_element_by_xpath('/html/body/div[2]/div/section/div[1]/div[1]/div/div/form/input[2]').click()
            #driver2.find_element_by_name('upload').click()
            driver2.implicitly_wait(20)

        except:
            pass

    else:
        pass


def Help_window():
    messagebox.showinfo(title="How to use this executable",message=InfoForTHeUser)



# --------------------------------------------------------------------------------------------------------------
# ---------------------------------------------- Tkinter -------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------

InfoForTHeUser ="Please make sure that you have used the Automated DCT to take the export and the exported CSVs are present in 'D: Import files' folder. \r\n\r\n This window will help you to upload Designation, Grades, Contribution, job level CSVs \r\n \r\n \r\n Some points to remeber -> \r\n\r\n 1. Please make sure that you are adding the entire instance link. that is make sure to include 'https://' also \r\n\r\n 2. Please add the correct user ID and Password \r\n\r\n 3. 'Delays' are added purposely so as to let the website load all its elements. \r\n\r\n 4. Please select Contribution and Job level checkboxes if you want to upload them. Note : If user selects not to upload Job level then Grade in designation csv will be uploaded. \r\n \r\n\r\n Information about buttons -> \r\n 1. Upload files -> Will open a new Google chrome window and maximize it automatically then CSV exports from D -> Import files folder will be uploaded \r\n\r\n 4. Close chrome window -> will close the google chrome window\r\n"

# --------------------------------------------------- Added new root which represents Designation upload ---------------------------------------

driver = None
driver2 = None

def on_close2():

    if driver2:
        driver2.close()

def Open_designation_window():

    global WebLink1
    global username2
    global password2
    global CheckBox_Contribution_var
    global CheckBox_Joblevel_var

    root3 = tk.Tk()
    #root3 = Toplevel(root)
    #root3 = Toplevel()

    root3.title('Core_DCT_designation')
    #width then hight
    root3.geometry('445x270+1260+150')

    #root3['bg'] = '#5252ff'
    root3['bg'] = '#F8FAFA'

    # define font
    myFont2 = font.Font(family='Playfair Display',size=9)

    tk.Label(root3,text="Client Instance / Website Link",width=25,bg='#ADD8E6',fg='black',font=myFont2).grid(row=1,column=1,padx=10,pady=5)
    WebLink1 = StringVar()
    name1 = tk.Entry(root3, textvariable=WebLink1,width=30,bg='#F5F5F5')
    name1.grid(row=1,column=2,padx=5,pady=5)

    tk.Label(root3,text="User ID / Email ID",activebackground='white',width=25,bg='#ADD8E6',fg='black',font=myFont2).grid(row=2,column=1,padx=10,pady=3)
    username2 = StringVar()
    name2 = tk.Entry(root3, textvariable=username2,width=30,bg='#F5F5F5')
    name2.grid(row=2,column=2,padx=5,pady=3)

    tk.Label(root3,text="Password",width=25,bg='#ADD8E6',fg='black',font=myFont2).grid(row=3,column=1,padx=10,pady=3)
    password2 = StringVar()
    name3 = tk.Entry(root3, textvariable=password2,show="*",width=30,bg='#F5F5F5')
    name3.grid(row=3,column=2,padx=5,pady=3)

    CheckBox_Contribution_var = IntVar()
    CheckBox_Contribution1 = tk.Checkbutton(root3, text="Contribution Level, Applicable?", variable=CheckBox_Contribution_var, onvalue=1, offvalue=0,activebackground='blue',bg='#ADD8E6',fg='black',font=myFont2).grid(row=4,column=1,padx=10,pady=10,columnspan=2)

    #CheckBox_Joblevel_var= IntVar()
    #CheckBox_Job3 = tk.Checkbutton(root3, text="Job Level, Applicable?", variable=CheckBox_Joblevel_var, onvalue=1, offvalue=0,activebackground='blue',bg='#ADD8E6',fg='black',font=myFont2,width=25).grid(row=4,column=2,padx=10,pady=10)

    tk.Button(root3, text='Upload files', command=upload_files2,width=25,relief=RAISED,activebackground='Grey',bg='#ADD8E6',fg='black').grid(row=6,column=1,padx=10,pady=8,columnspan=2)

    tk.Button(root3, text='Close Chrome Window', command=on_close2,width=25,relief=RAISED,activebackground='Grey',bg='#ADD8E6',fg='black').grid(row=7,column=1,padx=8,pady=5,columnspan=2)

    tk.Label(root3,text="To add Cost Center, Location Type, City Type,\r Grade and Contribution level ",width=60,bg='#D0D3D4',fg='black').grid(row=8,column=1,padx=10,pady=10,columnspan=2)

    root3.mainloop()



