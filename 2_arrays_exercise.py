""" 
Exercise: Array DataStructure

1. Let us say your expense for every month are listed below,
	1. January -  2200
 	2. February - 2350
    3. March - 2600
    4. April - 2130
    5. May - 2190

Create a list to store these monthly expenses and using that find out,

    1. In Feb, how many dollars you spent extra compare to January?
    2. Find out your total expense in first quarter (first three months) of the year.
    3. Find out if you spent exactly 2000 dollars in any month
    4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    5. You returned an item that you bought in a month of April and
    got a refund of 200$. Make a correction to your monthly expense list
    based on this

[Solution](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/Solution/1_expenses.py)

"""
# Creating a list
monthly_expenses = [2200, 2350, 2600, 2130, 2190]
print(monthly_expenses)

# Difference between Feb and Jan expenses
two_difference = monthly_expenses[1] - monthly_expenses[0]
print(f'The expense difference between Feb and Jan is {two_difference}')

# Total expenses in the first quarter
first_quarter = monthly_expenses [0] +  monthly_expenses [1] +  monthly_expenses [2]
print(f"Total expenses of the first quarter is {first_quarter}")

# Print month index that I spent exactly 2000
if 2000 in monthly_expenses:
        print(True)
else:
        print(False)

# Add June's expense
monthly_expenses.append(1980)
print(monthly_expenses)

# Insert April's new expense
monthly_expenses[3] = 1930
print(monthly_expenses)
   



