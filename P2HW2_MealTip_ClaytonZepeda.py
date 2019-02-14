# Program that will calculate meal's total cost and calculate tips with 15%,18%,20%
# 2-7-2019
# CTI-110 P2HW2 - Meal Tip Calculator
# Clayton Zepeda
#
#Input meal cost
#Input tip percentage
#calculate tip percentage times total meal cost
#Output the tip amount for each percentage
#

meal_cost = float(input('Enter the cost of the meal: ' ))
total_meal_cost1 = meal_cost * .15
total_meal_cost2 = meal_cost * .18
total_meal_cost3 = meal_cost * .20

print ('15% tip: ',format(total_meal_cost1, '.2f'))                        
print ('18% tip: ',format(total_meal_cost2, '.2f'))
print ('20% tip: ',format(total_meal_cost3, '.2f'))
