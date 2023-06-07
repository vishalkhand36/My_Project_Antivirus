from tkinter import *
from tkinter.ttk import *
import time
import hashlib



import os
from tkinter import filedialog
from tkinter import messagebox
from numpy import empty, equal

from PIL import Image , ImageFont , ImageDraw

malware_hashes=list(open("virushash.unibit","r").read().split('\n'))
virusinfo = list(open("virusinfo.unibit","r").read().split('\n'))

def ak():
    #malware_hashes=list(open("virushash.unibit","r").read().split('\n'))
    #virusinfo = list(open("virusinfo.unibit","r").read().split('\n'))

    def sha256_hash(filename):

        try:
           with open(filename, "rb") as f:
               bytes= f.read()
               sha256hash=hashlib.sha256(bytes).hexdigest()
               f.close()
           return sha256hash

        except:
           return 0

    
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

    virusName =[]
    virusPath = [] 


     # when the virus is detect then they go to this folder 

    def scan(path):
        dir_list = list()
        for (dirpath,dirnames,filenames) in os.walk(path):
            dir_list += [os.path.join(dirpath, file) for file in filenames]


        for i in dir_list:
           print(i)

           time.sleep(1)
           bar['value']+=0.80
    
           window.update_idletasks()

           if malware_detector(i)!=0:
               virusName.append(malware_detector(i)+":: File :: "+i)
               virusPath.append(i)

    def scanpc():
        scan("C:\\users")
        
        if not virusName:

         messagebox.showinfo("done", "Your system is  safe!!!!")
        else:
         messagebox.showinfo("Alert", "Your system is not safe!!!!")



    window= Tk()
    window.title('Your files are scanning...')
    window['bg'] = 'black'
    bar= Progressbar(window, orient=HORIZONTAL, length=300)
    bar.pack(pady=10)

    button=Button(window,text="scan", command=scanpc).pack()

    window.mainloop()




        












