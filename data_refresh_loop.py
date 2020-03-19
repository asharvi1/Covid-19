import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time
from apscheduler.schedulers.blocking import BlockingScheduler

df = 0

def get_data():
	global df
	url = "https://www.worldometers.info/coronavirus/"
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	table = soup.find(name = 'table', attrs = {'id': 'main_table_countries'})

	df = pd.read_html(str(table))[0]
	df = df.iloc[:-1, :]
	df = df[['Country,Other', 'TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases', 'Serious,Critical']]


scheduler = BlockingScheduler()
scheduler.add_job(get_data, 'interval', hours = 1)
scheduler.start()




