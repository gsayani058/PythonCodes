#!/usr/bin/env python
# coding: utf-8

# ## Lab-8(String): Sayani Ghosh
# ### Batch_Code - ANPC6667

# In[1]:


#Q. 1. Write a Python program to count the occurrences of each word in a given sentence

string = "To change the overall look your document. To change the look available in the gallery"
count = {}  # Initialize as an empty dictionary
txt = string.split(" ")

for i in txt:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)


# In[2]:


#Q.2- Write a Python program to remove a newline in Python, String = "\nBest \nDeeptech \nPython \nTraining\n"

original_string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newline characters
cleaned_string = original_string.replace('\n', '')

print("\nString after removing newlines:")

print(cleaned_string)


# In[3]:


#Q.3 Write a Python program to reverse words in a string

string= "Deeptech Python Training"
reverse_str=""
for i in string:
    reverse_str=i+reverse_str
print("reverse string :",reverse_str)


# In[4]:


# Q. 4. Write a Python program to count and display the vowels of a given text


def count_and_display_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    vowel_list = []

    for char in text:
        if char in vowels:
            vowel_count += 1
            vowel_list.append(char)

    print("Vowel Count:", vowel_count)
    print("Vowels:", ', '.join(vowel_list))


user_input = "Welcome to python Training"
count_and_display_vowels(user_input)


# In[ ]:




