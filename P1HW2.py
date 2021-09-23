# A simple program designed to calculate a 6% tax on a monthly Cable charge, depending on user input of their monthly cable cost.
# 9/21/21
# CTI-110 P1HW2 - Basic Math
# Xavier Washington
#


#input
#processing
#output

print('P1HW2')


userNum1 =(input('Enter name of expense:')) #This is a flexible input spot for users to name their recurring charge.
userNum2 = float(input('Enter monthly charge:')) #This is an integer-oriented input spot for the cost of a charge, pre-tax.



print('Bill:',userNum1, end=' ')
print('\t Before Tax:$',userNum2)
#This is the code needed to contain "Bill" and "Before Tax" on the same line of code.

txt='Monthly Tax: ${:.2f}'
print(txt.format(userNum2 * 0.06))
#This operation calculates 6% of whatever the user inputs into 'Enter monthly charge'.

txt='Monthly Charge: ${:.2f}'
print(txt.format(userNum2 * 1.06))
#This operation calculates the total monthly cost with the 6% tax included.

txt='Annual Charge: ${:.2f}'
print(txt.format(userNum2 * 12 * 1.06))
#This final operation takes the Monthly Charge and multiplies it by 12, accounting for an entire year of charges.
