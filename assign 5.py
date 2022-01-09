#!/usr/bin/env python
# coding: utf-8

# In[15]:


class py_solution:
    def pow(self, x, n):
        if x==0  or n==1:
            return x 
        val = self.pow(x, n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(py_solution().pow(10, 2));


# In[ ]:





# In[ ]:




