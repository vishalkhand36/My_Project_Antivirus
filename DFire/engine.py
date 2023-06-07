# importing hash library

#from fileinput import filename
import hashlib
#from importlib.resources import path
import os
#from posixpath import dirname
#from typing import Counter

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


        

        if malware_detector(i) !=0:

            virusName.append(malware_detector(i)+":: File :: "+i)
            virusPath.append(i)

    

# Virus Remover 
def virusRemover(path):
    folderScanner(path)
    if virusPath:
        for i in virusPath:
            os.remove(i)
    else:
        return 0        


def junkfileremover():  

    # temp file remove .

    temp_list = list()


    #windows username
   # username= os.environ.get('USERNAME').upper().split(" ")

    for (dirpath,dirnames,filenames) in os.walk('C:\\Windows\\Temp'):
        temp_list += [ os.path.join ( dirpath,file ) for file in filenames ]
        temp_list += [ os.path.join ( dirpath,file ) for file in dirnames]

    
    for (dirpath,dirnames,filenames) in os.walk('C:\\Users\\HP\\AppData\\Local\\Temp'):
        temp_list += [ os.path.join ( dirpath,file ) for file in filenames ]
        temp_list += [ os.path.join ( dirpath,file ) for file in dirnames]


    for (dirpath,dirnames,filenames) in os.walk("C:\\Windows\\Prefetch"):
        temp_list += [ os.path.join ( dirpath,file ) for file in filenames]
        temp_list += [ os.path.join ( dirpath,file ) for file in dirnames]


    print(temp_list)



    if temp_list:
            for i in temp_list:
                print(i)

                try:
                    os.remove(i)

                except :
                    pass

                try:
                    os.redir(i)

                except :
                    pass

    else:
        return 0 


