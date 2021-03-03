#!/bin/python3
import random
import string
try :
    length = input('Input the length of the password [default : 20] : ')
except NameError :
       print("Please Supply a valid integer")
except KeyboardInterrupt :
    print("\nUser interrupted the program \nExitting...")
if length == '':
    length = 20
elif length == ' ' :
    length = 20
chars = str(string.ascii_letters + string.digits + string.punctuation)
try : 
    int(length)
except ValueError:
    print("Please Supply a valid integer")
try :
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)
except NameError:
    print('')
except KeyboardInterrupt :
    print("\nUser interrupted the program \nExitting...")
except TypeError :
    print('')
