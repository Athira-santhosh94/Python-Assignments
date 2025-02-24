Python Fundamentals

# Exercise 1
print("Charlie")
print("ST1001")
print("charlie@gmail.com")

# Exercise 2
# Using escape sequences to print each details
print("Charlie\nST1001\ncharlie@gmail.com")

# Exercise 3
num1 = 14
num2 = 7
print(num1, "+", num2, "=", num1 + num2)
print(num1, "*", num2, "=", num1 * num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "/", num2, "=", num1 / num2)

# Exercise 4
# Printing numbers from 1 to 5 in steps
print(1)
print(2)
print(3)
print(4)
print(5)

# Exercise 5
print('"SDK" stands for "Software Development Kit", \nwhereas\n"IDE" stands for "Integrated Development Environment".')

# Exercise 6
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

# Exercise 7
num = 23
textnum = "57"
decimal = 98.3
print('Type of num:',type(num))
print('Type of textnum :',type(textnum))
print('Type of decimal :',type(decimal))
# Converting textnum to integer for addition
textnum_int = int(textnum)
sum = num + textnum_int + decimal
print("Sum of variables:", sum)
print("Type of the sum:", type(sum))

# Exercise 8
days_in_year = 365          # number of days in a year
hours_in_day = 24           # number of hours in a day
minutes_in_hour = 60        # number of minutes in an hour

# Calculating total minutes in a year
total_minutes = days_in_year * hours_in_day * minutes_in_hour

print("Total minutes in a year:", total_minutes)

# Exercise 9
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")

# Exercise 10
#Calculate and covert pound to dollar
# Save this code in PoundsToDollars.py

pounds = float(input("Please enter amount in pounds: £"))
exchange_rate = 1.25
dollars = pounds * exchange_rate
print(f"£{pounds} are ${dollars}")
