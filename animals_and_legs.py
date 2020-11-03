# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The second represents the number of pigs owned by the farmer
# It should print how many legs all the animals have

print('Please type below the number of chickens the farmer has: ')
input_chickens = int(input())

print('Please type below how many pigs does the farmer have: ')
input_pigs = int(input())

Total_Legs = ((input_chickens*2) + (input_pigs*4))
print('Total Legs of Animals: ' + str(Total_Legs))
