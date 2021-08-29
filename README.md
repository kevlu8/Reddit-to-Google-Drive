# Reddit to Google Drive
Bulk download Reddit posts and upload to a Google Drive folder based on date. 
This program uses [PyDrive](https://pypi.org/project/PyDrive/) and [BDFR](https://github.com/aliparlakci/bulk-downloader-for-reddit) (Used in the DL folder, do not touch contents)

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
How many posts to get. Cannot be over 1000 due to api limitations

### Sort:
What type of sort to use. Hot, top, new, controversial, rising. Cannot be anything else.

### TimeSort:
Time period for sorting. Day, week, month, year, all. Cannot be anything else.

### Parent ID:
Drive folder ID of where the folders named by date should be put. This is the ID of a folder: ![image](https://user-images.githubusercontent.com/69993704/131234603-caf985f7-87f7-4129-9511-a220120c9f6a.png)
If you want it in your drive, put `root` here.


Run `start.bat` which will open a blank command prompt window inside of the H:\ directory. Then, type `get.py` and wait for it to finish downloading and uploading.

## How it works
First, the program uses BDFR to download Reddit posts, which can be images, gifs, videos, or even text! Then, it is put into a directory by date **coded by me!!! :)** After that, it is uploaded to Google Drive in a folder named in YYYY-MM-DD format. This entire project took around 3 hours to make the bare minimum of, and a more optimized version is still being developed!
