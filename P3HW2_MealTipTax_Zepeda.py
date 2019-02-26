# A program that will calculate and display the total costs of a meal with
# tips 15%, 18% or 20% and 7% sales tax.
# CTI-110-0003
# P3HW2 - MealTipTax
# Clayton Zepeda
# 2-14-2019
#


def Main():
# Sales tax
    sales_tax = .07    


# Ask the user to enter the meal charge.
    meal_charge = float(input('Enter the meal charge: '))
    


# Ask the user to enter the tip amount considered.(15%, 18% or 20%)
# Calculate tip amounts
# If user inputs tip amount not 15%, 18% or 20%, display error message.
    print("Recommended tip percentage amounts are 15, 18, or 20.")
    tip = None
    while True:
        #if tip percentage is valid input it breaks.
        try:
            tip = float(input('Enter the tip percentage amount: '))
        except Exception:
            print("Tip percentage amount not an accepted value.")
        if tip == 15:
            break
        elif tip == 18:
            break
        elif tip == 20:
            break
        else:
            print('Tip percentage amount not an accepted value.')

# Calculate tax amount    
    tip_amount = (tip / 100) * meal_charge
    
    tax_amount = sales_tax * meal_charge
        
    total = meal_charge + tip_amount + tax_amount
    
# Display meal cost, tip and tax amounts.
    print('Meal Charge: $' + format(meal_charge, '.2f'),'\nTip: $' + \
    format(tip_amount, '.2f'),'\nSales Tax: $' + format(tax_amount, '.2f'),\
    '\nTotal: $' + format(total, '.2f'), )



  
Main()
