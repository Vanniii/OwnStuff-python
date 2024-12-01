import time
print("WEIGHT CONVERTER 2.0")

print()


while True:
    weight = input("Weight: ")
    try:
        weight = float(weight)
        break
    except ValueError:
        print("It needs to be a number, dumbass.")
        weight = input("Weight: ")

unit = input("(K)kg or (L)bs: ")
if unit.upper() == "K":
    converted = weight * 2.20462
    print("Converted weight: " + str(converted) + " lbs")
    time.sleep(5)
elif unit.upper() == "L":
    converted = weight / 2.20462
    print("Converted weight: " + str(converted) + " kg")
    time.sleep(5)
else:
     print("Wrong unit. Idiot.")
     time.sleep(5)

