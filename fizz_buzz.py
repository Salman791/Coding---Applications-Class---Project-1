# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

a = 0

for a in range(1, 101):
    if a % 3==0:
        print("Fizz")
    elif a % 5==0:
        print("Buzz")
    elif a % (3*5)==0:
#How do I maintain the sequence and make sure it prints FizzBuzz if it's a multiple of both???
        print("FizzBuzz")

    else:
        print(a)







