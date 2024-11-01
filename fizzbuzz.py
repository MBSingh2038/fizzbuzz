# add your code here
#Write a Python that prints the numbers from 1 to 100. if the number is divisible by 3 print Fizz,
#if the number is dividable by 5 print Buzz instead of the number. if the number is dividable by 
#3 and 5 print FizzBuzz instead of the number

for num in range(1, 101):
    if(num%5==0 and num%3==0):
        print("FizzBuzz")
    elif(num%5==0):
        print("Buzz")
    elif(num%3==0):
        print("Fizz")
    else:
        print(num)

"""
Pattern from 1 to upto the user choice

choice = int(input("How many patterns:- "))

for num in range(1, choice+1):
    if(num%5==0 and num%3==0):
        print("FizzBuzz")
    elif(num%5==0):
        print("Buzz")
    elif(num%3==0):
        print("Fizz")
    else:
        print(num)

"""
