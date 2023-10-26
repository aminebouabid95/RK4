def f(x,y):
    return x+1/y


def RK4(x0,y0,h,T):
    Y=[]
    import numpy as np
    import matplotlib.pyplot as plt
    X=np.linspace(x0,x0+T,51)
    x=x0
    y=y0
    while x<T:  
        k1 = f(x,y)
        k2 = f(x+h/2,y+h*k1/2)
        k3 = f(x+h/2,y+h*k2/2)
        k4 = f(x+h  ,y+h*k3)
        y = y+h/6*(k1+2*k2+2*k3+k4)    
        x = x+h
        Y.append(y)
    plt.plot(X,Y)
    plt.show()
RK4(x0=0,y0=1,h=0.1,T=5)