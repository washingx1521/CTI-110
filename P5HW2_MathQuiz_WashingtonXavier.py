import random

#CTI-110
#Xavier Washington
#11/4/21
#P5LAB2 - Math Quiz
#


print('Welcome to Math Quiz')
print()
print('MAIN MENU')
print('------------------------------------')
def menu_items(): #Defines the function for the main menu
    menu_items = ["1. Adding Random Numbers" , "2. Subtracting Random Numbers" , "3. Exit Test"] #Three options for the user
    print(menu_items[0])
    print(menu_items[1])
    print(menu_items[2])
    menu_choice() #Calls the menu_choice function


def random_addition(): #Defines the function for generating random numbers for addition
    proceed = 'y'
    integer_one = random.randint(10, 300)#Randint means random integer. 10, 300 is the range.
    integer_two = random.randint(10, 300)
    equation_solution = (integer_one + integer_two)#Stores the correct answer to the equation
    print(f'{integer_one} + {integer_two}')#Prints the integers as an addition problem
    while proceed == 'y':
        student_answer = int(input('Enter your answer: '))#place for students to input their answer
        if student_answer == equation_solution:
            print('Congratualtions! Your answer is correct!')#Good ending
            proceed = 'n'
            menu_choice()
        else:
            print('Sorry, answer is incorrect. Try again.')#Bad ending
                         



def random_subtraction():#Defines the function for generating random numbers for subtraction
    proceed = 'y'
    integer_one = random.randint(10, 300)#Range is any number(s) between 10 and 300
    integer_two = random.randint(10, 300)
    equation_solution = (integer_one - integer_two)
    print(f'{integer_one} - {integer_two}')
    while proceed == 'y':
        student_answer = int(input('Enter your answer: '))
        if student_answer == equation_solution:
            print('Congratualtions! Your answer is correct!')#Good ending
            proceed = 'n'
            menu_choice()
        else:
            print('Sorry, answer is incorrect. Try again.')#Bad ending

def exit_test():
    print('Test exited successfully, have a great day!') #Ends the test, sends off the user.


def menu_choice():#Defines the function for the main menu choices
    proceed = 'y'
    print()
    while proceed == 'y': 
        user_choice = int(input('Please choose one of the menu options: '))#Place for users to select which menu option they want to proceed with
        if user_choice == 1:
            random_addition()#Random addition is assigned to 1
            proceed = 'n'
        elif user_choice == 2: 
            random_subtraction()#Random subtraction is assigned to 2
            proceed = 'n'
        elif user_choice == 3: #Exit Test is assigned to 3
            exit_test()
            proceed = 'n'
        else:
            print('Not a valid choice!') #Any entry besides 1, 2, or 3 is considered an invalid choice.




menu_items()
