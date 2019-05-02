import requests
from datetime import timedelta, date
import datetime

url = 'https://www.epd.gov.hk/epd/misc/cdm/chit/CWDCS-web-Basic-{}.xls'

proxies ={'http':'http://202.130.161.208'}

datePrevious = datetime.datetime.now() - timedelta(days = 1)
date_string = datePrevious.strftime("%Y%m%d")

file_name = 'CWDCS-web-Basic-' + date_string + '.xls'
directory = r'C:\Users\CHA82870\Mott MacDonald\Lam, Julian - Landfill Disposal Record' + '\\'
url_filled = url.format(date_string)

r = requests.get(url_filled, proxies=proxies, verify = False)

with open(directory + file_name, "wb") as code:
	code.write(r.content)