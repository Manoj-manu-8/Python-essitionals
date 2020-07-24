#!/usr/bin/env python
# coding: utf-8
ASSIGNMENT 4:
1.Write a program to print the repeated words index in a given string?
         
# In[4]:


s="If we are good to someone one day we will have respect for that"
l=s.split()
for i in l:
    if (i=="we"):
         print(s.index(i))
         print(s.rindex(i)) 
         break

2.using islower() and isupper give some exaples?
solution:islower() and isupper() are boolean methods in the string both the methods return true or false 
cases: 1)if the given string contains some capital letters and some small letters then it will return false. 
       2)if the given string contains all capital letters then it will return true
       3)if the given string contains all small letters then it will return true.
       
# In[5]:


string="If we are good to someone one day we will have respect for that"
print(string.islower())


# In[7]:


st="MAN"
print(st.isupper())


# In[9]:


st1="manoj is bad boy"
print(st1.islower())


# In[11]:


string1="if we are good to someone one day we will have respect for that"
print(string1.islower())


# In[12]:


s1="WELCOME THE TECHNICAL WORLD"
print(s1.islower())


# In[13]:


s12="WELCOME THE TECHNICAL WORLD"
print(s12.isupper())


# In[14]:


s13="WELCOME the TECHNICAL world"
print(s13.islower())


# In[15]:


s14="welcome the digital world"
print(s14.islower())


# In[ ]:




