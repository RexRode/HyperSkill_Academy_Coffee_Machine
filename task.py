# Make sure your output matches the assignment *exactly*
time_spent_on_computer_in_hours_per_day = int(input())
if time_spent_on_computer_in_hours_per_day < 2:
    print("That seems reasonable")
elif time_spent_on_computer_in_hours_per_day < 4:
    print("Do you have time for anything else?")
else:
    print("You need to get outside more!")
