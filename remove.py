import os
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')

os.chdir("H:\\")

os.system("del /f /q /s H:\Database\\")

os.chdir("H:\Database\\")

os.rmdir(date)