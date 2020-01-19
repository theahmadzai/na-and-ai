# Question 9:Write a program to display the following  Shape. User must enter no of rows and columns and also the length of diagonal.
#    *   *   *
#   *** *** ***
#    *   *   *

n = int(input("Enter a diagonal: "))

s = n
last = 0
for x in range(1, n+1):
    print(str(" " * s) + str("*" * (x + last)) + str(" " * s))
    last = last+1
    s = s-1

s = 1
last = n-1

print("*" * ((n*2)+1))

for x in range(n, 0, -1):
    print(str(" " * s) + str("*" * (x + last)) + str(" " * s))
    last = last-1
    s = s+1


        #    *                         3 1 3
        #   ***                        2 3 2
        #  *****                       1 5 1
        # *******                      0 7 0
        #  *****                       1 5 1
        #   ***                        2 3 2
        #    *                         3 1 3