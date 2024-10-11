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


print('Hello! This program will calculate the total amount of money owed at the end of a month.  ')

#Prompt to input package color
color_package = str(input('Please enter a color of one of the packages listed: ')).lower().lower()

#While loop for if input data is not valid
while color_package not in ('green', 'blue', 'purple'):
    color_package = str(input('Please enter one of the color packages listed: '))
    print (color_package.lower())

#Prompt to input GB used in a month
total_monthly_data = int(input('Please enter data (GB) used in month: '))
while total_monthly_data == "":
    print('Please enter a valid number of Data')
    total_monthly_data = int(input('Please enter data (GB) used in month: '))



#If package color is green
if color_package == 'green':
   money_owed = 49.99 + ((total_monthly_data -2) * 15)
   coupon= str(input('Do you have a coupon?: ')).lower().replace(' ','')
   while coupon not in ('yes', 'no'):
       print('Please enter either yes or no')
   if coupon == 'yes' and money_owed >= 75:
         money_owed =  money_owed - 20

#If package color is blue
elif color_package == 'blue':
    money_owed = 70 + ((total_monthly_data - 4) * 10)

#If package color is purple
elif color_package == 'purple':
    money_owed = 99.95

#Data output
print(f'The number of Data Used was: {total_monthly_data} GB')
print(f'The amount of Money Owed is: ${money_owed:.2f}')




