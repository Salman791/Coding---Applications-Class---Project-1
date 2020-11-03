# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:

# Sum: 22, Average: 4.4

print('Please Type Integer 1: ')
input_Integer_1 = int(input())

print('Please Type Integer 2: ')
input_Integer_2 = int(input())

print('Please Type Integer 3: ')
input_Integer_3 = int(input())

print('Please Type Integer 4: ')
input_Integer_4 = int(input())

print('Please Type Integer 5: ')
input_Integer_5 = int(input())

Sum = (input_Integer_1+input_Integer_2+input_Integer_3+input_Integer_4+input_Integer_5)
Average = (Sum / 5)

print('Sum: ' + str(Sum))
print('Average: ' + str(Average))
