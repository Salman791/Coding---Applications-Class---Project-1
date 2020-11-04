# Create a program that asks for a number and prints the multiplication table with that number

a = int(input("Enter A Number: "))
b = 1
while (b<=10):
    print(a," * ",b," = ",(a*b))
    b = b+1