#!/usr/bin/env python
# coding: utf-8

# ## Lab-5: Sayani Ghosh
# ### Batch_Code - ANPC6667

# In[2]:


#Q.1 - Print the table of 5 using for loop

for i in range(6):
    print(i)


# In[9]:


#Q.2 - Print even number series by taking input from the user

n = int(input('Enter a number: '))
for i in range(2,n,2):
    print(i)


# In[11]:


# Q.3 - Create a list and iterate through its items using a for loop

flower_list = ['Rose', 'Lily', 'Tulip', 'Lotus', 'Cherry', 'Jasmine', 'Merigold']
for i in flower_list:
    print(i)


# In[12]:


#Q.4 - Calculate the sum of numbers from 1 to 10 and make a sentence

sum_result = 0
for i in range(1, 11):
    sum_result += i

# Print the result
print(f"The sum of numbers from 1 to 10 is: {sum_result}")


# In[ ]:




