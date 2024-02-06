#!/usr/bin/env python
# coding: utf-8

# # Day 03  0F 75 DAYS CHALLENGE 

# # PANDAS 

# # titanic dataset
# 
# 

# In[7]:


import pandas as pd


# In[3]:


df = pd.read_csv("train.csv")


# In[4]:


df


# In[5]:


df.head()


# In[6]:


df.tail()


# In[8]:


df.dtypes


# In[10]:


df.count()


# In[11]:


df.describe()


# In[15]:


df[['Name','Age','Sex','Embarked']]


# In[16]:


df.dtypes == 'object'


# In[17]:


df.dtypes == 'float'


# In[18]:


df.dtypes == 'int'


# In[20]:


df[df.dtypes[df.dtypes ==  'int64'].index]


# In[21]:


df[df.dtypes[df.dtypes == 'float64'].index]


# In[22]:


df.head(9)


# In[23]:


df.tail(19)


# In[25]:


df[['Ticket']]


# In[28]:


df[['Ticket']][2:9]


# In[29]:


df[['Ticket']][2:9:2]


# In[30]:


df[['Cabin','Ticket']][2:90]


# In[34]:


df['new_col']= 2.5


# In[32]:


df


# In[35]:


df.insert(loc =3,column = 'food',value = 0)


# In[36]:


df


# In[37]:


df['Name']


# In[40]:


a =df['Name'][2:6]


# In[41]:


a


# In[43]:


type(a)


# In[50]:


m1 =pd.Series([100,200,300,400], index =[1,2,3,4])


# In[51]:


m1


# In[54]:


m2 = pd.Series([66,77,88,99], index = [1,2,3,4])


# In[55]:


m2


# In[56]:


m3 = pd.concat([m1,m2])


# In[57]:


m3


# In[58]:


m1*m2


# In[59]:


m1+m2


# In[64]:


df.drop('PassengerId', axis = 1)


# In[65]:


df


# In[ ]:




