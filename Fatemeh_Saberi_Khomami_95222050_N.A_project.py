#if you do not have 'numpy' and 'sympy' libraries on your computer, please install it via the bellow commands in cmd
#pip install numpy
#pip install sympy

#import libraries
from sympy import symbols , simplify
import numpy as np

#define interpolation functions
def lagrange(lst_x,lst_y,est_point):
    x = symbols('x')
    lagrangee= []
    for i in range(0, (len(lst_x))):
        up = 1
        down = 1
        for j in range(0, (len(lst_x))):

            if(j==i):
                continue
            else:
                up*=(x- lst_x[j])
            down=up.subs(x,lst_x[i])

        lagrangee.append((up / down))
    p=sum(np.multiply(lst_y, lagrangee))
    print('\n','our interpolation function via lagrange is :',simplify(p),'\n')
    print('our estimation for x= {} via lagrange method is : '.format(est_point),(p.subs(x,est_point)).evalf())


def newton(ls_x, ls_y, est_point):
    x = symbols('x')

    F = {}
    for i in range(0, len(ls_x)):
        F[str(0) + str(i)] = ls_y[i]

    for i in range(1, len(ls_x)):
        for j in range(0, (len(ls_x) - i)):
            F[str(i) + str(j)] = (F[str(i - 1) + str(j + 1)] - F[str(i - 1) + str(j)]) / (ls_x[j + i] - ls_x[j] )

    crs = [1]
    for i in range(1, (len(ls_x))):
        temp = 1
        for j in range(0, i):
            temp *= (x - ls_x[j])
        crs.append(temp)

    p = 0
    for i in range(0, len(ls_x)):
        p += np.multiply(F[str(i) + str(0)], crs[i])

    print('\n', 'our interpolation function via newton is :', p, '\n')
    print('our estimation for x= {} via newton method is : '.format(est_point), (p.subs(x, est_point)).evalf())

def forward(ls_x,ls_y,est_point):

    F={}
    for i in range(0  , len(ls_x)):
        F[str(0)+str(i)]=ls_y[i]


    for i in range(1 , len(ls_x)):
        for j in range(0 , (len(ls_x)-i)):
            F[str(i)+str(j)]= F[str(i-1)+str(j+1)]- F[str(i-1)+str(j)]

    h=(ls_x[((len(ls_x))-1)]-ls_x[0])/((len(ls_x))-1)
    s=(est_point - ls_x[0])/h
    comb=[1]
    for i in range(1, (len(ls_x))):
        up = 1
        down = np.prod( range(  1,(i+1)  ) )
        for j in range(0 , i):
            up *= (s-j)
        comb.append(up/down)

    p=0
    for i in range(0  , len(ls_x)):
        p+=np.multiply(F[str(i) + str(0)], comb[i])

    print('\n','our estimation for x= {} via forward method is : '.format(est_point),p)


#test the methods
lagrange([0,1,8,27,64],[0,1,2,3,4],20)
newton([-1,1,2,3],[-2,0,7,26],0.5)
forward([4,6,8,10],[1,-2,-3,-6],7)


