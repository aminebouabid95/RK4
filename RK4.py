
def RK4(t0,y0,h,T,f):
    import numpy as np
    import sympy
    x=np.linspace(t0,t0+T,100)
    t=t0
    y=y0
    while t<T:  
        k1 = f(t,y)
        k2 = f(t+h/2,y+h*k1/2)
        k3 = f(t+h/2,y+h*k2/2)
        k4 = f(t+h  ,y+h*k3)
        y = y+h/6*(k1+2*k2+2*k3+k4)    
        t = t+h
        
        
RK4(t0=0,y0=1,h=0.1,T=5,f=1/(t+y))