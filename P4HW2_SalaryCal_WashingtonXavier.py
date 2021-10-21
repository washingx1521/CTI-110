#CTI-110
#P4HW2
#Xavier Washington
#10/17/2021
#

# totals of all employees
total_overtimePay = 0
total_regPay = 0
total_grossPay = 0
employee_Count = 0

proceed = 'y'

while proceed == 'y':
    #individual employee variables
    hours_Worked = 0
    pay_Rate = 0
    over_time = 0
    reg_pay = 0
    overtime_pay = 0
    gross_pay = 0
    pay = 0

    employee_Name = input('Enter employee name or "None" to terminate:') #Allows user to enter employee name

    if employee_Name == 'None' or employee_Name == 'none':
        proceed = 'n' #None is a key term that will stop the loop entirely
    else:
        employee_Count += 1
        hours_Worked = int(input('How many hours did they work?:'))
        pay_Rate = float(input('What is their pay rate?:'))
        #These questions are to be asked if Employee Name isn't 'None' or 'none'
        
        if hours_Worked > 40:
            #Individual pay
            over_time = hours_Worked - 40
            reg_pay = 40 * pay_Rate
            overtime_pay = (pay_Rate * 1.5) * over_time
            gross_pay = overtime_pay + reg_pay

            #Add to overall
            total_overtimePay += overtime_pay
            total_regPay += reg_pay
            total_grossPay += gross_pay
        else:
            #This code calculates the pay for all employees. overtime or not
            reg_pay = hours_Worked * pay_Rate
            total_regPay += reg_pay
            total_grossPay += reg_pay
            gross_pay = reg_pay

        #This code prints the above values under their respective names
        print('Hours Worked\tPay Rate\tOvertime\tOvertime Pay\tRegHour Pay\tGross')
        print('----------------------------------------------------------------------------------------')
        text = f'{hours_Worked}\t\t${pay_Rate}\t\t{over_time}\t\t${overtime_pay}\t\t${reg_pay}\t\t${gross_pay}'
        print(text)
        print('')
        
#This code prints the combined, calculated values of all employees.               
print(f'Total number of employees entered: {employee_Count}')
print(f'Total amount payed for overtime: ${total_overtimePay}')
print(f'Total amount payed for regular hours: ${total_regPay}')
print(f'Total amount payed in gross: ${total_grossPay}')


