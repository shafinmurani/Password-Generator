#!/bin/python3
import random
import string

try :
    length = int(input('Input the length of the password : '))
except NameError :
       print("Please Supply a valid integer")
except KeyboardInterrupt :
    print("\nUser interrupted the program \nExitting...")

chars = str(string.ascii_letters + string.digits + string.punctuation)

try :
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)
except NameError:
    print('')
except KeyboardInterrupt :
    print("\nUser interrupted the program \nExitting...")
