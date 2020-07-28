#!/usr/bin/env python
# coding: utf-8
1)convert the keys to values and values to keys and store in new dictonary?  
# In[30]:


d={1:'m',2:'a',3:'n',4:'o',5:'j'}
newd=dict([(d[i],i) for i in list(d)])
print(newd)

2nd:method
# In[32]:


d={1:'m',2:'a',3:'n',4:'o',5:'j'}
newd=dict([(j,i) for i,j in d.items()])
print(newd)


# 2)Take list of tuple and add the tuple elements and store in new list?

# In[33]:


l=[(1,2),(3,4),(5,6)]
l1=[(i+j) for i,j in l]
print(l1)

2ndmethod:
# In[34]:


l=[(1,2),(3,4),(5,6)]
l2=[]
for i,j in l:
    c=i+j
    l2.append(c)
print(l2)

3)Take list  it contains tuple and list.make inner list and tuples to outer list 
# In[61]:


l3=[(1,2,3),[2,3,4],[1,2,5],('hy','bye','see')]
l4=[]
for x,y,z in l3:
    l4.append(x)
    l4.append(y)
    l4.append(z)
print(l4)


# In[ ]:





# In[ ]:




