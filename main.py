from Data import Scraper
from Data.Spreadsheets import List

''' Scraping Data '''
sum = 0

print 'Scraping data'
for sheet in List.sheets:
	print sheet
	data = Scraper.scrape('Data/spreadsheets/all-euro-data-' + sheet + '.xls')
	for i in range(len(data)):
		sum += len(data[i])
sum /= 2

print
print sum
