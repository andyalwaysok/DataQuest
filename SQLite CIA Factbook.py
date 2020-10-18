#!/usr/bin/env python
# coding: utf-8

# Data: CIA World Factbook - Compendium of Stats about all countires on Earth

# In[1]:


get_ipython().run_cell_magic('capture', '', '%load_ext sql\n%sql sqlite:///factbook.db')


# Skimming data

# In[2]:


get_ipython().run_cell_magic('sql', '', '\nSELECT *\nFROM facts\nLIMIT 5')


# Min & Max of population and growth

# In[3]:


get_ipython().run_cell_magic('sql', '', '\nSELECT MIN(population), MAX(population), MIN(population_growth), MAX(population_growth)\nFROM facts')


# Investigating which country has 0 and 7.2 bil population

# In[5]:


get_ipython().run_cell_magic('sql', '', '\nSELECT *\nFROM facts\nWHERE population = 0')


# In[6]:


get_ipython().run_cell_magic('sql', '', '\nSELECT *\nFROM facts\nWHERE population = (SELECT MAX(population) FROM facts)')


# Min & Max of population and growth without World

# In[7]:


get_ipython().run_cell_magic('sql', '', "\nSELECT MIN(population), MAX(population), MIN(population_growth), MAX(population_growth)\nFROM facts\nWHERE name != 'World'")


# Average population and area without World

# In[8]:


get_ipython().run_cell_magic('sql', '', "\nSELECT AVG(population), AVG(area)\nFROM facts\nWHERE name != 'World'")


# Countries with most people and highest growth rate

# In[11]:


get_ipython().run_cell_magic('sql', '', "\nSELECT name\nFROM facts\nWHERE population = (SELECT MAX(population) FROM facts WHERE name != 'World')")


# In[13]:


get_ipython().run_cell_magic('sql', '', "\nSELECT name\nFROM facts\nWHERE population_growth = (SELECT MAX(population_growth) FROM facts WHERE name != 'World')")


# Which countries have the highest ratios of water to land? 
# Which countries have more water than land?

# In[23]:


get_ipython().run_cell_magic('sql', '', '\nSELECT name, area_water, area_land, \nMAX((CAST(area_water AS FLOAT) / area_land) * 100) ratio\nFROM facts')


# In[25]:


get_ipython().run_cell_magic('sql', '', '\nSELECT name, area_water, area_land, \n(CAST(area_water AS FLOAT) / area_land) * 100 ratio\nFROM facts\nWHERE ratio > 50\nORDER BY 4 DESC')


# Which countries will add the most people to their population next year?

# In[36]:


get_ipython().run_cell_magic('sql', '', "SELECT name, population, population_growth, \nMAX(population * (population_growth/100)) growth\nFROM facts\nWHERE name != 'World'\nORDER BY 4 DESC")


# Which countries have a higher death rate than birth rate?

# In[39]:


get_ipython().run_cell_magic('sql', '', '\nSELECT name, birth_rate, death_rate\nFROM facts\nWHERE birth_rate < death_rate\nORDER BY 3')


# What countries have the highest population/area ratio?

# In[44]:


get_ipython().run_cell_magic('sql', '', '\nSELECT name, population, area, population/area\nFROM facts\nORDER BY 4 DESC')


# In[ ]:




