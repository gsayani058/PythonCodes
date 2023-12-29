#!/usr/bin/env python
# coding: utf-8

# ## Lab-6: Sayani Ghosh¶
# ### Batch_Code - ANPC6667

# In[3]:


#Q.1 - Print the factorial of a number entered by the user using a while loop

num = int(input("enter a number"))
fact=1
i=1
while(i<=num):
    fact=fact*i
    i+=1
print("factorial result of digit ",num,"is",fact)


# In[11]:


#Q.2 - Create a code that describe the use of break statement in while loop

num=int(input("enter a number"))
i=1
while(i<=num):
    if i==3:
        break
    else:
        print(i)
        i+=1
else:
    print("this is else part")


# In[13]:


# Q.3 - Write a Python program using a while loop to iterate through each character of the string "Python" and print each character on a new line. Additionally, calculate and print the length of the string.

str="Python"
print("length=",len(str))
i=0
while i<len(str):  # Iterate through each character using a while loop
    print(str[i])  # Print each character on a new line
    i+=1           # Increment the index and update the string length


# In[14]:


# Q.4 - Write a Python program that takes an integer input from the user and calculates its factorial using a while loop. Display the result as the factorial of the entered number.

number = int(input("Enter a number: "))

# Initialize variables
factorial = 1
current_number = 1

# Calculate factorial using a while loop
while current_number <= number:
    factorial *= current_number
    current_number += 1

# Print the result
print(f"The factorial of {number} is: {factorial}")


# In[ ]:




