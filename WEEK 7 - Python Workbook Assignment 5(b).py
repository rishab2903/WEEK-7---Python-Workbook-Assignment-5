#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
GradeList = zip(names,grades)
df = pd.DataFrame(data=GradeList,
columns=['Names','Grades'])
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]


# In[7]:


df


# In[8]:


df['Grades'].count()


# In[10]:


df['Grades'].mean()


# In[ ]:





# In[11]:


df['Grades'].std()


# In[ ]:





# In[12]:


df['Grades'].min()


# In[ ]:





# In[13]:


df['Grades'].max()


# In[ ]:





# In[14]:


df['Grades'].quantile(.25)


# In[ ]:





# In[15]:


df['Grades'].quantile(.5)


# In[ ]:





# In[16]:


df['Grades'].quantile(.75)


# In[ ]:





# In[ ]:




