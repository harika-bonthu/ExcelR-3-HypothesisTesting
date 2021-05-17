### Problem Statement 

# A F&B manager wants to determine whether there is any significant difference in the 
# diameter of the cutlet between two units. A randomly selected sample of cutlets 
# was collected from both units and measured? Analyze the data and draw inferences 
# at 5% significance level. Please state the assumptions and tests that you 
# carried out to check validity of the assumptions.

# Load the csv file 
Cutlets = read.csv('Cutlets.csv')

#View data
View(Cutlets)

attach(Cutlets)

### Check Normality

#Defining our Null, Alternate Hypothesis
# Ho: Data is normally distributed
# Ha: Data is not normally distributed
shapiro.test(Unit.A) # p-value = 0.32 > 0.05. Unit.A is normallty distributed

shapiro.test(Unit.B) # p-value = 0.5225 > 0.05. Unit.B is normally distributed

### Check if the variances are equal
# Ho: Equal ariances
# Ha: Inequal variances
var.test(Unit.A, Unit.B) # p-value = 0.3136 > 0.05. Equal variances

# X (A, B) is 2(Discrete) and Y(diameter) is Continuous.
# Y1, Y2 follows Normal Distribution and have equal variances. 
# So we go for 2 Sample T Test for Equal Variances

### 2 Sample T Test

# Defining our Null, and Alternate hypothesis
Ho = 'Avg of Diameter of Unit A is equal to Avg of diameter of Unit B'
Ha = 'Avg of Diameter of Unit A is not equal to Avg of diameter of Unit B'

t.test(Unit.A, Unit.B, alternative = "two.sided", conf.level = 0.95, correct = TRUE)
# p-value = 0.4723 > 0.05. 
# Ho = 'Avg of Diameter of Unit A is equal to Avg of diameter of Unit B'

