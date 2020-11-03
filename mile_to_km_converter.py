# Write a program that asks for an integer that is a distance in miles,
# then it converts that value to kilometers and prints it

print('Please type distance in miles below: ')

input_distance_1 = int(input())

# KM = Miles * 1.609344

KM = input_distance_1 * 1.609344
print(str(KM) + ' km')
