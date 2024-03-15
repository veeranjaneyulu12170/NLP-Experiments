#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[2]:


nltk.download('punkt')
nltk.download('stopwords')


# In[13]:


text = "Let us remove some of the stop words."


# In[14]:


tokens = word_tokenize(text)


# In[15]:


stop_words = set(stopwords.words('english'))


# In[16]:


filtered_tokens = [word for word in tokens if word.lower() not in stop_words]


# In[17]:


filtered_text = ' '.join(filtered_tokens)


# In[18]:


print("Original Text:")
print(text)


# In[19]:


print("\nText after removing stopwords:")
print(filtered_text)


# In[ ]:
