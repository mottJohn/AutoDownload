import requests
from datetime import timedelta, date
import datetime

url = 'https://maps.weather.gov.hk/r4/input_files/r2c_wd.csv'

proxies ={'http':'http://202.130.161.208'}

now = datetime.datetime.now()
date = now.strftime("%Y%m%d")
file_name = "r2c_wd_{}.csv".format(date)
directory = r"C:\Users\CHA82870\Mott MacDonald\Contract 3101 - 3RS ET Service - Do\09 Environmental Monitoring\02 Impact Data\01 Air Quality and Noise\Wind Data" +"\\"

r = requests.get(url, proxies=proxies)

with open(directory + file_name, "wb") as code:
	code.write(r.content)