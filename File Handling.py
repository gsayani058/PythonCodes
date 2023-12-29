#!/usr/bin/env python
# coding: utf-8

# ## Lab-10: Sayani Ghosh
# ### Batch_Code - ANPC6667

# In[1]:


#Q-1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

file = open('ABC.txt','r')
print(file.read())        # Opening our text file in read only mode using the open() function


# In[2]:


# Q-2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”

# creating variable to store the number of words
number_of_words = 0

# Opening our text file in read only mode using the open() function
file = open('ABC.txt','r')

# Reading the content of the file using the read() function and storing
data = file.read()

#Splitting the data into separate lines
lines = data.split()

# Iterating over every word in lines
for word in lines:

# checking if the word is numeric or not
    if not word.isnumeric():

# Adding the length of the  lines in our number_of_words variable
        number_of_words += 1

# Printing total number of words
print(number_of_words)


# In[3]:


# Q-3. Write a function in Python to count uppercase character in a text file “ABC.txt”

def count_letter():
    file = open('ABC.txt','r')
    data = file.read()
    
    count = 0
    for letter in data:
        if letter.isupper():
            count += 1
            
    print(count)
    file.close()
    
count_letter()


# In[4]:


# Q-4. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

def display_words():
    file = open('story.txt','r')
    data = file.read()
    
    for i in data:
        word = data.split()
        for i in word:
            if len(i) < 4:
                print(i)
    file.close() 
print('words, which are less than 4 characters:')
display_words()


# In[ ]:




