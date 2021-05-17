### Problem Statement 
'''
A F&B manager wants to determine whether there is any significant difference in the 
diameter of the cutlet between two units. A randomly selected sample of cutlets 
was collected from both units and measured? Analyze the data and draw inferences 
at 5% significance level. Please state the assumptions and tests that you 
carried out to check validity of the assumptions.
'''

### Solution 
alpha = 0.05 # From the problem statement

# Import necessary libraries
import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Load Cutlets.csv file as pandas dataframe
Cutlets = pd.read_csv('Cutlets.csv')

# View Data
print(Cutlets.head())

# Check the dimension of the dataframe
print('\n' + 'Shape of Cutlets dataframe is {shape}'.format(shape = Cutlets.shape)) # 35 rows and 2 columns

# Check if there are any null values
# print(Cutlets.notna().count()) # There are no null values in our dataframe

# Check the data distribution using various plots
plt.figure(figsize=(20,10)) 
plt.subplot(2,3,2)
plt.hist(Cutlets['Unit A'], density=True)
plt.title('Histogram of Unit A')

plt.subplot(2,3,5)
plt.hist(Cutlets['Unit B'], density=True)
plt.title('Histogram of Unit B')

plt.subplot(2,3,3)
plt.boxplot(Cutlets['Unit A'], vert=False)
plt.title('Boxplot of Unit A')

plt.subplot(2,3,6)
plt.boxplot(Cutlets['Unit B'], vert=False)
plt.title('Boxplot of Unit B')

plt.subplot(2,3,1)
stats.probplot(Cutlets['Unit A'], plot=plt)
plt.title('Normal Q-Q plot of Unit A')

plt.subplot(2,3,4)
stats.probplot(Cutlets['Unit B'], plot=plt)
plt.title('Normal Q-Q plot of Unit B')


plt.show() # Data looks normal from the graphs

print('\n' + "Both the Unit A, Unit B seems to be Normally distributed as observed from the Graphs")

for columnName, columnData in Cutlets.iteritems():
	print('\n' + "*** Measures of central tendency, dispersion for '{}' ***".format(columnName))
	print("Mean: {:0.3f}".format(np.average(columnData.values)))
	print("Median: {:0.3f}".format(np.median(columnData.values)))
	print("Mode: {}".format(stats.mode(columnData.values)[0]))
	print("Variance: {:0.3f}".format(np.var(columnData.values)))
	print("Standard Deviation: {:0.3f}".format(np.std(columnData.values)))
	print("Range: {:0.3f}".format(max(columnData.values)-min(columnData.values)))

# Mean, Median are nearly same, so the data could be Normally distributed.

# # # Shapiro test to check if data is normally distributed
# unitA_ShapiroTest = stats.shapiro(Cutlets['Unit A'])
# unitB_ShapiroTest = stats.shapiro(Cutlets['Unit B'])
# print('\n'+"P value from Shapiro test results of Unit A is: {}".format(unitA_ShapiroTest[1]))
# print("P value from Shapiro test results of Unit B is: {}".format(unitB_ShapiroTest[1])) # Both are normally distributed as p>alpha

# Normality test
# Defining our Null, and Alternate hypothesis
Ho = 'data is Normally distributed'
Ha = 'data is not Normally distributed'
# P high Ho Fly (Accept Null Hypothesis)
# P low Ho Go (Reject Null Hypothesis)

# Def a function to check if data is Normal by applying Shapiro test
def check_normality(df):
	for columnName, columnData in Cutlets.iteritems():
		print('\n' + "*** Shapiro Test Results of '{}' ***".format(columnName))
		p = round(stats.shapiro(columnData.values)[1], 2)

		if p>alpha:
			print("{p} > {alpha}. We fail to reject Null Hypothesis. '{columnName}' {Ho}".format(p=p, alpha=alpha, columnName=columnName, Ho=Ho))
		else:
			print("{p} <= {alpha}. We reject Null Hypothesis. '{columnName}' {Ha}".format(p=p, alpha=alpha, columnName=columnName, Ha=Ha))

check_normality(Cutlets)


### Variance Test by using stats.levene()
# Defining our Null, and Alternate hypothesis
Ho = 'Variance of Unit A is approximately equal to Variance of Unit B'
Ha = 'Variance of Unit A is not equal to Variance of Unit B'

def check_variances(df):
	print('\n' + "*** Variances Test Results' ***")
	p = round(stats.levene(Cutlets['Unit A'], Cutlets['Unit B'])[1],2)

	if p>alpha:
		print("{p} > {alpha}. We fail to reject Null Hypothesis. {Ho}".format(p=p, alpha=alpha, Ho=Ho))
	else:
		print("{p} <= {alpha}. We reject Null Hypothesis. {Ha}".format(p=p, alpha=alpha, Ha=Ha))

check_variances(Cutlets)

# X (A, B) is 2(Discrete) and Y(diameter) is Continuous. 
# Y1, Y2 follows Normal Distribution and have equal variances. 
# So we go for 2 Sample T Test for Equal Variances

# Defining our Null, and Alternate hypothesis
Ho = 'Avg of Diameter of Unit A is equal to Avg of diameter of Unit B'
Ha = 'Avg of Diameter of Unit A is not equal to Avg of diameter of Unit B'

# arrays = []

def t_test(df):
	print('\n' + "*** 2 Sample T Test Results ***")
	# arr1 = np.array(Cutlets['Unit A'])
	# arr2 = np.array(Cutlets['Unit B'])
	# arrays = [arr1, arr2]
	# print(arrays)
	# p = round(stats.ttest_ind(*arrays, equal_var=True)[0], 2)
	test_results = stats.ttest_ind(Cutlets['Unit A'], Cutlets['Unit B'], equal_var=True)
	# print(test_results)
	p = round(test_results[1],2)

	if p>alpha:
		print("{p} > {alpha}. We fail to reject Null Hypothesis. {Ho}".format(p=p, alpha=alpha, Ho=Ho))
	else:
		print("{p} <= {alpha}. We reject Null Hypothesis. {Ha}".format(p=p, alpha=alpha, Ha=Ha))

t_test(Cutlets)