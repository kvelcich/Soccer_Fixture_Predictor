# Soccer Fixture Predictor
Machine Learning program to predict soccer game results using the football-data.co.uk dataset for training.

Below shows the final error rates for the different learning methods used after optimization:

| SVM Linear | SVM RBF | Polynomial Regression | Random Forests | SVM Poly | QDA | SVM Sigmoid |
| --- | --- | --- | --- | --- | --- | --- |
| 42.49% | 43.14% | 44.21% | 44.31% | 46.49% | 48.97% | 58.7% |

![Alt text](http://velci.ch/images/Results.png)


[Read full setup, results and analysis here.](http://velci.ch/files/Predicting_Soccer_Match_Results.pdf)

## Required Libraries
This program is dependent on the python libraries: **xlrd** for parsing the excel data files, **scikit-learn** and **SciPy** for implementing the machine learning algorithms.

## How To Run
#### 1. Install Python
To install python, download and install a python version from [here.](https://www.python.org/downloads/)

#### 2. Install pip
Next, in order to download the required libraries, install pip following the directions at [pypa.io](https://pip.pypa.io/en/stable/installing/).

#### 3. Install xlrd
Once pip is installed correctly, in order to install the xlrd library simply run the following command:
```
pip install xlrd
```

#### 4. Install scikit-learn
Next, install scikit-learn using the following command:
```
pip install sklearn
```

#### 5. Install SciPy
Lastly, install SciPy using the following command:
```
pip install scipy
```

#### 6. Download Files
You can download this project by using the following command:
```
git clone https://github.com/kvelcich/Soccer_Fixture_Predictor
```

#### 7. Edit Main, and Run
To run the program, in the main directory of the project, run the following command:
```
python main.py
```
You can also dig around, editing the hyperparameters and the range of the inputs given to the algorithms in order to achieve differing results.
