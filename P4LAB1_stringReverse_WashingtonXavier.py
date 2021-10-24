#CTI-110
#P4LAB1
#Xavier Washington
#10/21/2021
#
proceed = 'y'
message_list = []#Storing the user input as a list
reverse_list = []#Storing the reversed text as a list for callback.

while proceed == 'y':
    messageString = input("Enter message or 'Done' to terminate: ")
    #This scans for Done or done as input for the message string. If detected, the program terminates.
    if messageString == 'Done' or messageString == 'done':
        break #breaks the loop
    else:
        message_list.append(messageString) #adds the message string input to the message list

for x in range(len(message_list)):c #x serves as a placeholder for searching within the message list
    messageString = message_list[x]
    reverse_list.append(messageString[::-1])#sends the reversed message to the reverse_list

for x in range(len(reverse_list)): #x serves as a placeholder for searching within the reverse list
    print(reverse_list[x]) #prints the reverse list
