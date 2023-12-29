#!/usr/bin/env python
# coding: utf-8

# ## Lab-7(Functions): Sayani Ghosh
# ### Batch_Code - ANPC6667

# In[1]:


# Q.1)  Function without Parameters

def my_func():
    print('I am Learning python from Pranoti mam')
my_func()   # calling the function


# In[2]:


# Q.2) Function with Parameter

def add_numbers(a, b):
    """A function that adds two numbers."""
    result = a + b
    return result

# Calling the function with two parameters
result = add_numbers(5, 3)
print("Sum of thwo numbers:", result)


# In[3]:


# Q.3) Function with Default Parameter

def my_function(country = "Job seeker"):
  print("I am a " + country)

my_function("Student")
my_function("Employee")
my_function()
my_function("HR")


# In[4]:


# Q.4) Function with Return Keyword 

def mul_num(a, b):  
    # this function is return the value of (a + b)  
    return a * b  
def boolean_function(a):  
    # this function is return the Boolean value  
    return bool(a)  
# calling function  
result1 = mul_num(28, 43)  
print("Output of first function,multiplication is  :", result1)  
result2 = boolean_function(9 < 5)  
print("\nOutput of second function, Boolean value is :", result2)  


# In[5]:


#Q.5) Recursion

def factorial(x):
    #This is a recursive functionto find the factorial of an integer

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = int(input("Enter a number: "))
print("The factorial of", num, "is", factorial(num))

