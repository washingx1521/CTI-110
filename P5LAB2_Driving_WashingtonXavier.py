#CTI-110
#Xavier Washington
#11/4/21
#P5LAB2 - Driving
#
twenty_miles = 0

def main():
    miles_per_gallon = float(input('Enter driven miles per gallon of gas: '))#User enters # of miles they drove
    dollars_per_gallon = float(input('Enter the cost of a gallon of gas: '))#User enters the cost of gas

    print('{:.2f}'.format(driving_cost(10, miles_per_gallon, dollars_per_gallon)))#outputs the cost of gas for 10 miles (based on cost provided by user)
    print('{:.2f}'.format(driving_cost(50, miles_per_gallon, dollars_per_gallon)))#outputs the cost of gas for 50 miles (based on cost provided by user)
    print('{:.2f}'.format(driving_cost(400, miles_per_gallon, dollars_per_gallon)))#outputs the cost of gas for 400 miles (based on cost provided by user)
    
def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):#function for compiling data
    

    return driven_miles * (1/miles_per_gallon) * dollars_per_gallon#Returns driving cost



    


main()
