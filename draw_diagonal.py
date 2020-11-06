# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was

n = int(input("Please enter a number: "))

for i in range(n):
    for j in range(n):

        if i==0 or i==n-1 or i==j or j==0 or j==n-1:
            print("%",end=" ")

        else:
            print(" ", end=" ")

    print(" ")
