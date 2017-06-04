from Data import Scraper, table
from Data.Spreadsheets import List
import numpy

''' Scraping Data '''
sum = 0

print 'Scraping data'
for sheet in List.sheets:
	print sheet
	data = Scraper.scrape('Data/Spreadsheets/all-euro-data-' + sheet + '.xls')

print 'Data Scraped\n'


print 'Formatting Data'
y = []
x = []
for i in range(len(data)):
	#only loop through for 10+ games
	for j in range(len(data[i])):
		instance = []

		# Append only the necessary values
		instance.extend(data[i][j - 1][1:93])

		# for a in range(len(data)):
		# 	for b in range(len(data)):
		# 		if a == i:
		# 			continue
		# 		if data[i][j][table.GAME_ID] == data[a][b][table.GAME_ID]:
		# 			print 'found'
		# print 'search\n'

		y.append(data[i][j][table.L1_GOALS])
		break
	break
print 'Data formatted\n'

l = []
for i in range(len(data)):
	for j in range(len(data[i])):
		if data[i][j][table.GAME_ID]) not in l
			l.append(data[i][j][table.GAME_ID])
		else:
			print l
