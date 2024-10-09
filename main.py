# Programmers:  Theresa and Antonio
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 10/9/24
# Lab Assignment: 4
# Problem Statement:  Write a program to determine how much a customer owes their mobile phone provider based on their subscription package and amount of data used.
# Data In: Color package, and number of GB
# Data Out: Amount of money owed for a month based on their package, and data used
# Credits:In class

#Package Green:
#For $49.99/month, 2GB of data is provided.
#Additional GB are $15/GB.
#Check if the customer has a coupon.
#The coupon takes $20 off a bill of $75 or more.
#Package Blue:
#for $70/month, 4GB of data is provided.
#Additional GB are $10/GB.
#Package Purple:
#For $99.95/month, unlimited data is provided.

color_package = str(input('Enter a color of one of the packages listed: ')).lower().lower()

while color_package != 'green' and color_package !=  'blue' and color_package != 'purple':
    color_package = str(input('enter one of the color packages listed'))
    color_package = color_package.lower()


total_monthly_data = int(input('enter data used in month:'))

if color_package == 'green':
   money_owed = 49.99 + ((total_monthly_data -2) * 15)
   if money_owed >= 75:
         money_owed =  money_owed - 20
elif color_package == 'blue':
    money_owed = 70 + ((total_monthly_data - 4) * 10)
elif color_package == 'purple':
    money_owed = 99.95

print(f'Data Used: {total_monthly_data} GB')
print(f'Money Owed: ${money_owed:.2f}')




