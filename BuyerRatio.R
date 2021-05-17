### Problem Statement 

# Sales of products in four different regions is tabulated for males and females. 
# Find if male-female buyer rations are similar across regions.

### Solution 

# Load the csv file 
BuyerRatio = read.csv('BuyerRatio.csv')

#View data
View(BuyerRatio)

attach(BuyerRatio)

# We have 4 discrete inputs (East, West, North, South)
# Ouput is also discrete
# So we go for Chi-Square test

# Defining our Null, Alternate hypothesis
Ho = "Male-Female buyer rations are similar across regions"
Ha = "Male-Female buyer rations are not similar across regions"

buyData <- data.frame(East, West, North, South)

print(chisq.test(buyData))
# p-value = 0.6603 > 0.05. Male-Female buyer rations are similar across regions.
