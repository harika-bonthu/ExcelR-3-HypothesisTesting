### Problem Statement

# A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT) of reports 
# of the laboratories on their preferred list. They collected a random sample and recorded TAT for reports of 4 laboratories. 
# TAT is defined as sample collected to report dispatch.   
# 
# Analyze the data and determine whether there is any difference in average TAT among the different laboratories at 5% significance level.

# Load the csv file 
LabTAT = read.csv('LabTAT.csv')

#View data
View(LabTAT)

attach(LabTAT)

### Check Normality

#Defining our Null, Alternate Hypothesis
# Ho: Data is normally distributed
# Ha: Data is not normally distributed
shapiro.test(Laboratory.1) # p-value = 0.5508 > 0.05. Unit.A is normallty distributed
shapiro.test(Laboratory.2) # p-value = 0.8637 > 0.05. Unit.A is normallty distributed
shapiro.test(Laboratory.3) # p-value = 0.4205 > 0.05. Unit.A is normallty distributed
shapiro.test(Laboratory.4) # p-value = 0.6619 > 0.05. Unit.B is normally distributed

### Check if the variances are equal
# Ho: All variances are equal 
# Ha: At least two of them differ
bartlett.test(list(Laboratory.1, Laboratory.2, Laboratory.3, Laboratory.4)) # p-value = 0.1069 > 0.05. All variances are equal

# Output(Y) TAT is continuous and follows Normal distribution with equal variances
# X factor is discrete (and more than 2) 
# So we go for one-way ANOVA test 

### one-way ANOVA test 

# Defining our Null, and Alternate hypothesis
Ho = 'Avg Turn Around Time (TAT) of reports of the laboratories are same'
Ha = 'Avg Turn Around Time (TAT) of reports of the laboratories are not same'
Stacked_Data <- stack(LabTAT)
View(Stacked_Data)
res <- aov(values~ind,data = Stacked_Data)
summary(res)
# p-value = 0.00 < 0.05. 
# Ha = 'Avg Turn Around Time (TAT) of reports of the laboratories are not same'

