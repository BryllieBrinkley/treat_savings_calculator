# Favorite Treat Caluculator

#fill out this form to find out how much money you can save: by putting in the cost of your favorite treat, followed by how often you indulge.
# Then, put the number of years you would like to save,and the interest you expect to make each year.

# Program make a simple calculator

num1 = int(input("Treat price:\n"))
operator = int(input("How many days per week do you buy this treat?:\n"))
num2 = int(input("# of Years you would like to save:\n"))


def treat_calculator(num1,operator,num2):
    weekly_cost = num1 * operator
    yearly_cost = weekly_cost * 52
    amount_saved = yearly_cost * num2
    print('The amount of money you would save = ' + str(amount_saved) + ".")

treat_calculator(num1,operator,num2)