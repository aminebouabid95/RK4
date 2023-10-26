# Author: Amine BOUABID
# This script solves ordinary differential equations using the the 4th order Runge-Kutta method (RK4)
# It takes as input a mathematical expression f expressed in terms of t and y, and 5 variables defined as follows:

# t0 and y0: Initial conditions
# h: Step size
# tf: Final time value 
# showPoints: Plots the calculated points on the curve

# Numerical Values of y are stored in the list Y and printed automatically along with step and time.
# Finally the script plots Y =f(X) using the numerically calculated values 
# The number of steps depends on the time interval and the step size. It is calculated as follows: n=(tf-t0)/h
# for an interval T = tf - t0 = 5, and h=0.05, the number of steps would be n = 100

def f(y,t):
    import numpy as np
    return 2*(1-y) - np.exp(-4*t)


def RK4(f,t0,y0,h,tf,showPoints):
    Y=[]
    import numpy as np
    import matplotlib.pyplot as plt
    n=int((tf-t0)/h)
    T=np.linspace(t0,tf,n)
    t=t0
    y=y0
    print('----------------------------')
    print('|step   |t       |y      ')
    for i in range(1,n+1):  
        k1 = f(y,t)
        k2 = f(y+k1/2,t+h/2)
        k3 = f(y+k2/2,t+h/2)
        k4 = f(y+k3 ,t+h)
        y = y+h/6*(k1+2*k2+2*k3+k4)    
        t = t+h
        Y.append(y)
        print('----------------------------')
        print('|%3d    |%3.3f   |%3.3f '%(i,t,y))
    print('-------------------------')
    
    #################### Plot ####################  
    plt.grid('both')
    plt.xlabel("t (s)")
    plt.ylabel("y (-)")
    plt.plot(T,Y,color='blue',linewidth=2)
    if showPoints: 
        plt.scatter(T,Y, color='red', s=20)
        plt.scatter([T[0], T[-1]],[Y[0], Y[-1]], color='green', s=40)
    plt.show()
    
# Uncomment to call method
RK4(f,t0=0,y0=1,h=0.02,tf=2,showPoints=False)