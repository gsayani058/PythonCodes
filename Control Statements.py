#!/usr/bin/env python
# coding: utf-8

# ## Lab4: Sayani Ghosh
# ## Batch_Code - ANPC6667

# In[15]:


#Q.1 - Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, 'is a Even number' )
else:
    print(num, 'is a Odd number')


# In[16]:


#Q.2 - Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age

age = int(input('Give the age number of a person: '))

if age >= 18:
    print('This Person is eligible to vote based on his/her age\nBecause the person is',age, 'years old')
else:
    print('This Person is not eligible to vote based on his/her age')


# In[17]:


#Q.3 - Write a Python program that determines if a given year is a leap year or not.

year = int(input('Enter the year to be checked: '))

if (year % 4 == 0) or (year % 400 == 0) and (year % 100 != 0):
    print('Given year is leap year')
else:
    print('Given year is not leap year')


# In[18]:


#Q.4 - Create a Python program that checks if a user-given number is positive, negative, or zero.

n=int(input("Enter a number:"))#taking an inpput from the user
if(n>0):#checking condition for positivity
    print("the number is positive")
if(n<0):#checking condition for nagativity
    print("The number is negative")
if(n==0):#checking for zero
    print("The number is zero")   


# In[19]:


#Q.5 - Write a Python program that determines the largest of three numbers entered by the user.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

def find_greatest(num1, num2, num3):
    # Compare the three numbers
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

result = find_greatest(num1, num2, num3)
print("The greatest number is: ", result)


# In[ ]:




