#!/usr/bin/env python
# coding: utf-8

# # Washington DC Housing Market Analysis 

# # Exploratory Data Analysis

# ### Data Source: https://www.redfin.com/blog/data-center

# In[1]:


#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Data Import and Data Cleaning
# ### Importing data and creating dataframes for each Washington DC region
# #### All required datasets are downloaded in our folder titled "data"

# In[2]:


# set up name label to match each csv dataset
lst = []
for i in range(1,83):
    location = 'data/'
    ext = 'data_crosstab ({}).csv'.format(i)
    final = location + ext
    lst.append(final)
    # print(final)

# pull datasets from data folder and clean data such as $1,200K, 1.5%, etc. Change data type from object to float
# create a new list: df_list to include all datasets
df_list = []
i = 0
for location in lst:
    df = pd.read_csv(location, encoding='utf-16', sep='\t')
    df = df.add_suffix('_'+str(i))
    # reformat the median sale prices from strings to floats
    #df["Median Sale Price" + "_"+ str(i)] = df["Median Sale Price" + "_"+ str(i)].str.replace("$", "").str.replace(",", "").str.replace("K","000").str.replace("%","").astype(float)
    for j in range(len(df.columns)-2):
        if df[df.columns[j+2]].dtype == 'object':
            df[df.columns[j+2]] = df[df.columns[j+2]].str.replace("$", "").str.replace(",", "").str.replace("K","000").str.replace("%","").astype(float)
        #df[df.columns[j+2]] = df[df.columns[j+2]].str.replace("$", "").str.replace(",", "").str.replace("K","000").str.replace("%","").astype(float)
    df_list.append(df)
    i += 1

df_list[0].head()


# ### Creating dataframe containing median sale prices, Homes Sold MoM and Inventory MoM of each Washington DC region from Feb. 2012 to Oct. 2019 

# In[5]:


# Create datasets for median sale prices, Homes Sold MoM and Inventory MoM and save them in data folder


#Creating dataframe containing Median Sale Price of each Washington DC region from Feb. 2012 to Oct. 2019 
final_lst = []
i = 0
for df in df_list:
    final_lst.append(df["Median Sale Price" + "_"+ str(i)][0:93])
    i += 1
median_sale_price = pd.concat(final_lst, axis = 1)
median_sale_price.to_csv('data/Median Sale Price.csv')
#median_sale_price

#Creating dataframe containing Homes Sold MoM of each Washington DC region from Feb. 2012 to Oct. 2019 
final_lst_2 = []
i = 0
for df in df_list:
    final_lst_2.append(df["Homes Sold MoM " + "_"+ str(i)][0:93])
    i += 1
homes_sold_mom = pd.concat(final_lst_2, axis = 1)
homes_sold_mom.to_csv('data/Homes Sold MoM.csv')
#homes_sold_mom

#Creating dataframe containing inventory MoM of each Washington DC region from Feb. 2012 to Oct. 2019 
final_lst_3 = []
i = 0
for df in df_list:
    final_lst_3.append(df["Inventory MoM " + "_"+ str(i)][0:93])
    i += 1
inventory_mom = pd.concat(final_lst_3, axis = 1)
inventory_mom.to_csv('data/Inventory MoM.csv')
#inventory_mom

