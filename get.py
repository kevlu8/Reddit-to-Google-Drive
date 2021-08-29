# Importing stuff
import os # Needed for many functions with creating and removing directories
from pydrive.auth import GoogleAuth # Needed for authenticating a google account
from datetime import datetime # Needed for getting the date
from pydrive.drive import GoogleDrive # Needed for uploading to Drive
import time # Needed for waiting in the program
from sys import exit # Needed to exit the program

os.chdir("H:\\")
fa = open("config.txt", 'r') # Opening config.txt to read configuration
subreddit = fa.readline()
amount = fa.readline()
sortvar = fa.readline()
sorttimevar = fa.readline()
parent = fa.readline()
fa.close() 

subreddit = subreddit.replace("\n", "")
amount = amount.replace("\n", "")
sortvar = sortvar.replace("\n", "")
sorttimevar = sorttimevar.replace("\n", "")
parent = parent.replace("\n", "") # Getting rid of new lines as to not confuse the computer ("What?! I need to get 100\n posts? I don't know what that is, so I'll just get the maximum amount!")

gauth = GoogleAuth()           
drive = GoogleDrive(gauth) # Setting up Drive and stuff
date = datetime.today().strftime('%Y-%m-%d') # Getting the date
command = "python -m bdfr download H:\Database\\" + date + "\ -s " + subreddit + " -L " + amount + " -S " + sortvar + " -t " + sorttimevar # The command for downloading the posts
directory = "H:\Database\\" + date + "\\" + subreddit + "\\" # The directory for the files to go to

os.chdir("H:\Database") 

# Reading config.dll to see if you already used the tool today
if not os.path.isfile('H:\Database\config.dll'):
   open('config.dll', 'x')

f = open('config.dll', 'r')
for line in f:
    line.replace("\n", "")
    if line == date:
        print("You have already used the tool today! Check your Google Drive to access your files!")
        print("We wish that we were able to provide this tool for infinite uses every day, however we do not have this function to avoid errors and duplicates.")
        print("If this was done in error or you halted a download, modify H:\Database\config.dll to remove today's date.")
        os.system("pause")
        exit()
f.close()

# Writing the date to config.dll
fw = open('config.dll', 'a')
fw.write(date + "\n")
fw.close()
os.mkdir(date)
os.system(command)

os.chdir("H:\\")

# Creating a folder with the date as its name
folder_name = date
folder = drive.CreateFile({'parents': [{'id': parent}], 'title' : folder_name, 'mimeType' : 'application/vnd.google-apps.folder'}) 
folder.Upload()

fileID = folder['id'] # ID of the newly created folder

# Uploading the files to Google Drive
upload_file_list = os.listdir(directory)
for upload_file in upload_file_list:
    os.chdir("H:\Database\\" + date + "\\" + subreddit + "\\")
    gfile = drive.CreateFile({'parents': [{'id': fileID}]})
    gfile.SetContentFile(upload_file)
    print("Uploading " + upload_file + "...")
    gfile.Upload()

os.chdir("H:\\") # Change the directory so we don't get an "In use" error!

time.sleep(10)

os.rmdir(directory) # Delete the folder with all the files in it

print("Done uploading to drive and removing the directory! Press any key to quit.")

os.system("pause")