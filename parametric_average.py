# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

#a = int(input("Please enter a number: "))

sum = 0
average = 0

for a in range(1,4):
    a = int(input("Please enter a number: "))

    sum = a + sum
    average = sum / 3

print("Sum: ",sum, "Average: ",average)



