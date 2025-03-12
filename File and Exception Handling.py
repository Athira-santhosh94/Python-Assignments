# Exercise 1: Read a file and display its contents

def create_and_read_file(filename):
    with open(filename, 'w') as file:
        file.write("Hello, this is a sample file.\nThis file is created for reading.")
    with open(filename, 'r') as file:
        content = file.read()
        print("File Contents:\n", content)
create_and_read_file("sample.txt")

# Exercise 2: Copy contents of one file to another

with open('source.txt', 'w') as f:
    f.write("Hello, this is a test file.")

def copy_file(source, destination):
    try:
        with open(source, 'r') as src:
            content = src.read()
        with open(destination, 'w') as dest:
            dest.write(content)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except Exception as e:
        print("An error occurred:", e)

# Call the function
copy_file('source.txt', 'destination.txt')

# Exercise 3: Reads a file and counts the number of words

with open('sample.txt', 'w') as f:
    f.write("Hello world! This is a test file with some words.")
def count_words(filename):
    try:
        with open(filename, 'r') as file:  
            content = file.read()
            words = content.split()
            word_count = len(words)
        print(f"Total number of words in '{filename}': {word_count}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)

# Call the function
count_words('sample.txt')

# Exercise 4:Converts user input to an integer and handles errors.
def convert_to_integer():
    try:
        user_input = input("Enter a number: ").strip() 
        number = int(user_input)  
        print(f"Converted integer: {number}")
    except ValueError:  
        print("Error: Invalid input. Please enter a valid integer.")

# Call the function
convert_to_integer()

# Exercise 5:Checks if the input list contains negative numbers and raises an exception if found.

def check_positive_numbers():
    try:
        numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
         
        for num in numbers:
            if num < 0:
                raise ValueError("Negative numbers are not allowed!")
        print("All numbers are positive:", numbers)
    except ValueError as e:
        print("Error:", e)

# Call the function
check_positive_numbers()

# Exercise 6: Compute the average of a list of integers with exception handling
def compute_average():
    try:
        numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split())) 
        if not numbers:  
            raise ValueError("List cannot be empty!")  
        average = sum(numbers) / len(numbers)  
        print(f"The average is: {average:.2f}")
    except ValueError as e:
        print("Error:", e)
    finally:
        print("Program has finished running.") 

# Call the function
compute_average()

# Exercise 7:Write a string to a file with exception handling
def write_to_file():
    try:
        filename = input("Enter the filename: ")  
        content = input("Enter the content to write: ")  
        with open(filename, 'w') as file:  
            file.write(content)  
        print("Welcome! File has been successfully written.")  
    except Exception as e:
        print("Error:", e) 
 
# Call the function
write_to_file()

