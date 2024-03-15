#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize



# In[5]:


text = input("Enter text")

words = word_tokenize(text)

porter_stemmer = PorterStemmer()
stemmed_words = [porter_stemmer.stem(word) for word in words]

print("Stemmed Words:")
print(stemmed_words)

wordnet_lemmatizer = WordNetLemmatizer()
lemmatized_words = [wordnet_lemmatizer.lemmatize(word) for word in words]

print("\nLemmatized Words:")
print(lemmatized_words)


# In[ ]:
