# Exercise 1
# Calculate sum or product based on inputs
def custom_function(arg1, arg2=10, arg3=None):
    if arg3 is None:
        print(arg1 + arg2)
    else:
        print(arg1 * arg2 * arg3)
arg1 = int(input("Enter first argument: "))
arg2 = int(input("Enter second argument (or press Enter for default 10): ") or 10)
arg3_input = input("Enter third argument (or press Enter for None): ")
arg3 = int(arg3_input) if arg3_input else None
custom_function(arg1, arg2, arg3)
 
# Exercise 2
# Return strings with length>= 5
def filter_strings(string_list):
    return [s for s in string_list if len(s) >= 5]
# Example 
print(filter_strings(["Giraffe", "dog", "Crocodile", "cat"])) 

# Exercise 3
# evaluate given mathematical expression using the eval() function
expression = "3 * 5 + 2"
result = eval(expression)
print(result) 

# Exercise 4
# Filter prime numbers from user input list
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(is_prime, num_list))
print("Prime numbers:", prime_numbers)  

# Exercise 5
# list of strings to uppercase
words = ["hello", "world", "python", "functions"]
uppercase_words = list(map(str.upper, words))
print(uppercase_words)  
