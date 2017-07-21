from Data import Scraper, table, SimpleScraper
from Data.Spreadsheets import List
from Util.reduction import reduce_params, simple_reduction
from Util.util import maxp
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from scipy.stats import multivariate_normal
from Calculate import error
from sklearn.qda import QDA
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
import copy
import math
import numpy
import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

''' Scraping Data '''
y = []
x = []


print 'Scraping data'
for sheet in List.sheets:
	print sheet
	data = SimpleScraper.scrape('Data/Spreadsheets/all-euro-data-' + sheet + '.xls')

	for i in range(0, len(data), 2):
		instance = []

		home_stats = copy.deepcopy(data[i])
		away_stats = copy.deepcopy(data[i + 1])
		simple_reduction(home_stats)
		simple_reduction(away_stats)

		instance.extend(home_stats)
		instance.extend(away_stats)
		x.append(instance)
		y.append(data[i][-1])

		instance = []
		instance.extend(away_stats)
		instance.extend(home_stats)
		x.append(instance)
		y.append(data[i + 1][-1])
	print 'Data formatted'

print 'Data Scraped\n'

print 'Converting...'

x = numpy.array(x)
#numpy.random.shuffle(x)
y = numpy.array(y)

print 'Normalizing data'
for j in range(len(x[0])):
	mean = numpy.mean(x[:, [j]])
	stand_dev = numpy.std(x[:, [j]])
	x[:, [j]] -= mean
	if stand_dev == 0:
		stand_dev = 1
	x[:, [j]] /= stand_dev
print 'Data Normalized\n'

size = len(x)
training_size = 9 * size / 10
if training_size % 2 == 1:
	training_size -= 1

# --- Regression ---
print 'Transforming Data'
poly = PolynomialFeatures(degree=3)
x_ = poly.fit_transform(x)
print 'Data transformed\n'

print 'Fitting data'
clf = linear_model.LinearRegression()
clf.fit(x_[0:training_size,:], y[0:training_size])
print 'Data fit\n'

print 'Predicting...'
y_predict = clf.predict(x_[training_size:size,:])

print 'Calculating error...'
error_rate = error.calc_error(y_predict, y[training_size:size])
print 'Success rate: ', error_rate

# Classification set up
y_home = []
all_data = []

for i in range(0, training_size, 2):
	data_instance = copy.deepcopy(x[i])

	if y[i] == y[i + 1]:
		y_home.append(2)
	elif y[i] > y[i + 1]:
		y_home.append(0)
	else:
		y_home.append(1)

	all_data.append(data_instance)

# --- QDA Classification ---
print 'Fitting data'
home_qda = QDA()
home_qda.fit(all_data, y_home)

correct = 0
print 'Predicting results: '
for i in range(training_size, size, 2):
	inst = x[i].reshape(1,-1)

 	ph = home_qda.predict(inst)

	if ph == 0:
		if y[i] > y[i + 1]:
			correct += 1

	elif ph == 2:
		if y[i] == y[i + 1]:
			correct += 1
	else:
		if y[i] < y[i + 1]:
			correct += 1

error_rate = (correct * 1.0) / ((size - training_size) / 2)
print 'Success rate: ', error_rate

# --- SVM
clf  =svm.SVC(kernel="sigmoid", degree=4)
clf.fit(all_data, y_home)
correct = 0
print 'Predicting results: '
for i in range(training_size, size, 2):
	inst = x[i].reshape(1,-1)

 	ph = clf.predict(inst)

	if ph == 0:
		if y[i] > y[i + 1]:
			correct += 1

	elif ph == 2:
		if y[i] == y[i + 1]:
			correct += 1
	else:
		if y[i] < y[i + 1]:
			correct += 1

error_rate = (correct * 1.0) / ((size - training_size) / 2)
print 'Success rate: ', error_rate

# --- RandomForestClassifier ---
clf = RandomForestClassifier(n_estimators=16)
clf = clf.fit(all_data, y_home)
correct = 0
print 'Predicting results: '
for i in range(training_size, size, 2):
	inst = x[i].reshape(1,-1)

 	ph = clf.predict(inst)

	if ph == 0:
		if y[i] > y[i + 1]:
			correct += 1

	elif ph == 2:
		if y[i] == y[i + 1]:
			correct += 1
	else:
		if y[i] < y[i + 1]:
			correct += 1

error_rate = (correct * 1.0) / ((size - training_size) / 2)
print 'Success rate: ', error_rate
