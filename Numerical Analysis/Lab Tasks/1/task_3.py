from math import *
from random import *

# Task 3
seconds = int(input("Enter seconds: "))
hours = (seconds // 60) // 60
minutes = (seconds // 60) % 60
seconds = seconds % 60
print("H:M:S = ", hours, minutes, seconds)