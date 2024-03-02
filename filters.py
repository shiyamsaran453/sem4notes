#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 as cv
import matplotlib.pyplot as plt
import numpy as npy


# In[2]:


read=cv.imread("C:/Users/TEMP.DESKTOP-2JNK8R3.001/Downloads/ai.jpg")
read


# In[3]:


kernal =npy.ones((3,3),npy.float32)/9
kernal


# In[4]:


fil=cv.filter2D(read,-1,kernal)
cv.imshow("fil",fil)
cv.waitKey(0)
cv.destroyAllWindows()


# In[5]:


fil


# # bluring

# In[6]:


read1=cv.imread("C:/Users/TEMP.DESKTOP-2JNK8R3.001/Downloads/ai5.jpg")


# In[7]:


blur=cv.blur(read1,(5,5))
cv.imshow("blur",blur)
cv.imshow("read1",read1)
cv.waitKey(0)
cv.destroyAllWindows()


# # gaussian blur

# In[8]:


read2=cv.imread("C:/Users/TEMP.DESKTOP-2JNK8R3.001/Downloads/ai5.jpg")
gaus_blur=cv.GaussianBlur(read2,(5,5),0)
cv.imshow("gblur",gaus_blur)
cv.imshow("read",read2)
cv.imshow("blur",blur)
cv.waitKey(0)
cv.destroyAllWindows


# # bilateral filter

# In[11]:


read3=cv.imread("C:/Users/TEMP.DESKTOP-2JNK8R3.001/Downloads/ai5.jpg")
bi_fil=cv.bilateralFilter(read3,9,60,90)
cv.imshow("bi blur",bi_fil)
cv.imshow("read",read3)
cv.imshow("blur",blur)
cv.imshow("gblur",gaus_blur)
cv.waitKey(0)
cv.destroyAllWindows


# # median filters

# In[15]:


read4=cv.imread("C:/Users/TEMP.DESKTOP-2JNK8R3.001/Downloads/ai5.jpg")
me_fil=cv.medianBlur(read4,7)
cv.imshow("median",me_fil)
cv.imshow("bi blur",bi_fil)
cv.imshow("read",read3)
cv.imshow("blur",blur)
cv.imshow("gblur",gaus_blur)
cv.waitKey(0)
cv.destroyAllWindows


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




