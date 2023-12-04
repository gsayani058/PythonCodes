#!/usr/bin/env python
# coding: utf-8

# ## Lab2: Sayani Ghosh 
# ### Batch_Code - ANPC6667

# In[14]:


#Q.1 Write a program for arithmatic operators

n1 = int(input('Enter First number: '))
n2 = int(input('Enter second number: '))

def arithmetic_operators(n1,n2):
    addition = n1 + n2
    print('The result of addition is: ',addition)
    
    substruction = n1-n2
    print('The result of addition is: ',substruction)
    
    multiplication = n1*n2
    print('The result of addition is: ',multiplication)
    
arithmetic_operators(n1,n2)
    


# In[15]:


#Q.2 Write a program for assignment operators

num = int(input('Enter a number: '))

def assignment_operations(num):
    # Using =
    result_equal = num
    print(f"Result using '=': {result_equal}")

    # Using +=
    num += 5
    print(f"Result using '+=': {num}")

    # Using -=
    num -= 3
    print(f"Result using '-=': {num}")

    # Using *=
    num *= 2
    print(f"Result using '*=': {num}")

    # Using /=
    num /= 4
    print(f"Result using '/=': {num}")
assignment_operations(num)


# In[16]:


#Q.3Write a program for Bitwise operators 

def bitwise_operators_example(a, b):
    # Bitwise AND
    result_and = a & b
    print(f"{a} & {b} = {result_and}")

    # Bitwise OR
    result_or = a | b
    print(f"{a} | {b} = {result_or}")

    # Bitwise XOR
    result_xor = a ^ b
    print(f"{a} ^ {b} = {result_xor}")

    # Bitwise left shift
    result_left_shift = a << 1
    print(f"{a} << 1 = {result_left_shift}")

    # Bitwise right shift
    result_right_shift = a >> 1
    print(f"{a} >> 1 = {result_right_shift}")

# Example usage
num1 = 6  # binary: 0101
num2 = 3  # binary: 0011

bitwise_operators_example(num1, num2)


# In[17]:


#Q.4 Write a program to calculate greatest of three numbers.

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




