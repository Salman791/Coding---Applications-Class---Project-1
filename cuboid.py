# Write a program that stores 3 sides of a cuboid as variables (float)
# The program should write the surface area and volume of the cuboid like:
# Surface Area: 600
# Volume: 1000

# Forumula:
# SA of a cuboid = 2(l)(w)+2(l)(h)+2(h)(w)
# Volume of a cuboid = (length × breadth × height)


# Title
print('Surface Area and Volume Of A Cuboid')
print()

# Values

l = 10
b = 10
h = 10

x = 'l = '
y = 'b = '
z = 'h = '

print(x + str(l))
print(y + str(b))
print(z + str(h))

print()

# Calculation of Surface Area

SA = (2*l*b)+(2*l*h)+(2*h*b)
float(SA)
a = float(SA)
c = 'Surface Area: '
print(c + str(SA))

# Calculation of Volume

Volume = (l*b*h)
float(Volume)
d = float(Volume)
e = 'Volume: '
print(e + str(Volume))