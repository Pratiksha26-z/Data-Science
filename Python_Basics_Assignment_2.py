#!/usr/bin/env python
# coding: utf-8

# 1.What are the two values of the Boolean data type? How do you write them?
# 
# Ans:
#  The Boolean(bool) data type contains two values that is True and False. we will write them as True and False. and these values are case sensitive.
#     

# 2. What are the three different types of Boolean operators?
# 
# Ans: and, or ,not
3.Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).


Ans 

if A=True , B=True  A and B = True
if A=False , B=True  A and B = False
if A=True , B=False  A and B = False
if A=False , B=False  A and B = False

if A=True , B=True   A or B = True
if A=False , B=True  A or B = True
if A=True , B=False  A or B = True
if A=False , B=False  A or B = False

if A=True not A= False
if A=False not A=True
4. What are the values of the following expressions?
(5 &gt; 4) and (3 == 5)
not (5 &gt; 4)
(5 &gt; 4) or (3 == 5)
not ((5 &gt; 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)

Ans:

(5 > 4) and (3 == 5)                                    = False
not (5 > 4)                                             = False
(5 > 4) or (3 == 5)                                     = True
not ((5 > 4) or (3 == 5))                               = False
(True and True) and (True == False)                     = False
(not False) or (not True)                               = True
5. What are the six comparison operators?

Ans :
1. >
2. >=
3. <
4. <=
5. ==
6. !=6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.

Ans:
Assignment operator(=) is used to assign the value to the variable or expression.

Equal to operatoe(==) it is a relation operator, is used to compare left side operands to right side operands.
7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam >5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')
# In[13]:


spam = 0
if spam == 10:
    print('eggs')
if spam >5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')


# In[15]:


'''8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, 
and prints Greetings! if anything else is stored in spam.'''

spam = 2

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greeting')

9.If your programme is stuck in an endless loop, what keys you’ll press?
Ans:
CTRL + C
10.How can you tell the difference between break and continue?

A break statement is used to terminate the loop whenever a particular condition is satisfied.
The break statement will end the innermost loop if it is contained within a nested loop that is the loop inside the other loop.
It is used to end the loop that it is enclosed in, such as a do-while, while, switch, and for statement.

Syntax: break

The continue statement skips the remaining lines of code, for the current iteration of the loop. 
In this case, the loop does not end, it continues with the next iteration.

Syntax: continue11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

Ans: 
 Above 3 functions give you the same output , just writing style is different.

Syntax of range function is. range(start, stop, step)

range(10) : in this function stop value is provided but start and step is not mentioned , python is taking default value for                 these. start=0 and step=1 so the function will be range(0, 10, 1)

range(0, 10): in this function start and stop value is provided but step is not mentioned , python is taking default value for                 this step=1 so the function will be range(0, 10, 1)

range(0, 10, 1) : all the values were provided.
# In[5]:


'''12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.'''

for i in range(1,11):
    print(i)


# In[6]:


i=1

while i<=10:
    print(i)
    i=i+1

13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?

This function can be called with spam.bacon().