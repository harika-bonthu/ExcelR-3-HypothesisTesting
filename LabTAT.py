### Problem Statement 
'''
A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT) of reports 
of the laboratories on their preferred list. They collected a random sample and recorded TAT for reports of 4 laboratories. 
TAT is defined as sample collected to report dispatch.   

Analyze the data and determine whether there is any difference in average TAT among the different laboratories at 5% significance level.
'''

### Solution 
alpha = 0.05 # From the problem statement

# Import necessary libraries
import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Load LabTAT.csv file as pandas dataframe
LabTAT = pd.read_csv('LabTAT.csv')

# View Data
print(LabTAT.head())

# Check the dimension of the dataframe
print('\n' + 'Shape of LabTAT dataframe is {shape}'.format(shape = LabTAT.shape)) # 120 rows and 4 columns

# Check if there are any null values
# print(LabTAT.notna().count()) # There are no null values in our dataframe

# Check the data distribution using various plots
plt.figure(figsize=(20,10)) 

plt.subplot(4,3,1)
stats.probplot(LabTAT['Laboratory 1'], plot=plt)
plt.title('Normal Q-Q plot of Laboratory 1')

plt.subplot(4,3,2)
plt.hist(LabTAT['Laboratory 1'], density=True)
plt.title('Histogram of Laboratory 1')

plt.subplot(4,3,3)
plt.boxplot(LabTAT['Laboratory 1'], vert=False)
plt.title('Boxplot of Laboratory 1')

plt.subplot(4,3,4)
stats.probplot(LabTAT['Laboratory 2'], plot=plt)
plt.title('Normal Q-Q plot of Laboratory 2')

plt.subplot(4,3,5)
plt.hist(LabTAT['Laboratory 2'], density=True)
plt.title('Histogram of Laboratory 2')

plt.subplot(4,3,6)
plt.boxplot(LabTAT['Laboratory 2'], vert=False)
plt.title('Boxplot of Laboratory 2')

plt.subplot(4,3,7)
stats.probplot(LabTAT['Laboratory 3'], plot=plt)
plt.title('Normal Q-Q plot of Laboratory 3')

plt.subplot(4,3,8)
plt.hist(LabTAT['Laboratory 3'], density=True)
plt.title('Histogram of Laboratory 3')

plt.subplot(4,3,9)
plt.boxplot(LabTAT['Laboratory 3'], vert=False)
plt.title('Boxplot of Laboratory 3')

plt.subplot(4,3,10)
stats.probplot(LabTAT['Laboratory 4'], plot=plt)
plt.title('Normal Q-Q plot of Laboratory 4')

plt.subplot(4,3,11)
plt.hist(LabTAT['Laboratory 4'], density=True)
plt.title('Histogram of Laboratory 4')

plt.subplot(4,3,12)
plt.boxplot(LabTAT['Laboratory 4'], vert=False)
plt.title('Boxplot of Laboratory 4')

plt.show() # Data looks normal from the graphs

# print('\n' + "All the columns of LabTAT seem to be Normally distributed as observed from the Graphs")

for columnName, columnData in LabTAT.iteritems():
	print('\n' + "*** Measures of central tendency, dispersion for '{}' ***".format(columnName))
	print("Mean: {:0.3f}".format(np.average(columnData.values)))
	print("Median: {:0.3f}".format(np.median(columnData.values)))
	print("Mode: {}".format(stats.mode(columnData.values)[0]))
	print("Variance: {:0.3f}".format(np.var(columnData.values)))
	print("Standard Deviation: {:0.3f}".format(np.std(columnData.values)))
	print("Range: {:0.3f}".format(max(columnData.values)-min(columnData.values)))


# Normality Test
# Defining our Null, and Alternate hypothesis
Ho = 'data is Normally distributed'
Ha = 'data is not Normally distributed'
# P high Ho Fly (Accept Null Hypothesis)
# P low Ho Go (Reject Null Hypothesis)

# Def a function to check if data is Normal by applying Shapiro test
def check_normality(df):
	for columnName, columnData in df.iteritems():
		print('\n' + "*** Shapiro Test Results of '{}' ***".format(columnName))
		p = round(stats.shapiro(columnData.values)[1], 2)

		if p>alpha:
			print("{p} is > {alpha}. We fail to reject Null Hypothesis. '{columnName}' {Ho}".format(p=p, alpha=alpha, columnName=columnName, Ho=Ho))
		else:
			print("{p} <= {alpha}. We reject Null Hypothesis. '{columnName}' {Ha}".format(p=p, alpha=alpha, columnName=columnName, Ha=Ha))

check_normality(LabTAT) # All the four columns are normally distributed


### Variance Test by using stats.levene()
# Defining our Null, and Alternate hypothesis
Ho = 'All Variances are equal'
Ha = 'All Variances are not equal'

def check_variances(df):
	print('\n' + "*** Variances Test Results' ***")
	p = round(stats.levene(LabTAT['Laboratory 1'], LabTAT['Laboratory 2'], LabTAT['Laboratory 3'], LabTAT['Laboratory 4'])[1],3)

	if p>alpha:
		print("{p} is > {alpha}. We fail to reject Null Hypothesis. {Ho}".format(p=p, alpha=alpha, Ho=Ho))
	else:
		print("{p} <= {alpha}. We reject Null Hypothesis. {Ha}".format(p=p, alpha=alpha, Ha=Ha))

check_variances(LabTAT)

# Output(Y) TAT is continuous and follows Normal distribution with equal variances
# X factor is discrete (and more than 2) 
# So we go for one-way ANOVA test 

# Defining our Null, and Alternate hypothesis
Ho = 'Avg Turn Around Time (TAT) of reports of the laboratories are same'
Ha = 'Avg Turn Around Time (TAT) of reports of the laboratories are not same'

def f_oneway(df):
	print('\n' + "*** one-way ANOVA test Results ***")
	test_res = stats.f_oneway(LabTAT['Laboratory 1'], LabTAT['Laboratory 2'], LabTAT['Laboratory 3'], LabTAT['Laboratory 4'])
	# p = round(stats.f_oneway(LabTAT['Laboratory 1'], LabTAT['Laboratory 2'], LabTAT['Laboratory 3'], LabTAT['Laboratory 4'])[1])
	p = round((test_res)[1], 2)
	# print(p)
	if p>alpha:
		print("{p} > {alpha}. We fail to reject Null Hypothesis. {Ho}".format(p=p, alpha=alpha, Ho=Ho))
	else:
		print("{p} <= {alpha}. We reject Null Hypothesis. {Ha}".format(p=p, alpha=alpha, Ha=Ha))

f_oneway(LabTAT)