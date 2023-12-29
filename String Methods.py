#!/usr/bin/env python
# coding: utf-8

# ### Lab-9(String_methods): Sayani Ghosh
# ### Batch_Code - ANPC6667

# In[1]:


#Q.1) Write a Python program to Count all letters, digits, and special symbols from the given string
 
string = "P@#yn26at^&i5ve"
alphabets = digits = special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
        
print("\nTotal Number of Alphabets in this String is     : ",alphabets)
print("Total Number of Digits in this String is          : ",digits)
print("Total Number of Special Characters in this String : ",special)
    


# In[2]:


#Q.2) Write a Python program to remove duplicate characters of a given string.

string = "String and String Function"
def remove_duplicates(string):
    # Create an empty string to store the unique characters
    unique_string = ""

    # Iterate through the string and add each character to the unique_string
    # if it has not already been added
    for char in string:
        if char not in unique_string:
            unique_string += char

    return unique_string
remove_duplicates(string)


# In[3]:


#Q.3) Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string


def count_characters(input_string):
    # Initialize counters
    uppercase_count = 0
    lowercase_count = 0
    special_character_count = 0
    numeric_count = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is an uppercase letter
        if char.isupper():
            uppercase_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lowercase_count += 1
        # Check if the character is a special character
        elif char.isnumeric():
            numeric_count += 1
        else:
            special_character_count += 1
    
    return uppercase_count, lowercase_count, numeric_count, special_character_count


input_str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase, lowercase, numeric, special = count_characters(input_str)

print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")
print(f"Numeric values: {numeric}")
print(f"Special characters: {special}")


# In[4]:


#Q.4) Write a Python Count vowels in a string 

def count_vowels(input_string):
    # Define a set of vowels
    vowels = set("aeiouAEIOU")
    
    # Initialize the count
    vowel_count = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1
    
    return vowel_count


input_str = "Welcome to Python Assignment"
vowel_count = count_vowels(input_str)

print(f"Number of vowels in the string: {vowel_count}")


# In[ ]:




