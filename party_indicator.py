# Write a program that asks for two numbers
# The first number represents the number of girls that comes to a party, the
# second the boys
# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20
#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#
# It should print: Average party...
# If there are less people coming than 20
#
# It should print: Sausage party
# If no girls are coming, regardless the count of the people

a = int(input("How many girls are there in the party? "))
b = int(input("How many boys are there in the party? "))

if a == b and a + b > 20:
    print("The party is excellent!")
elif a < b and a + b > 20:
    print("Quite cool party!")
elif a > 0 and b > 0 and a + b < 20:
    print("Average party!")
elif a == 0:
    print("Sausage party! :(")
else:
    print("Enjoy your moment!")
