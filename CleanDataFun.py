#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import json
from pandas.io.json import json_normalize


# In[3]:


def cleanData(filePath, filePathJson, encoding):
    data = pd.read_csv(filePath, encoding=encoding)
    data['trending_date'] = '20' + data['trending_date']
    data['trending_date'] = pd.to_datetime(data['trending_date'],format='%Y.%d.%m')
    data['publish_time'] = data['publish_time'].replace(regex=True,to_replace=r"T.*",value=r'')
    data['publish_time'] = pd.to_datetime(data['publish_time'],format='%Y-%m-%d', errors='coerce')
    categories = pd.read_json(filePathJson)
    catData = json_normalize(categories['items'])
    idToCategories = pd.DataFrame(columns=['category_id', 'category'])
    idToCategories['category_id'] = catData['id']
    idToCategories['category'] = catData['snippet.title']
    idToCategories['category_id'] = idToCategories['category_id'].astype('int64')
    myData = pd.merge(data, idToCategories)
    myData = myData.drop(columns='category_id')
    myData['tags'] = myData.tags.str.strip().str.lower().str.replace('"','').str.replace('|',',')
    myData = myData.drop_duplicates()
    return myData

def cleanToCsv(existingFilePath, existingFilePathJson, newFilePathCsv, encoding):
    df = cleanData(existingFilePath, existingFilePathJson,encoding)
    df.to_csv(newFilePathCsv, index = None, header=True)

# In[ ]:




