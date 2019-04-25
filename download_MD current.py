import requests
from datetime import timedelta, date
import datetime

url = 'http://current.hydro.gov.hk/en/download_csv.php?start_dt={}%20{}:00&end_dt={}%20{}:00&mode=Surface'

proxies ={'http':'http://202.130.161.208'}

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
date_s = date.replace('-','')
date_path = now.strftime("%Y%m")
file_name = date_s +'000000-'+ date_s +'234500-Surface.csv'
directory = 'P:/Hong Kong/ENL/PROJECTS/355482 HKIA 3RS ET Services/09 Env Monitoring/02 Impact Data/06 High Speed Ferry/%s/MD Current Data/'%(date_path)
url_filled = url.format(date, "00:00", date, "23:45")

r = requests.get(url_filled, proxies=proxies)

with open(directory + file_name, "wb") as code:
	code.write(r.content)