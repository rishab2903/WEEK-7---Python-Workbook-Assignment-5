#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
Location = "~/Downloads/learn-data-analysis-w-python-master/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.tail()


# In[4]:


df.take(np.random.permutation(len(df))[:500])


# In[ ]:





# In[ ]:





# In[ ]:




