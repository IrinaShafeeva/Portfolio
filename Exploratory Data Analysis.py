#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[9]:


df = pd.read_csv(r"C:\Users\acer\Downloads\world_population.csv")
df


# In[10]:


pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[11]:


df.info()


# In[12]:


df.describe()


# In[13]:


df.isnull().sum()


# In[14]:


df.nunique()


# In[15]:


df.sort_values(by="World Population Percentage", ascending=False).head(10)


# In[17]:


df.corr()


# In[33]:


sns.heatmap(df.corr(), annot = True)

plt.rcParams['figure.figsize'] = (20,7)

plt.show()


# In[20]:


df.groupby('Continent').mean().sort_values(by="2022 Population",ascending=False)


# In[21]:


df[df['Continent'].str.contains('Oceania')]


# In[22]:


df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean().sort_values(by="2022 Population",ascending=False)
df2


# In[23]:


df.columns


# In[24]:


df3 = df2.transpose()
df3


# In[27]:


df3.plot();


# In[29]:


df.boxplot(figsize=(20,10));


# In[30]:


df.select_dtypes(include='float')

