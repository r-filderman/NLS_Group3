#!/usr/bin/env python
# coding: utf-8

# In[6]:


import PyPDF2 as PDF #import pdf module 
import re

p = PDF.PdfFileReader("covid-icf-iid-response-plan_TX.pdf")

# get number of pages
NumPages = p.getNumPages()

#define keyterms; Hi, Hello

kTerm = "COVID, Racial, disparities, COVID-19"

#extract text and do the search
for i in range(0, NumPages):
    PageObj = p.getPage(i)
    print("Looking through page " + str(i))
    Text = PageObj.extractText()
    Result = re.search(kTerm,Text)

    if Result:
         print(f"{kTerm} found")
    else:
         print("0")


# In[10]:


import glob
filenames = glob.glob(NLP\NLP Project)
print(filenames)


# In[ ]:




