# Importing stuff
import os # Needed for many functions with creating and removing directories
from pydrive.auth import GoogleAuth # Needed for authenticating a google account
from datetime import datetime # Needed for getting the date
from pydrive.drive import GoogleDrive # Needed for uploading to Drive
import time # Needed for waiting in the program
from sys import exit # Needed to exit the program
import shutil # Needed to delete entire directories
import argparse

print("Reading arguments...")
parser = argparse.ArgumentParser(description = 'Bulk download posts from Reddit then upload them to Google Drive.')
parser.add_argument('-s', "--subreddit", help = "The name of the subreddit you want to download from (required)", required = True)
parser.add_argument('-a', "--amount", help = "How many posts you want to download from the chosen subreddit (required)", required = True)
parser.add_argument('-S', "--sortvar", help = "The type of sort you would like: hot (default), top, new, rising, controversial")
parser.add_argument('-t', "--sorttimevar", help = "The time period that you want to sort for: day (default), week, month, year")

args = parser.parse_args()

os.chdir("H:\\")

subreddit = args.subreddit
amount = args.amount
sortvar = args.sortvar
sorttimevar = args.sorttimevar

if not args.sortvar:
    sortvar = "hot"

if not args.sorttimevar:
    sorttimevar = "day"

print("Reading parent.txt...")
fa = open("parent.txt", 'r') # Opening parent.txt to read configuration
parent = fa.readline()
fa.close()

subreddit = subreddit.replace("\n", "")
amount = amount.replace("\n", "")
sortvar = sortvar.replace("\n", "")
sorttimevar = sorttimevar.replace("\n", "")
parent = parent.replace("\n", "") # Getting rid of new lines as to not confuse the computer ("What?! I need to get 100\n posts? I don't know what that is, so I'll just get the maximum amount!")
subreddit = subreddit.lower() # Lowercasing subreddit to remove config.dll errors and folder conflicts

print("Connecting to Google Drive...")
gauth = GoogleAuth()           
drive = GoogleDrive(gauth) # Setting up Drive and stuff
date = datetime.today().strftime('%Y-%m-%d') # Getting the date
command = "python -m bdfr download H:\Database\\" + date + "\ -s " + subreddit + " -L " + amount + " -S " + sortvar + " -t " + sorttimevar # The command for downloading the posts
directory = "H:\Database\\" + date + "\\" + subreddit + "\\" # The directory for the files to go to
deldir = "H:\Database\\" + date + "\\"

os.chdir("H:\Database") 

# Reading config.dll to see if you already used the tool today
print("Reading \Database\config.dll...")
if not os.path.isfile('H:\Database\config.dll'):
    print("\Database\config.dll not found! Creating...")
    fb = open('config.dll', 'x')
    fb.close()

f = open('config.dll', 'r')
for line in f:
    line = line.replace("\n", "")
    if line == date + " " + subreddit:
        print("You have already used the tool today in the selected subreddit! Check your Google Drive to access your files!")
        print("We wish that we were able to provide this tool for infinite uses every day, however we do not have this function to avoid errors and duplicates.")
        print("If this was done in error or you halted a download, modify H:\Database\config.dll to remove the chosen subreddit under today's date.")
        print("If you used r/" + subreddit + " today but halted the download, delete the directory and delete the line containing \"" + date + " " + subreddit + "\".")
        os.system("pause")
        exit()
f.close()

# Writing the date to config.dll
print("Writing to \Database\config.dll...")
fw = open('config.dll', 'a')
fw.write(date + " " + subreddit + "\n")
fw.close()

print("Creating temporary folder...")
folderExists = False
for folders in os.listdir("H:\Database"):
    if folders == date:
        print("Folder already exists!")
        folderExists = True

if not folderExists:
    os.mkdir(date)

print("Running download...")
os.system(command)

os.chdir("H:\\")

# Creating a folder with the date as its name
print("Checking if Google Drive folder exists...")

fileExists = False

file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % (parent)}).GetList()
for file1 in file_list:
  print('Searching folders... Title = %s, ID = %s' % (file1['title'], file1['id']))
  if file1['title'] == date:
      print("Google Drive folder already exists!")
      fileID = file1['id']
      fileExists = True

if not fileExists:
    folder_name = date
    folder = drive.CreateFile({'parents': [{'id': parent}], 'title' : folder_name, 'mimeType' : 'application/vnd.google-apps.folder'}) 
    folder.Upload()

    fileID = folder['id'] # ID of the newly created folder

fileExists = False

file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % (fileID)}).GetList()
for file2 in file_list:
  if not fileExists:
    print('Searching folders... Title = %s, ID = %s' % (file2['title'], file2['id']))
    if file2['title'] == date:
        print("Google Drive folder already exists!")
        fileID = file2['id']
        fileExists = True

if not fileExists:
    folder_name = subreddit
    folder = drive.CreateFile({'parents': [{'id': fileID}], 'title' : folder_name, 'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()

    fileID = folder['id']

fileID = folder['id']

# Uploading the files to Google Drive
time.sleep(5)

print("Uploading files to Google Drive...")
upload_file_list = os.listdir(directory)
for upload_file in upload_file_list:
    os.chdir("H:\Database\\" + date + "\\" + subreddit + "\\")
    gfile = drive.CreateFile({'parents': [{'id': fileID}]})
    gfile.SetContentFile(upload_file)
    try:
        gfile.Upload()
    finally:
        gfile.content.close()
    if gfile.uploaded:
        print("Uploaded " + upload_file + " successfully!")

os.chdir("H:\\") # Change the directory so we don't get an "In use" error!

# os.system("remove.py")

shutil.rmtree(deldir) # Delete the folder with all the files in it

# shutil.rmtree(directory)

# os.rmdir(deldir)

os.system('pause')