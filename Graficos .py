#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd


df = pd.read_csv('coa2pc.csv', sep=';'  )


# In[78]:


df['transf_capita'] = df['transf'] / df['popul']


# In[79]:


df.dtypes.tail(10)


# In[80]:


import seaborn as sns
sns.set_theme(style="whitegrid")


df_bs = df[(df['provincia'] =='Buenos Aires')]
cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_bs,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[23]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_bs['year'], df_bs['transf']) #azul 
plt.plot(df_bs['year'], df_bs['inv']) #naranja


# In[24]:


df_cba = df[(df['provincia'] =='Cordoba')]

sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_cba,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[84]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_cba['year'], df_cba['transf']) #azul 
plt.plot(df_cba['year'], df_cba['inv'])  #naranja


# In[26]:


df_stafe = df[(df['provincia'] =='Santa Fe')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_stafe,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[27]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_stafe['year'], df_stafe['transf']) #azul  
plt.plot(df_stafe['year'], df_stafe['inv']) #naranja


# In[28]:


df_cmarca = df[(df['provincia'] =='Catamarca')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_cmarca,
    x="sh_gob", y="sh_prez",
    hue="year",size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[29]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_cmarca['year'], df_cmarca['transf']) #azul 
plt.plot(df_cmarca['year'], df_cmarca['inv'])  #naranja


# In[30]:


df_chaco = df[(df['provincia'] =='Chaco')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_chaco,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[31]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_chaco['year'], df_chaco['transf']) #azul  
plt.plot(df_chaco['year'], df_chaco['inv']) #naranja


# In[32]:


df_ctes = df[(df['provincia'] =='Corrientes')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_ctes,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[33]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_ctes['year'], df_ctes['transf']) #azul 
plt.plot(df_ctes['year'], df_ctes['inv']) #naranja


# In[34]:


df_for = df[(df['provincia'] =='Formosa')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_for,
    x="sh_gob", y="sh_prez",
    hue="year",size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[35]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_for['year'], df_for['transf']) #azul 
plt.plot(df_for['year'], df_for['inv']) #naranja


# In[36]:


df_chu = df[(df['provincia'] =='Chubut')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_chu,
    x="sh_gob", y="sh_prez",
    hue="year",size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[37]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_chu['year'], df_chu['transf']) #azul 
plt.plot(df_chu['year'], df_chu['inv']) #naranja


# In[38]:


df_er = df[(df['provincia'] =='Entre Rios')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_er,
    x="sh_gob", y="sh_prez",
    hue="year",size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[39]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_er['year'], df_er['transf']) #azul 
plt.plot(df_er['year'], df_er['inv']) #naranja


# In[40]:


df_jj = df[(df['provincia'] =='Jujuy')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_jj,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[41]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_jj['year'], df_jj['transf']) #azul 
plt.plot(df_jj['year'], df_jj['inv']) #naranja


# In[42]:


df_lp = df[(df['provincia'] =='La Pampa')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_lp,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[43]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_lp['year'], df_lp['transf']) #azul 
plt.plot(df_lp['year'], df_lp['inv']) #naranja


# In[44]:


df_lr = df[(df['provincia'] =='La Rioja')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_lr,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[45]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_lr['year'], df_lr['transf']) #azul 
plt.plot(df_lr['year'], df_lr['inv'])  #naranja


# In[46]:


df_mz = df[(df['provincia'] =='Mendoza')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_mz,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[47]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_mz['year'], df_mz['transf']) #azul
plt.plot(df_mz['year'], df_mz['inv'])  #naranja


# In[48]:


df_ms = df[(df['provincia'] =='Misiones')]
sns.set_theme(style="whitegrid")



cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_ms,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[49]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_ms['year'], df_ms['transf']) #azul 
plt.plot(df_ms['year'], df_ms['inv']) #naranja


# In[50]:


df_nq = df[(df['provincia'] =='Neuquen')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_nq,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[51]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_nq['year'], df_nq['transf']) #azul 
plt.plot(df_nq['year'], df_nq['inv']) #naranja


# In[52]:


df_rn = df[(df['provincia'] =='Rio Negro')]
sns.set_theme(style="whitegrid")



cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_rn,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[53]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_rn['year'], df_rn['transf']) #azul 
plt.plot(df_rn['year'], df_rn['inv']) #naranja


# In[54]:


df_slta = df[(df['provincia'] =='Salta')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_slta,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[55]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_slta['year'], df_slta['transf']) #azul
plt.plot(df_slta['year'], df_slta['inv'])  #naranja


# In[56]:


df_sj = df[(df['provincia'] =='San Juan')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_sj,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[57]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_sj['year'], df_sj['transf']) #azul 
plt.plot(df_sj['year'], df_sj['inv']) #naranja


# In[58]:


df_sluis = df[(df['provincia'] =='San Luis')]
sns.set_theme(style="whitegrid")


cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_sluis,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[59]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_sluis['year'], df_sluis['transf']) #azul
plt.plot(df_sluis['year'], df_sluis['inv'])  #naranja


# In[60]:


df_scruz = df[(df['provincia'] =='Santa Cruz')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_scruz,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[61]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_scruz['year'], df_scruz['transf']) #azul
plt.plot(df_scruz['year'], df_scruz['inv'])   #naranja


# In[62]:


df_stgo = df[(df['provincia'] =='Santiago del Estero')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_stgo,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[63]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_stgo['year'], df_stgo['transf']) #azul
plt.plot(df_stgo['year'], df_stgo['inv'])  #naranja


# In[64]:


df_tf = df[(df['provincia'] =='Tierra del Fuego')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_tf,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[65]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_tf['year'], df_tf['transf']) #azul
plt.plot(df_tf['year'], df_tf['inv']) #naranja


# In[66]:


df_tc = df[(df['provincia'] =='Tucuman')]
sns.set_theme(style="whitegrid")




cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df_tc,
    x="sh_gob", y="sh_prez",
    hue="year", size = 'transf',
    palette=cmap, sizes=(50, 200),
)
g.figsize = (1000,2000)
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)


# In[67]:


import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
plt.plot(df_tc['year'], df_tc['transf']) #azul
plt.plot(df_tc['year'], df_tc['inv'])  #naranja


# In[68]:


import matplotlib.pyplot as plt
import seaborn as sns
grid = sns.FacetGrid(df, col = "provincia", hue = 'year')
grid.map(sns.scatterplot, "sh_gob", "sh_prez")
plt.figure(figsize=(100,200))
grid.add_legend()

plt.show()


# In[74]:


import matplotlib.pyplot as plt
import seaborn as sns
df['transf_capita'] = df['transf'] / df['popul']
plt.figure(figsize=(20,10))
sns.boxplot(x='provincia', y='transf_capita', data=df)


# In[82]:


plt.figure(figsize=(20,10))
sns.boxplot(x='provincia', y='transf', data=df)


# In[ ]:




