#!/bin/python3
import random
import string
import sys
try :
    length = input('Input the length of the password [default : 20] : ')
except NameError :
       print("Please Supply a valid integer")
except KeyboardInterrupt :
    print("\nUser interrupted the program \nExitting...")
chars = str(string.ascii_letters + string.digits + string.punctuation)
if length == '':
    length = 20
elif length == ' ':
    length = 20
try : 
    intlen = int(length)
except ValueError:
    print("Please Supply a valid integer")

if intlen <= 15:
	print("Select a number higher than 15")
	sys.exit()
try :
    password = ''.join(random.choice(chars) for _ in range(intlen))
    print(password)
except NameError:
    print('')
except KeyboardInterrupt :
    print("\nUser interrupted the program \nExitting...")
except TypeError :
    print('')
