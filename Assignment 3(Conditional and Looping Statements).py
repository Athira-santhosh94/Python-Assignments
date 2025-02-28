# Exercise 1
# MonthNames.py
month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = int(input("Enter the month: "))
if 1 <= month <= 12:
    print(f"Month {month} is {month_names[month - 1]}")
else:
    print("Invalid month number.")

# Exercise 2
# Cinema Ticket Price for different age groups
age = int(input("Enter your age: "))
if age < 16:
    price = 6 / 2
elif age >= 60:
    price = 6 / 3
else:
    price = 6
print(f"Your ticket costs £{price:.2f}")

# Exercise 3
# BodyMassIndex.py
weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("You are in the 'Underweight' range.")
elif 18.5 <= bmi < 25:
    print("You are in the 'Normal' range.")
elif 25 <= bmi < 30:
    print("You are in the 'Overweight' range.")
else:
    print("You are in the 'Obese' range.")

# Exercise 4
# Greatest of three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

print(f"The greatest number is {greatest}")

# Exercise 5
# Factorial using loop
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")

# Exercise 6
# Reverse a number using while loop
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print(f"Reversed number: {rev}")

# Exercise 7
# Finding multiples of a number
num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))
for i in range(1, limit + 1):
    print(num * i)

#Exercise 8
#Print until done is entered
while True:
    value = input(":")  # Take user input
    if value.lower() == 'done':  # Removes extra spaces & checks lowercase
        print("Done")
        break
    print(value)

# Exercise 9
for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Exercise 10
# Printing pattern 
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
