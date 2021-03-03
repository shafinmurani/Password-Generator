#!/bin/python3
import random
import string

try :
    length = int(input('Input the length of the password [Default : 20] : '))
    if lenght >=10 : 
        print("Please increase the length of the password, Your password is too short")
    if length == '':
        length = 20
    elif length == ' ':
        length == 20
except NameError :
       print("Please Supply a valid integer")
chars = str(string.ascii_letters + string.digits + string.punctuation)

try :
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)
except NameError:
    print('')
