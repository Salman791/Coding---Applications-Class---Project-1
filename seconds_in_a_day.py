# current_hours = 14;
# current_minutes = 34;
# current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variables

current_hours = 14
current_minutes = 34
current_seconds = 42

#Calculating total seconds in a day
Total_Seconds_In_A_Day = 24*60*60

a = 'Total Seconds In A Day: '

print(a + str(Total_Seconds_In_A_Day))

Total_Seconds_In_The_Current_Day = (current_hours*current_minutes*current_seconds)

b = 'Total Seconds In The Current Day: '

print(b + str(Total_Seconds_In_The_Current_Day))

Remaining_Seconds_In_The_Day = (Total_Seconds_In_A_Day - Total_Seconds_In_The_Current_Day)

c = 'Remaining Seconds In The Day: '

print(c + str(Remaining_Seconds_In_The_Day))