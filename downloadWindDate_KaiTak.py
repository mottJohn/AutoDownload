import requests
from datetime import timedelta, date
import datetime

url = 'https://maps.weather.gov.hk/r4/input_files/se_wd.csv'

proxies ={'http':'http://202.130.161.208'}

now = datetime.datetime.now()
date = now.strftime("%Y%m%d")
file_name = "r2c_wd_{}.csv".format(date)
directory = r"P:\Hong Kong\ENL\PROPOSALS\403329 Kai Tak Sports Park ET\Baseline Monitoring Report\Appendices\raw data\Data\Wind Data" +"\\"

r = requests.get(url, proxies=proxies)

with open(directory + file_name, "wb") as code:
	code.write(r.content)