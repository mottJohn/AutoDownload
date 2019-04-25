import requests
import pandas as pd
from datetime import timedelta, date
import datetime
import time

now = datetime.datetime.now()
date_path = now.strftime("%Y%m")
path = r'P:\Hong Kong\ENL\PROJECTS\355482 HKIA 3RS ET Services\09 Env Monitoring\02 Impact Data\01 Air Quality & Noise\%s\Weather'%(date_path) + '\\'

datePrevious = datetime.datetime.now() - timedelta(days = 1)
date_string = datePrevious.strftime("%Y%m%d")

url_conc = 'http://www.aqhi.gov.hk/tc/aqhi/past-24-hours-pollutant-concentrationf322.html?stationid=78'
html_conc = requests.get(url_conc).content

while True:
	try:
		df_list_conc = pd.read_html(html_conc)
		df_conc = df_list_conc[1]
		df_conc.to_csv(path + date_string + '_conc.csv', encoding = "utf-8")

		url_aqhi = 'http://www.aqhi.gov.hk/tc/aqhi/past-24-hours-aqhif322.html?stationid=78'
		html_aqhi = requests.get(url_aqhi).content

		df_list_aqhi = pd.read_html(html_aqhi)
		df_aqhi = df_list_aqhi[2]
		df_aqhi.to_csv(path + date_string + '_aqhi.csv',encoding ='utf-8')
	
		break
		
	except:
		time.sleep(2)
		
