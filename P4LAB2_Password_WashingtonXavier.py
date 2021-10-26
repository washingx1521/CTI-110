password = input('Enter password here: ')#place for users to input passwords

myIndex = 0 #searches the password
enhanced_password = '' #new password


while myIndex < len(password): #scans the password length in a while loop

    if password[myIndex] == 'i':
        enhanced_password += '1'#replaces 'i' with 1
    elif password[myIndex] == 'a':
        enhanced_password += '@'#replaces 'a' with @
    elif password[myIndex] == 'm':
        enhanced_password += 'M'#replaces 'm' with M
    elif password[myIndex] == 'B':
        enhanced_password += '8'#replaces 'B' with 8
    elif password[myIndex] == 's':
        enhanced_password += '$'#replaces 's' with $
    else:
        enhanced_password += password[myIndex] 

    myIndex += 1

    if myIndex == len(password):
        enhanced_password += '!' #attaches an ! to the end of any output
print(f'Your new password is: {enhanced_password}')#outputs the new password
    
