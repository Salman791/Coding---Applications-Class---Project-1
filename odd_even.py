# Write a program that reads a number from the standard input,
# Then prints "Odd" if the number is odd, or "Even" if it is even.

n = int(input(" Enter number: "))
if (n%2==0):
    print(n," is an even number")
else:
    print(n," is an odd number")
