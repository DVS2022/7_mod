import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def take_rates():

	page = requests.get('https://mfd.ru/currency/?currency=USD')
	soup = BeautifulSoup(page.text, 'html.parser')
	data = soup.find('table', {'class': 'mfd-table mfd-currency-table'})
	data_list = data.find_all('td')
	
	dates, rates = sort_rates(data_list)

	visual_graph(dates, rates)

def sort_rates(data_list):

	rates = [float(str(data_list[i-1])[4: -5]) for i in range(len(data_list)-1, 3, -3)]
	dates = [str(data_list[i-2])[6: -5] for i in range(len(data_list)-1, 3, -3)]
	return dates, rates

def visual_graph(dates, rates):

	x, ax = plt.subplots()
	ax.xaxis.set_major_locator(MaxNLocator(6))
	ax.grid(True)
	ax.set_title('Курс USD/RUB', fontsize=20)
	ax.set_xlabel('Дата', fontsize=12)
	ax.set_ylabel('Курс, руб', fontsize=12)
	ax.plot(dates, rates)

	plt.show()
	

take_rates()