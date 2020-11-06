# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

row = int(input("Please enter the number of rows: "))

for i in range(row):
    print(" "*(row-i)+" *"*(i+1))
for j in range(row-1):
    print(" "*(j+2)  +" *"*(row-1-j))

# solution from https://www.youtube.com/watch?v=Z_2bQ0_ULFQ