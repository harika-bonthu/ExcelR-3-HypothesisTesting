# Problem Statement
'''
TeleCall uses 4 centers around the globe to process customer order forms. 
They audit a certain %  of the customer order forms. Any error in order form renders it defective and has to be reworked before processing.  
The manager wants to check whether the defective %  varies by centre. 
Please analyze the data at 5% significance level and help the manager draw appropriate inferences
'''

# Solution
alpha = 0.05 # From the problem statement

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load the Costomer+OrderForm.csv as pandas dataframe
CustOrderForm = pd.read_csv('Costomer+OrderForm.csv')

#View Data
print(CustOrderForm.head())

# print(CustOrderForm.describe())

# Shape of dataframe
print(CustOrderForm.shape) # 300 rows and 4 columns

for columnName, columnData in CustOrderForm.iteritems():
	print('\n'+"Value counts of column {}".format(columnName))
	print(columnData.value_counts())


# Defining our Null, Alternate Hypothesis
Ho = 'Defective %  across the centers is same'
Ha = 'Defective %  across the centres is not same'
def chi_square(df):
	errorFree = [271, 267, 269, 280]
	Defective = [29,33, 31, 20]
	table = [errorFree, Defective]
	# print(table)

	stat, p, dof, expected = stats.chi2_contingency(table)
	# print(test)
	p = round(p, 2)

	print('\n'+"Inference from P Value")
	if p>alpha:
		print("{p} is greater than {alpha}. We fail to reject Null Hypothesis. {Ho}".format(p=p, alpha=alpha, Ho=Ho))
	else:
		print("{p} less than {alpha}. We reject Null Hypothesis. {Ha}".format(p=p, alpha=alpha, Ha=Ha))

	# If p<=alpha, reject Ho. Hence, there is a relation between the two categorical variables
	# else, retain Ho. Hence, there is no relation between the two categorical variables 

	Hnull = 'There is no relation between the categorical variables'
	Halt = 'There is a relation between the categorical variables'
	# Computing the critical values
	critical = stats.chi2.ppf(q=1-alpha, df=dof)
	
	print('\n'+"Inference from Critical Value")

	if critical>stat:
		print("{critical} is greater than {stat}. We fail to reject Null Hypothesis. {Hnull}".format(critical=round(critical,2), stat=round(stat, 2), Hnull=Hnull))
	else:
		print("{critical} less than {stat}. We reject Null Hypothesis. {Halt}".format(critical=round(critical,2), stat=round(stat, 2), Halt=Halt))

	# If critical<=stat, reject Ho. Hence, there is a relation between the two categorical variables
	# else, retain Ho. Hence, there is no relation between the two categorical variables 

chi_square(CustOrderForm)