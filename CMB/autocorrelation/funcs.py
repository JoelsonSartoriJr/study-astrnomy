import math
import numpy as np

def f(x:list)->list:
    y = 0
    try:
        n = len(x)
        y = np.zeros(n)
        for i in range(n):
            if x[i]>0: y[i] = f(x[i])
    except:
        if x>0:
            y = 20*x*math.exp(-10*x)
    
    return y

def f_dois(x:float)->float:
    y = np.sin(10*x)*np.exp(-10*np.fabs(x))
    return y
    
    
prod = lambda x, h: f(x)*f(x+h)

prod_dois = lambda x, h: f_dois(x)*f_dois(x+h)