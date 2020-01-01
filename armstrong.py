number = input("Enter a number of 3 digits: ")

if len(number) != 3:
    print("Pleaes enter a 3 digit number.")
    exit()

d1 = int(number[0]) ** 3
d2 = int(number[1]) ** 3
d3 = int(number[2]) ** 3

total = d1+d2+d3

if total != int(number):
    print("The number is not armstrong.")
else:
    print("The number is armstrong.")