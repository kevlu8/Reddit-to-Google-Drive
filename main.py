from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import praw
import argparse
import json
import os
import requests

def dlfile(url, filename):
	with open(filename, 'wb') as f:
		f.write(requests.get(url).content)

parser = argparse.ArgumentParser(description='Download images from reddit and upload to google drive')
parser.add_argument("-s", "--subreddit", type=str, help='subreddit to download from (default: home)')
parser.add_argument("-n", "--number", type=int, help='number of images to download', default=10)
parser.add_argument("-k", "--keep", action='store_true', help='keep images after upload')

with open("parent.txt", "r") as f:
	parent_id = f.read()

args = parser.parse_args()

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# read auth.json for reddit credentials
with open('auth.json') as f:
	data = json.load(f)
	client_id = data['client_id']
	client_secret = data['client_secret']
	user_agent = data['user_agent']
	username = data['username']
	password = data['password']

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent, username=username, password=password)

if not os.path.exists('images'):
	os.mkdir('images')

if args.subreddit:
	subreddit = reddit.subreddit(args.subreddit)
	for sub in subreddit.hot(limit=args.number):
		if sub.url.endswith('.jpg') or sub.url.endswith('.png'):
			filename = sub.url.split('/')[-1]
			dlfile(sub.url, "images/" + filename)
			file = drive.CreateFile({'title': filename, 'parents': [{'id': parent_id}]})
			file.SetContentFile("images/" + filename)
			file.Upload()
			file.content.close()
			if not args.keep:
				os.remove("images/" + filename)
else:
	# for each subreddit in the user's home page
	for subreddit in reddit.user.subreddits(limit=None):
		subreddit = reddit.subreddit(subreddit.display_name)
		for sub in subreddit.hot(limit=args.number):
			if sub.url.endswith('.jpg') or sub.url.endswith('.png'):
				filename = sub.url.split('/')[-1]
				dlfile(sub.url, "images/" + filename)
				file = drive.CreateFile({'title': filename, 'parents': [{'id': parent_id}]})
				file.SetContentFile("images/" + filename)
				file.Upload()
				file.content.close()
				if not args.keep:
					os.remove("images/" + filename)
if not args.keep:
	os.rmdir('images')

print("Done")