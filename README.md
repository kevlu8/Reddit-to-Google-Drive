# Reddit to Google Drive
Bulk download Reddit posts and upload to a Google Drive folder based on date
This program uses [PyDrive](https://pypi.org/project/PyDrive/) and [BDFR](https://github.com/aliparlakci/bulk-downloader-for-reddit) (Used in the DL folder, do not touch contents)

## Setup
### This code is terrible, and requires many specific circumstances. If you do not want to go through all of this, watch this repo and wait for me to make it better.

First, create a separate partition with ~10 GB of storage. Call it H:\
![image](https://user-images.githubusercontent.com/69993704/131233892-eb61c30c-2817-4247-b453-673033acbbfd.png)

Next, extract this repository's contents into H:\

Now, open up command prompt and type `python -m pip install bdfr --upgrade` and also `python -m pip install PyDrive`. These are required for the program to run. The rest will be done by the program!

## Use
You will need to create a bunch of complicated stuff that I will talk about later
Run `start.bat` which will open a blank command prompt window inside of the H:\ directory. Then, type `get.py` and wait for it to finish downloading and uploading.
