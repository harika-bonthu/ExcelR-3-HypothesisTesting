### Problem Statement 
'''
Sales of products in four different regions is tabulated for males and females. 
Find if male-female buyer rations are similar across regions.
'''

### Solution 
alpha = 0.05

# Import necessary libraries
import pandas as pd 
from scipy import stats
import numpy as np

# Load BuyerRatio.csv file as pandas dataframe
BuyerRatio = pd.read_csv('BuyerRatio.csv')

# View Data
print(BuyerRatio.head())

# Check the dimension of the dataframe
print('\n' + 'Shape of BuyerRatio dataframe is {shape}'.format(shape = BuyerRatio.shape)) # 2 rows and 5 columns

# We have 4 discrete inputs (East, West, North, South)
# Ouput is also discrete
# So we go for Chi-Square test

# Defining our Null, Alternate hypothesis
Ho = "Male-Female buyer rations are similar across regions"
Ha = "Male-Female buyer rations are not similar across regions"

def chi_square(df):
	Males = [50, 142, 131, 70]
	Females = [435,1523, 1356, 750]
	table = [Males, Females]
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

chi_square(BuyerRatio)