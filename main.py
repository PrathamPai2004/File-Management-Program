import os
import time
import pyttsx3
import platform
import sys
from datetime import datetime


prompt  = "Do you want to\n\nread-Write-Display-Delete--Recycle the deleted files?\n\n[ENTER RECYCLE_AREA TO VIEW THE RECYCLE FUNCTIONALITIES]\nEnter 'recyclefunctions' for operating on the recycled Directory \n\nInput :  "

recycleList =[]
runTimeFiles = []
engine = pyttsx3.init()
directoryList =set()
voices = engine.getProperty('voices')
engine.setProperty('rate',150)
voice = engine.setProperty('voice',voices[1].id)
flag = 0

welcome = "Hi This is me, Pratham......."
engine.say(welcome)
engine.runAndWait()

fileDict ={}

fileDictList =[]

message = "L O A D I N G"

current_Date_and_Time = str(datetime.now())[:-3]
system_name = platform.system()
node_name = platform.node()
release = platform.release()
version = platform.version()
machine = platform.machine()
processor = platform.processor()

systemInfo =["Operating System - "+system_name,"User - "+node_name,"Release - "+release,"Version - "+version,"Machine - "+machine,"Processor - "+processor]

operationalString = "Operations : read -  write - display/show - recyclefunctions - recycle - delete\n"

def dateTime():
    programExecuted ="                 Program executed on : "
    print()
    for p in range(0,len(programExecuted)):
        print(programExecuted[p]+" ",end='')
        time.sleep(0.05)
    
    print("\n                                       ",end='')
    
    for i in range(0,len(current_Date_and_Time)):
        print(current_Date_and_Time[i],end='')  
        time.sleep(0.1)  
    print("\n\n")
    print("Getting Machine Properties : ")
    loading()
    print("Machine properties :\n")
    for j in range(0,len(systemInfo)):
        print(systemInfo[j])
        time.sleep(0.02)
    print("\n")
    

def welcomeTransition():
    welcomeMessage = "P R O G R A M   MAIN.PY  D E P L O Y I N G . . . . . . ."
    for i in range(len(welcomeMessage)):
        print(welcomeMessage[i],end='')
        time.sleep(0.06)

    
def loading():
    for i in range(1, 101):
        print(f'\rLoading... {i}%', end='', flush=True)
        time.sleep(0.01)  

    print("\nDone!\n")

        
        
def propertiesModule(filename):
    filename = filename+".txt"
    accessRight = input("Enter the access rights - ReadOnly / Readwrite : \n")
    accessRight = accessRight.strip().lower()
    if(accessRight == 'readonly'):
        accessRight ='ro'
        
        
    else:
        accessRight='rw'
        
    fileDict.__setitem__("access_right",accessRight)
    fileDictList.append(fileDict) 
    
def viewProperties(filename):
    filename = filename+".txt"
    
    print(fileDictList[filename])
               

def timeDelay(delay):
    time.sleep(int(delay))

def recycleBin(filename,content):
    
    # filename = filename+".txt"
    directory =rf"C:\Users\prath\python\file_Project"
    recycleFiles = os.listdir(directory)
    if(len(recycleFiles)==0):
        return -1
    with open(f"./file_Project/{filename}",'w') as f :
        f.write(content)
        menu()

    
def showDirectories():

    directory =r'C:\Users\prath\python\file_Project'
    contents = os.listdir(directory)
    
    count = 0
    for file in contents:
        count= count + 1
        directoryList.add(file)
           
    if(count==2):
        return -1
              
    #count = 1 signifies only main.py is there
        
    print(directoryList)
    print("\n\n")
  


def getContentOfRecycleBin(file):
    file = file[0:len(file)-4]
    print(file)
    directory = r"C:\Users\prath\python\recycleBin"
    filesUnderThis = os.listdir(directory)
    contents=""
    try:
        with open(rf"{directory}\{file}.txt",'r') as fr:
            print(file)
            
            contents = fr.read()
        transferFromBinToCurrent(file,contents)
        os.remove(rf"{directory}/{file}.txt")
        loading()
        print(rf"File {file}.txt recovered successfully")
            
            
    except Exception as e:
        print(rf"Couldn't load {file}.txt from recycle bin! Try Again")
        menu() 

        
def transferFromBinToCurrent(file,contents):
    destPath = r"C:\Users\prath\python\file_Project"
    try:
        with open(rf"{destPath}\{file}.txt",'w') as fw:
            fw.write(contents)
        loading()
        print("File recycled without any interruption")
    except Exception as e :
        print("Couldn't write into the normal directory")   

    
def transferToBin(deletedFile):
    directory =r"C:\Users\prath\python\file_Project"
    with open(fr"{directory}\{deletedFile}",'r') as f:
        content = f.read()
    recycleDirectory = r"C:\Users\prath\python\recycleBin"
    with open(rf"{recycleDirectory}\{deletedFile}",'w') as fw:
        fw.write(content)
        
    # recycleBin(deletedFile,content)    
     
    
def deleteFile(removalFile):
    directory =r'C:\Users\prath\python\file_Project'
    contents = os.listdir(directory)
    engine.setProperty('rate',180)
    
    try:    
        for file in contents:
            if f"{removalFile}.txt" == file:
                if f"{removalFile}.txt" in runTimeFiles:
                    engine.say(f"Alert ! This file is created in the existing run time ..it is advised to Re-Run the program for deleting {removalFile}.txt")
                    engine.runAndWait()
                    
                print(f"{removalFile}.txt found")
                engine.say(f"Disclaimer ! You have prompted {removalFile}.txt for the deletion ")
                # engine.runAndWait()
                engine.say("If you did this unintentionally Please reconfirm machine with 'yes'.. or.. Proceed for the deletion by pressing ENTER ")
                engine.runAndWait()
                print(f"Do you want to undo the previous action : Enter 'yes' for retaining {removalFile}.txt ")
                timeDelay(2)
                print("IF YOU STILL WANT TO CONTINUE WITH THE DELETION PROCESS PRESS ENTER")
                undo=input()
                undo=undo.strip().lower()
                
                print("Please do note that Program sometimes crashes while deleting the file |")
                if(undo==" "):
                    undo=""
                if(undo==""):
                    engine.say("You have pressed Enter....Deletion occuring")
                    path = directory + rf"\{removalFile}.txt"
                    print(path)
                    print()
                    loading()
                    print()
                    print(f"{removalFile}.txt Deleted successfully on user's choice")
                    print(path)
                    directoryList.remove(f"{removalFile}.txt")
                    transferToBin(rf"{removalFile}.txt")
                    os.remove(path)
                    time.sleep(0.5)
                    print(f"Deletion of {removalFile}.txt has been carried out successfully")
                    menu()
                    break
                    
                if(undo=='yes'):
                    time.sleep(1.5)
                    loading()
                    engine.say(f"{removalFile}.txt got retained")
                    engine.runAndWait()
                    print(f"{removalFile}.txt retained")
                    menu()
                    
                
        else:
            print(f"{removalFile}.txt is not there")
            
    except Exception :
        timeDelay(2)
        print("\n\n\n\n\n")
        print("\n\nFiles which are created in this run time cant be deleted\n\n")
        print("\n Re-Run the program for the deletion \n  This Program crashes in deletion feature as it cannot run Writing and Removal for one simultaneous execution\n\n\n")
        notify = "Files which are created in this run time cant be deleted. Re-Run the program for the deletion This Program crashes in deletion feature as it cannot run Writing and Removal for one simultaneous execution"
        
        # timeDelay(3)
        runAgain = "Please Re-Run |  Program main.py "
        abortingNotice = " Program getting aborted by itself in 5 seconds "
        voice = engine.setProperty('voice',voices[1].id)
        
        engine.say(notify)
        engine.runAndWait()
        engine.say(runAgain)
        engine.runAndWait()
        engine.say(abortingNotice)
        engine.runAndWait()
    
        print("Please Re-Run |  Program main.py getting aborted by itself in 5 seconds \n")
        for i in range(1,6):
            timeDelay(0.8)
            print(i)
        loading()
        print("Aborted")
        exit()   

def readFileLoudly(content):
    engine.say(content)
    engine.runAndWait()
    engine.say("file read completely")
    loading()
    menu()
                
def checkExistingFileWithUserInput(userFile,fileList):
    #initially it was of sinle argument
    #in directoryList {in for loop}
    for file in fileList :
        if userFile in file:
            return 1
    
    if(userFile!=file):
        return -1    

        
def menu():
    print("\nM A I N  M E N U\n")
    
    engine.say("Please input the appropriate operation")
    engine.runAndWait() 

    userAction = input(prompt+":=> ")
    print()
    while userAction!='exit':
        supplyUserInput(userAction.strip().lower())
    
    
    engine.say("Exited conveniently on the user's choice")
    engine.say("...Good Bye")    
    engine.runAndWait()
    exit()


     
def readDocument(filename):
    
        with open(f"./file_Project/{filename}.txt",'r') as f:
            
            userChoice = input("Please enter 'listen' to listen to the content : ")
            loading()
            print(rf"You are reading {filename}.txt\n")
            data = f.read()
            print(data)
            if userChoice=='listen':
                loading()
                engine.say(f"Reading {filename}.txt")
                readFileLoudly(data)
            menu()
        print("Please enter the valid document name")
        showDirectories()
        # print(existing_files)
        menu()    
      
       
def supplyUserInput(userAction):            
    match userAction:
        case 'read':

            if(showDirectories() == -1):
                engine.say("There are no text files to read...Please add TEXT files into the directory ")
                engine.runAndWait()
                print("There are no text files to read\nPlease Add to read")
                menu()
            
            else:
                
                showDirectories()
                
                fileInput = input("Enter the file which you want to read : [enter 'exit' to any time jump for the main menu] ")
                if(fileInput=='exit'):
                    menu()
            
                check = (checkExistingFileWithUserInput(f"{fileInput}",directoryList))
                if(check == 1):
                    print("Opening the document....")
                    readDocument(f"{fileInput}")
                    # readFile(fileInput)
                else:
                    print("Enter the valid filename given in the list below : ")
                    showDirectories()
                    file = input("Enter the filename : ").strip().lower()
                    print("Enter exit to jump into the main menu : ")
                    if(file=='exit'):
                        menu()
                    checkExistingFileWithUserInput(file,directoryList)
                    
                    
                    
                
        
        case 'write':
            
            fileName = input("Enter the filename : ")
        
            content =""
            with open(f"./file_Project/{fileName}.txt",'w') as f :
                runTimeFiles.append(f"{fileName}.txt")
                print("Enter content (or 'exit' to finish : ")
                while content!='exit':
                    
                    content = input()
                    
                    if(content=='exit'):
                        break
                    f.write(content+"\n")
                    
            with  open(f"./file_Project/{fileName}.txt",'r') as fr :
                line_count = 0
                for line in fr:
                    line_count+=1
            
                if(line_count>0):
                    engine.say(rf"File {fileName}.txt has been written into the directory")
                    print(f"Wrote successfully! with {line_count} no of lines")
                    menu()
                else:
                    print("Failure")
                        
                
        case 'show' | 'display':
                        
            print("The files you have in your directory are :\n")
            if(showDirectories() == -1):
                engine.say("There is an empty list in the directory ..Please add some text files for appending the list")
                engine.runAndWait()
                print("Null text directory")
            menu()            
                    
        case 'delete' | 'remove':
            showDirectories()
            if(showDirectories()==-1):
                engine.say("There are no text files to read...Please add TEXT files into the directory ")
                engine.runAndWait()
                print("\nYou have no text files to delete | You are redirected to the Main Menu")
                for i in range(0,4):
                    print(".."*(i+1))
                    time.sleep(0.3)
                menu()
            removalFile = input("Enter the file which you want to delete : ")
            removalFile = removalFile.strip()
            if removalFile =='exit':
                menu()
            deleteFile(removalFile)
            if flag==1:
                menu()
                
        case 'properties':
            showDirectories()
            fileName = input("Enter the file Name to alter the properties : ")
            if(checkExistingFileWithUserInput(f"{fileName}.txt",directoryList)):
                propertiesModule(fileName)
                print("Properties set successfully\n")
                viewProperties(fileName)
                
            else:
                print("File not found")
                   
        case 'recycle':
            directory =r"C:\Users\prath\python\recycleBin"
            recycleFiles = os.listdir(directory)
            if(len(recycleFiles)==0):
                print("There are no files to recycle")
                menu()
            else:
                print(recycleFiles)
                recycleFile = input("Enter the file name : ")
                if(recycleFile=='exit'):
                    menu()
                for file in recycleFiles:
                    recycleList.append(file)
                if(checkExistingFileWithUserInput(recycleFile,recycleList)==-1):
                    print("Enter the valid filename to recycle")
                    menu()
                else:
                    getContentOfRecycleBin(rf"{recycleFile}.txt")
                    # with open(fr"C:\Users\prath\python\recycleBin\{recycleFile}.txt") as f:
                    #     content = f.read()
                    #     recycleBin(recycleFile,content)
                    #     print("Recycle done")
                        
        case 'recyclefunctions' | 'recyclearea':
            print("Here is your recycle directory : ")
            directory = r'C:\Users\prath\python\recycleBin'
            deadFiles = os.listdir(directory)
            print(deadFiles)
            recyclePrompt = "Enter recycle to recycle the files | Enter delete to delete permanently"
            recycleUserChoice = input("Enter your choice : 'delete' for permanent deletion  [PLEASE ENTER 'exit' AT ANY TIME TO JUMP INTO THE MAIN MENU]\nInput :  ")
            if(recycleUserChoice=='exit'):
                menu()
            match recycleUserChoice:
                case 'recycle':
                    supplyUserInput('recycle')
                    menu()
                    
                case 'delete':
                    directory = r'C:\Users\prath\python\recycleBin'
                    deadFiles = os.listdir(directory)
                    print(deadFiles)
                    fileInputForPermanentDeletion = input("Enter the filename for deletion : ")
                    fileInputForPermanentDeletion+=".txt"
                    if fileInputForPermanentDeletion in deadFiles:
                        path = directory + rf'\{fileInputForPermanentDeletion}'
                        print(f"{fileInputForPermanentDeletion} found for the permanent deletion")
                        print("\nDeletion occuring")
                        loading()
                        os.remove(path)
                        print(rf"{fileInputForPermanentDeletion} deleted permanently from the System")
                    else:
                        print("You inputted wrong file name")
                        menu()    
                    
                case _:
                    print("Invalid choice\n")
                    menu()    
                        
            
        case _:
            engine.say("Invalid response")
            engine.runAndWait()
            print("!Invalid response!")
            menu()

dateTime()
welcomeTransition()
loading()                        
menu()