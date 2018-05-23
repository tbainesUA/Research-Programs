
# coding: utf-8

# In[1]:


import numpy as np


# In[30]:


def Chi_Sqaure(Observed, Expected, Observed_Uncertainty):
    # This function takes in inputs: Observed Measured Value
    #                                Expect Model Value
    #                                Observed Uncertainty in measured value
    #
    # This function computes and returns the chi square value to test how well the data fits to a model
    #                                 
    #                                X^2 = (y_n - f(x_n))^2/ y_n_err^2 : sum over all possible n 
    #                                
    return np.sum(((Observed-Expected)/Observed_Error)**2)
