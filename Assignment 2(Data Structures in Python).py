#Topic:List

#Q1. Create a list of 5 random numbers and print the list.
import random
random_list = random.sample(range(1, 100), 5)  # Picks 5 unique random numbers
print("Random List:", random_list)
#Q2. Insert 3 new values to the list and print the updated list
random_list[2:2] = [101, 102, 103]
print("The list after inserting is:", random_list)
print("Updated List:", random_list)
# Q3. Use a for loop to print each element in the list
print("Elements in the List:")
for num in random_list:
    print(num)


#Topic:Dictionary

#Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.
person = {'name': 'John', 'age': 25, 'address': 'New York'}
print("Original Dictionary:", person)
# Q2. Add a new key-value pair to the dictionary
person['phone'] = '1234567890'
print("Updated Dictionary:", person)


#Topic:Set

# Q1. Create a set with values 1, 2, 3, 4, and 5
number_set = {1, 2, 3, 4, 5}
print("Original Set:", number_set)
# Q2. Add the value 6 to the set
number_set.add(6)
print("Set after adding 6:", number_set)
# Q3. Remove the value 3 from the set
number_set.remove(3)
print("Set after removing 3:", number_set)

# Topic:Tuple

# Q1. Create a tuple with values 1, 2, 3, and 4
number_tuple = (1, 2, 3, 4)
print("Tuple:", number_tuple)
# Q2. Print the length of the tuple
print("Length of Tuple:", len(number_tuple))
