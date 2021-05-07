#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import glob
import time

import pandas as pd


# In[ ]:


data_path = "/DATA/7A/xblock/"
df_path = "/DATA/7A/assets/dataframes/"

#
erc20_transactions_path = "ERC20Transactions/uncompressed"
erc721_transactions_path = "ERC721Transactions/uncompressed"
internal_transactions_path = "InternalTransactions/uncompressed"
normal_transactions_path = "NormalTransactions/uncompressed"

#token information
token_info_path = "TokenInfo/uncompressed/"
erc20_filename = "ERC20TokenInfo.csv"
erc721_filename = "ERC721TokenInfo.csv"


# ## Read raw data from disk

# In[ ]:


#read all erc721 transactions
all_files = glob.glob(data_path + internal_transactions_path + "/*.csv")

li = []
bs = time.time()
for filename in all_files:
    start = time.time()
    print("Reading file", filename, "...", end="", flush=True)
    dfd = pd.read_csv(filename, index_col=None, header=0)
    li.append(dfd)
    end = time.time()
    print("took", end - start, "seconds.")
be = time.time()
print("Total:", be - bs, "seconds.")

df = pd.concat(li, axis=0, ignore_index=True)
print(df.shape[0])
print(df.head())


# ### pandas df problems

# In[6]:


#df.drop('value',axis='columns', inplace=True) #for erc20Transactions
#df.drop('tokenId',axis='columns', inplace=True) #for erc721Transactions
print(df.dtypes)


# ## Store DataFrame

# In[7]:


file_name = "internalTransactions.df"

s = time.time()
#df.drop('tokenId',axis='columns', inplace=True) #for erc721Transactions
df.to_feather(df_path + file_name)
e = time.time()
"Took", e - s, " seconds."


# ## Reaf DataFrame from Disk

# In[10]:


file_name = "internalTransactions.df"

s = time.time()
df = pd.read_feather(df_path + file_name)
e = time.time()
print("Took", e - s, " seconds.")
print(df.head(5))


# In[ ]:




