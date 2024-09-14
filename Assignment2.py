#Getting Started with Python
#CIS103 Introduction to Programming
#Professor - MD Ali
#Student - Ndubuisi Mbamalu
#Assignment2-programiming section
#9/13/2024

#while loop - Write a Python program using a `while` loop that prints numbers from 1 to 10 but exits the
#loop early if the number is greater than 5.

num = 1
while num <= 10:
    print(num)
    if num > 5:
        print("Number is greater than 5. Exiting the loop.")
        break
    num += 1
print("Loop has ended.")

#2. For Loop
#Write a Python program that uses a `for` loop to iterate over the string "CIS103" and prints
#each character along with its ASCII value.

my_string = "CIS103"
for char in my_string:
    ascii_value = ord(char) # Use the built-in 'ord()' function to get the ASCII value of the character
    print(f"Character: {char}, ASCII value: {ascii_value}") # Print the character along with its ASCII value

#3. Nested loop

for i in range(1, 5):  # Loop from 1 to 4 (inclusive)
    for j in range(i):  # Loop 'i' times for each row
        print("*", end="")  # Print '*' without a new line
    print()  # move to the next line after finishing the current row

#4. String operations
#a) Reversed slicing

def reverse_string(s):
    return s[::-1]  # This tells Python to take the string s, start from the end (-1), and move backward to the beginning,reversing it.
string = "Ndubuisi in python"
reverse_string=reverse_string(string)
print ("reversed string:",reverse_string)

#4b) formatting
def format_output(name, age, salary):
    print(f"Name: {name:<10} Age: {age:>3} Salary: ${salary:>10,.2f}")
## Name is left-aligned in 10 characters, Age is right-aligned in 3 characters, and Salary is right-aligned in 10 characters.
name="John"
age=30
salary=50000.50
format_output(name, age, salary)

#5)List operations
my_list=[8,12, 16, 20, 24,30]
#a) append 26 to the list
my_list.append(26)
print("after appending:", my_list)

#b)insert a # at a specific index
my_list.insert(3,5) #inserting 5 at index 3
print("after inserting 5 at index 3:", my_list)

#c)Sort the list in ascending order
my_list.sort()
print("after sorting in ascending order:", my_list)

#d)Pop the last element of the list and print it
last_element=my_list.pop()
print("popped my last element:", last_element)
print("list after poppint last element:", my_list)

#5e)Remove a specific number from the list
my_list.remove(5)
print("after removing 5 from the list:", my_list)

#6 Write a Python program that creates a tuple with 5 elements and prints the first and last
#elements.Then, attempt to modify one of the elements and explain the result.

my_tuple = (10, 15, 25, 30, 55)
print("First element:", my_tuple[0]) #Print the first and last elements
print("Last element:", my_tuple[-1])
try:
    my_tuple[1] = 20  # Trying to modify the second element
except TypeError as f:
    print("error:", f)

#7 dictionary Operations
# Creating dictionary with the given key-value pairs
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

#a)Add a new key-value pair to the dictionary
my_dict['profession']='Trader' #Adding key-profession-with value Trader
print("After adding 'Trader':", my_dict)

#b)Update the value of the 'age' key
my_dict['age']=32 #Updating the age to 32
print("After updating 'age':", my_dict)

#c)Remove the 'city' key from the dictionary
my_dict.pop('city')#Removing the 'city' key
print("After removing 'city':", my_dict)

#d)Print all the keys and values in the dictionary
print("Keys and values in the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

#8 Break and Continue Operations.
#Write a Python program that uses a `while` loop and breaks out of the loop when a certain
#condition is met. Include an option to `continue`, skipping an iteration.


counter = 0 #Initialize a counter variable

while True:
    counter += 1 #Increment counter.
    if counter == 6: # If counter is 6,skip.
        print("Skipping 6")
        continue  # That is, skip the rest of the loop body and move to the next iteration.
    print("Counter:", counter) # Print the current counter value.
    if counter == 11: #If counter reaches 11, break out of the loop.
        print("Counter has reached 11, breaking the loop.")
        break  #Exit the loop.


