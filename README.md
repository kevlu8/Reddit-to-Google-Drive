# Reddit to Google Drive
Bulk download Reddit posts and upload to a Google Drive folder based on date. 
This program uses [PyDrive](https://pypi.org/project/PyDrive/) and [BDFR](https://github.com/aliparlakci/bulk-downloader-for-reddit)

## Setup
### This code is terrible, and requires many specific circumstances. If you do not want to go through all of this, watch this repo and wait for me to make it better.

You'll need Python version 3.9+ for this.

First, create a separate partition with ~10 GB of storage. Call it H:\
![image](https://user-images.githubusercontent.com/69993704/131233892-eb61c30c-2817-4247-b453-673033acbbfd.png)

Next, extract this repository's contents into H:\

Now, open up command prompt and type `python -m pip install bdfr --upgrade` and also `python -m pip install PyDrive`. These are required for the program to run. The rest will be done by the program!

## Use
Open `config.txt` and modify it to your preferences. **DO NOT LEAVE ANY OF THESE BLANK OR EVERYTHING WILL BREAK.** Here's the format:
```
Subreddit
Post amount
Sort
TimeSort
Parent ID
``` 
### Subreddit:
Which sub to get posts from. Do not include the `r/`, only include the name. For instance, `pics`

### Post Amount:
How many posts to get. Cannot be over 1000 due to api limitations.

### Sort:
What type of sort to use. Hot, top, new, controversial, rising. Cannot be anything else. If you're indecisive, `Hot` is the default sort.

### TimeSort:
Time period for sorting. Day, week, month, year, all. Cannot be anything else. If you're indecisive, `Day` is the default sort.

### Parent ID:
Drive folder ID of where the folders named by date should be put. This is the ID of a folder: 

![image](https://user-images.githubusercontent.com/69993704/131234603-caf985f7-87f7-4129-9511-a220120c9f6a.png)

If you want it in your `My Drive`, put `root` here.

Here's an example of a good `config.txt` file:
```
memes
100
top
day
1-1xxSMUmeZdoKwst052yTzMgcDcT-ZGC
```

Now, go to the [Google Developer Console](https://console.developers.google.com/) and create a new project. ![image](https://user-images.githubusercontent.com/69993704/131235246-0b90f44b-8104-4fc5-bd49-71548713cf93.png)

Name it whatever you want then click Create. 

![image](https://user-images.githubusercontent.com/69993704/131235253-467aeb5a-6ec5-432e-b747-ee7071aa9c9b.png)

Now, click on "Enable APIs and Services"

![image](https://user-images.githubusercontent.com/69993704/131235291-6688e03e-d783-421f-960d-c35d42449c5a.png)

Search for Google Drive and enable Google Drive API

![image](https://user-images.githubusercontent.com/69993704/131235309-aac10fa4-27b3-4ccd-bd96-ac968dc87303.png)
![image](https://user-images.githubusercontent.com/69993704/131235315-44ba89eb-a448-4292-ae55-d851da1afaaf.png)

After you get redirected to this screen, click on "Create Credentials" ![image](https://user-images.githubusercontent.com/69993704/131235324-6312e5f1-60b7-4641-a75b-979650f03a3d.png)

Choose these settings: 
![image](https://user-images.githubusercontent.com/69993704/131235331-9c6eb152-00df-4506-aa52-dbba2f8a6a73.png) then click next.

Here, you can name your app whatever you want and enter your email in the 2 fields. Also pick an icon. ![image](https://user-images.githubusercontent.com/69993704/131235349-cc236206-fa99-4a54-b683-20b4d12feee7.png) I'm using a throwaway email so there's no need to try to email me.

When it asks you for scopes, just ignore it and click continue.

In OAuth Client ID, pick these settings: 

![image](https://user-images.githubusercontent.com/69993704/131235361-15c1b05c-6d04-45d4-96df-432f76b5192e.png)

When you see this, click done. ![image](https://user-images.githubusercontent.com/69993704/131235365-cfd81c76-06f1-4dc7-8ce7-858d4dbd6ad6.png)

Now, download the JSON. It will be named something really long. Just change that to `client_secrets.json` and move it to H:\

![image](https://user-images.githubusercontent.com/69993704/131235371-ead83281-8042-4c88-9dff-cee47021901a.png)

Go to "OAuth consent screen" and add yourself as a test user.

![image](https://user-images.githubusercontent.com/69993704/131235418-cbeb7511-349f-4b71-a5ab-eaa000373148.png)

![image](https://user-images.githubusercontent.com/69993704/131235426-0e4d0f18-28dd-4e1d-bb31-37bc224615e4.png)

Now, go to `settings.yaml` and change the client_id to your client id and the client_secret to your client secret (both are in `client_secrets.json`)

Your H:\ should now look like this:

![image](https://user-images.githubusercontent.com/69993704/131235452-4515b42e-d191-4d39-be35-d7554185ecb0.png)


Run `start.bat` which will open a blank command prompt window inside of the H:\ directory. Then, type `get.py` and wait for it to finish downloading. Once it finishes, it will prompt you to log in. Just select the account where you want the files to be uploaded and allow access. Then, it will upload. 

## How it works
First, the program uses BDFR to download Reddit posts, which can be images, gifs, videos, or even text! Then, it is put into a directory by date **coded by me!!! :)** After that, it is uploaded to Google Drive in a folder named in YYYY-MM-DD format. This entire project took around 3 hours to make the bare minimum of, and a more optimized version is still being developed!
