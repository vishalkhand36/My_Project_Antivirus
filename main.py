from email.mime import image
#from engine import junkfileremover

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
import hashlib
import os
from tkinter import filedialog
from tkinter import messagebox
from numpy import empty, equal
from engine import junkfileremover
from prog import ak
from time import strftime
from datetime import datetime


from PIL import Image , ImageFont , ImageDraw




malware_hashes=list(open("virushash.unibit","r").read().split('\n'))
virusinfo = list(open("virusinfo.unibit","r").read().split('\n'))

def sha256_hash(filename):

    try:
        with open(filename, "rb") as f:
            bytes= f.read()
            sha256hash=hashlib.sha256(bytes).hexdigest()
            f.close()
        
    
        return sha256hash

    except:
        return 0


    



#now detect malware
def malware_detector(pathoffile):
    global malware_hashes
    global virusinfo
    h_m_check= sha256_hash(pathoffile)

    Counter=0

    for i in malware_hashes:
        if i == h_m_check:
            return virusinfo[Counter]
        counter =+1
        
    return 0
    

#malware detect in folder
virusName =[]
virusPath = []      # when the virus is detect then they go to this folder 

def folderScanner(path):

    

    dir_list = list()

    # Get the list of all files in directory tree at given part 
    for (dirpath,dirnames,filenames) in os.walk(path):
       


    
        dir_list += [os.path.join(dirpath, file) for file in filenames]


    for i in dir_list:
        print(i)


        

        if malware_detector(i)!=0:
            virusName.append(malware_detector(i)+":: File :: "+i)

            virusPath.append(i)

   


  
    

    

    

msg=[]
        
def virusRemover(path):
    folderScanner(path)
    if virusPath:
        for i in virusPath:
            os.remove(i)
            msg=[1]
    else:
        return 0




# file browsing

def scanfile():
    filepath= filedialog.askdirectory()
    folderScanner(filepath)

    


    if not virusName:

         messagebox.showinfo("Alert", "This file is  safe!!!!")
    else:
        messagebox.showinfo("Alert", "This file is not safe!!!!")


# virus removel
def removefile():
    filepath= filedialog.askdirectory()
    virusRemover(filepath)

    if not msg:

         messagebox.showinfo("done", " virus removed")
    else:
        messagebox.showinfo("Alert",   "File is already safe!!!!!")
    
    

def ramBooster():
    tasklist = ['notepad.exe',"cmd.exe"]

    # Task Kill

    for i in tasklist:

        os.system ("taskkill /f /im {}".format(i))

def engine_run():
    junkfileremover()
    messagebox.showinfo( "done", "junkfile removed")


def systemscan(path):

    

    dir_list = list()

    # Get the list of all files in directory tree at given part 
    for (dirpath,dirnames,filenames) in os.walk(path):
       


    
        dir_list += [os.path.join(dirpath, file) for file in filenames]

    
    #for i in dir_list:
   

        
    

    for i in dir_list:
        print(i)

    
        
        


        if malware_detector(i)!=0:
            virusName.append(malware_detector(i)+":: File :: "+i)

            virusPath.append(i)

    


    
    
def realtimemoniter():
    systemscan("C:\\users")
    if not virusName:

         messagebox.showinfo("done", "Your system is  safe!!!!")
    else:
        messagebox.showinfo("Alert", "Your system is not safe!!!!")
        
    
#exit
def iexit():
            iexit=tkinter.messagebox.askyesno("DFire | Antivirus and System Cleaning Software by Shivila Technologies","Do you want to Exit ?",parent=roo_ueuron)
            if iexit >0:
                    roo_ueuron.destroy()
            else:
                    return
         


    


roo_ueuron =tkinter. Tk()

roo_ueuron.title('DFire | Antivirus and System Cleaning Software by Shivila Technologies')
roo_ueuron['bg'] = "#1A252C"

roo_ueuron.geometry('1100x700')
roo_ueuron.maxsize(width=1100 , height=900)


roo_ueuron.iconbitmap(r'icon.ico')
  


#title label
title_lbl=Label(roo_ueuron, text="DFire | Antivirus and System Cleaning Software by Shivila Technologies", 
        font=("arial",15,"bold"),
        bg="black",
        fg="#6c9493"
        )     

title_lbl.place(x=0,y=0,width=1100,height=45)  

def time():
                string = strftime( '%H:%M:%S %p' )
                lbl.config(text = string)
                lbl.after(1000, time)

lbl = Label(title_lbl, font = ('Arial',15,'bold'),bg='black',fg='white')
lbl.place(x=0,y=0,width=110,height=50)
time()

# frame 
frame=Frame(roo_ueuron,bg="white",bd=7) #bd for border
frame.place(x=0,y=40,width=1100,height=260)



img3=Image.open(r"Shivila Logo.png")
img3=img3.resize((210,210),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
frame.photoimg3=ImageTk.PhotoImage(img3)
        
#f_lbl=Label(frame, image=frame.photoimg3)
#f_lbl.place(x=0,y=0 ,height=250)

b1=Button(frame, image=frame.photoimg3, cursor="hand2", bg="white", bd=0)
b1.place(x=0,y=30,width=230, height=200)


title_lbl=Label(frame, text="Check your system status and clean it securely", 
        font=("arial",20,"bold"),
        bg="white",
        fg="#1974D2"
        )     

title_lbl.place(x=250,y=80,width=700,height=45)  





#Full scan btn
img4=Image.open(r"FULL SYSTEM SCAN.png")
img4=img4.resize((150,150),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
roo_ueuron.photoimg4=ImageTk.PhotoImage(img4)
        

b2=Button(roo_ueuron, image=roo_ueuron.photoimg4, cursor="hand2", bg="black", bd=2)
b2.place(x=120,y=330,width=200, height=175)

detect_btn = tkinter.Button (roo_ueuron,text='FULL SYSTEM SCAN',command=ak,width=19, height=1,font=('arial',12,'bold'),bg='white',fg='black',bd=2)
detect_btn.place(x=120,y=500)


#select system scan

img5=Image.open(r"SELECTED SYSTEM SCAN.png")
img5=img5.resize((150,150),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
roo_ueuron.photoimg5=ImageTk.PhotoImage(img5)
        


b2=Button(roo_ueuron, image=roo_ueuron.photoimg5, cursor="hand2", bg="black", bd=2)
b2.place(x=450,y=330,width=200, height=175)

detect_btn = tkinter.Button (roo_ueuron,text='CUSTOM FILE SCAN',command=scanfile,width=19, height=1,font=('arial',12,'bold'),bg='white',fg='black')
detect_btn.place(x=450,y=500)

#virus removel

img6=Image.open(r"VIRUS REMOVAL.png")
img6=img6.resize((150,150),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
roo_ueuron.photoimg6=ImageTk.PhotoImage(img6)
        


b2=Button(roo_ueuron, image=roo_ueuron.photoimg6, cursor="hand2", bg="black", bd=2)
b2.place(x=780,y=330,width=200, height=175)

detect_btn = tkinter.Button (roo_ueuron,text='VIRUS REMOVAL',command=removefile,width=19, height=1,font=('arial',12,'bold'),bg='white',fg='black')
detect_btn.place(x=780,y=500)

#cleaning

img7=Image.open(r"SYSTEM CLEANING.png")
img7=img7.resize((150,150),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
roo_ueuron.photoimg7=ImageTk.PhotoImage(img7)
        


b2=Button(roo_ueuron, image=roo_ueuron.photoimg7, cursor="hand2", bg="black", bd=2)
b2.place(x=300,y=550,width=200, height=175)

detect_btn = tkinter.Button (roo_ueuron,text='CLEANING',command=engine_run,width=19, height=1,font=('arial',12,'bold'),bg='white',fg='black')
detect_btn.place(x=300,y=720)


#ramboost

img8=Image.open(r"RAM BOOST.png")
img8=img8.resize((150,150),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
roo_ueuron.photoimg8=ImageTk.PhotoImage(img8)
        


b2=Button(roo_ueuron, image=roo_ueuron.photoimg8, cursor="hand2", bg="black", bd=2)
b2.place(x=620,y=550,width=200, height=175)

detect_btn = tkinter.Button (roo_ueuron,text='RAM BOOST',command=ramBooster,width=19, height=1,font=('arial',12,'bold'),bg='white',fg='black')
detect_btn.place(x=620,y=720)



# exit

detect_btn = tkinter.Button (roo_ueuron,text='Exit',command=iexit,width=8, height=1,font=('arial',11,'bold'),bg='black',fg='white')
detect_btn.place(x=1015,y=5)


roo_ueuron.mainloop()
