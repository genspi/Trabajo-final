#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


df = pd.read_csv('coa2pc.csv', sep=';'  )


# In[7]:


df['transf_capita'] = df['transf'] / df['popul']


# In[8]:


df['inv_capita'] = df['inv'] / df['popul']


# In[9]:


df.dtypes.tail()


# In[14]:


df['dif_sh']= df['sh_prez']-df['sh_gob']
df['dif_sh']


# In[54]:





# In[5]:


import statsmodels.api as sm
model = sm.OLS(df['sh_prez'], sm.add_constant(df[['sh_gob'],['transf']]))
result = model.fit()
print(result.summary())


# In[6]:


import statsmodels
import statsmodels.formula.api as smf
res = smf.ols(formula="sh_prez ~ sh_gob + transf + inv", data=df).fit()
res.summary()


# In[21]:


import statsmodels
import statsmodels.formula.api as smf
res = smf.ols(formula="sh_prez ~ sh_gob*core + transf", data=df).fit()
res.summary()


# In[22]:


import statsmodels
import statsmodels.formula.api as smf
res = smf.ols(formula="sh_prez ~ sh_gob*core + inv", data=df).fit()
res.summary()


# In[23]:


df_nn = df.dropna(subset= ["sh_gob", "transf", "sh_prez", "inv"])
df_nn


# In[24]:


df_07 = df_nn[(df_nn['year'] == 2007)]


# In[25]:



import statsmodels
import statsmodels.formula.api as smf
res = smf.ols(formula="sh_prez ~ sh_gob + transf*core", data=df_07).fit()
res.summary()


# In[26]:



import statsmodels
import statsmodels.formula.api as smf
res = smf.ols(formula="sh_prez ~ sh_gob + transf", data=df_07).fit()
res.summary()


# In[27]:


df_11 = df_nn[(df_nn['year'] == 2011)]


# In[28]:



import statsmodels
import statsmodels.formula.api as smf
res = smf.ols(formula="sh_prez ~ sh_gob + transf", data=df_11).fit()
res.summary()


# In[79]:



import statsmodels
import statsmodels.formula.api as smf
res = smf.ols(formula="sh_prez ~ sh_gob + transf*core", data=df_11).fit()
res.summary()


# In[29]:


df_15 = df_nn[(df_nn['year'] == 2015)]


# In[30]:


import statsmodels
import statsmodels.formula.api as smf
res = smf.ols(formula="sh_prez ~ sh_gob + transf", data=df_15).fit()
res.summary()


# In[81]:


import statsmodels
import statsmodels.formula.api as smf
res = smf.ols(formula="sh_prez ~ sh_gob + transf + transf_post1 + transf_post2", data=df_07).fit()
res.summary()


# In[31]:


import statsmodels
import statsmodels.formula.api as smf
res = smf.ols(formula="sh_prez ~ sh_gob + transf_post1*core ", data=df_11).fit()
res.summary()


# In[34]:


import statsmodels
import statsmodels.formula.api as smf
res = smf.ols(formula="sh_prez ~ sh_gob + inv_post2 + inv_post1 + inv ", data=df_11).fit()
res.summary()


# In[33]:


import statsmodels
import statsmodels.formula.api as smf
res = smf.ols(formula="dif_sh ~ pubemp + inv_capita*core ", data=df).fit()
res.summary()


# In[ ]:




