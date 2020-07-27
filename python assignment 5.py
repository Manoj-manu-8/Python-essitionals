#!/usr/bin/env python
# coding: utf-8
1)How can we sort the list given and append all the zeroes?
# In[1]:


l=[0,1,2,10,5,2,6,0,7,56,0,24,0]
l.sort()
s=[]
s1=[]
for i in l:
    if (i==0):
        s.append(i)
    else:
        s1.append(i)
s1.extend(s)
print(s1)

2)Given the two sorted list and sort them in a order with using only one loop and without using sort function?

# In[11]:


l1=[10,20,30,40,60]
l2=[5,15,25,35,45,60]
size=len(l1)
size1=len(l2)
res=[]
i=0
j=0

while i<size and j<size1:
    if (l1[i]<l2[j]):
        res.append(l1[i])
        i=i+1
    else:
        res.append(l2[j])
        j=j+1

print(res)


# In[ ]:




