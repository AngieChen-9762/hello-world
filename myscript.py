#!/usr/bin/env python
# coding: utf-8

# In[1]:


def square(x):
    '''square a number'''
    return x ** 2

for N in range(1, 4):
    print(N, 'squared is', square(N))

