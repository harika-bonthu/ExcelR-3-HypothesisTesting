# Problem Statement
# 
# TeleCall uses 4 centers around the globe to process customer order forms. 
# They audit a certain %  of the customer order forms. Any error in order form renders it defective and has to be reworked before processing.  
# The manager wants to check whether the defective %  varies by centre. 
# Please analyze the data at 5% significance level and help the manager draw appropriate inferences

# Load the csv file 
CustOrderForm = read.csv('Costomer+OrderForm.csv')

#View data
View(CustOrderForm)

attach(CustOrderForm)

dplyr::count(CustOrderForm, India, sort = TRUE)
dplyr::count(CustOrderForm, Indonesia, sort = TRUE)
dplyr::count(CustOrderForm, Malta, sort = TRUE)
dplyr::count(CustOrderForm, Phillippines, sort = TRUE)

# Defining our Null, Alternate Hypothesis
Ho = 'Defective %  across the centers is same'
Ha = 'Defective %  across the centres is not same'

a <- data.frame(280, 267, 269, 271)
b <- data.frame(20, 33, 31, 29)
buyData <- table(a, b)
View(buyData)

print(chisq.test(buyData))
# p-value = 0.2133 > 0.05. Defective %  across the centers is same.
