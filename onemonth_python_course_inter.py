#write a program that prints the number from 1 to 100
for i in range(1,101):
    print(i)

# But for multiples of three print "Fizz" instead of the number
for i in range(1,101):
    if((i%3)==0):
        print("Fizz")
    else:
        print(i)

# and for the multiples of five print "Buzz".
for i in range(1,101):
    if((i%5)==0):
        print("Buzz")
    else:
        print(i)

# For numbers that are multiples of both three and five print "FizzBuzz".
for i in range(1,101):
    if((i%5)==0) and ((i%3)==0):
        print("FizzBuzz")
    else:
        print(i)