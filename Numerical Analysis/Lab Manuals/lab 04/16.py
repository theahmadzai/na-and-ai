# Question 16:write a program that ask the user for a number of seconds and
# print out how many minutes and second that is. for instance 200 seconds is 3 minutes and 20 sec

seconds = int(input('No of seconds: '))
min = seconds // 60
sec = seconds % 60

print(seconds, ' time seconds is ', min, ':', sec)