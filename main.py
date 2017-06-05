from Data import Scraper, table
from Data.Spreadsheets import List
from Util.reduction import reduce_params
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import copy
import numpy
import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

''' Scraping Data '''
y = []
x = []


print 'Scraping data'
for sheet in List.sheets:
	print sheet
	data = Scraper.scrape('Data/Spreadsheets/all-euro-data-' + sheet + '.xls')

	print 'Formatting Data'
	for i in range(len(data)):
		#only loop through for 10+ games
		for j in range(5, len(data[i])):
			instance = []

			# Append only the necessary values
			data_values = copy.deepcopy(data[i][j - 1])
			reduce_params(data_values)
			instance.extend(data_values)

			# Finding other instance
			for a in range(len(data)):
				if a == i:
					continue
				for b in range(len(data[i])):
					if data[i][j][table.GAME_ID] == data[a][b][table.GAME_ID]:
						break
				if data[i][j][table.GAME_ID] == data[a][b][table.GAME_ID]:
					break
			data_values = copy.deepcopy(data[a][b - 1])
			reduce_params(data_values)
			instance.extend(data_values)
			x.append(instance)
			y.append(data[i][j][table.L1_GOALS])
	print 'Data formatted\n'

print 'Data Scraped\n'

print len(x)
print 'Converting...'
x = numpy.array(x)
print 'Normalizing data'
for j in range(len(x[0])):
	mean = numpy.mean(x[:, [j]])
	stand_dev = numpy.std(x[:, [j]])

	x[j] -= mean
	x[j] /= stand_dev
print 'Data Normalized\n'

print 'Transforming Data'
poly = PolynomialFeatures(degree=2)
x_ = poly.fit_transform(x)
print 'Data transformed\n'

print 'Fitting data'
clf = linear_model.LinearRegression()
clf.fit(x_[0:60000,:], y[0:60000])
print 'Data fit\n'

print 'Predicting...'
y_predict = clf.predict(x_[60000:61404,:])
print y_predict

#print x_[0:500,:].shape
