# Program to display profit from projected amount of total sales.
# 2-5-2019
# CTI-110 P2T1 - Sales Prediction
# Clayton Zepeda
#
#Use the value 0.23 to represent 23 percent

#Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

#Display the profit
print('The profit is $', format(profit, ',.2f'))
