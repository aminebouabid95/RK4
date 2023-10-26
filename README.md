This script solves ordinary differential equations using the the 4th order Runge-Kutta method (RK4)
It takes as input a mathematical expression f expressed in terms of t and y, and 5 variables defined as follows:

t0 and y0: Initial conditions
h: Step size
tf: Final time value 
showPoints: Plots the calculated points on the curve

Numerical Values of y are stored in the list Y and printed automatically along with step and time.
Finally the script plots Y =f(X) using the numerically calculated values 
The number of steps depends on the time interval and the step size. It is calculated as follows: n=(tf-t0)/h
for an interval T = tf - t0 = 5, and h=0.05, the number of steps would be n = 100