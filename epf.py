#!/usr/bin/env python3

import math
from itertools import combinations


def calc_slope_intercept(point,name=''):
    x,z,theta=point

    m=-1*math.tan(theta*math.pi / 180)
    b=x-m*z

    return (m,b, name, x,z,theta)


def intersect_of(p1,p2):
    m1,b1, n1, _,_,_ = p1
    m2,b2, n2 , _,_,_= p2

    if m1==m2:
        return None
    
    x = (b1*m2 - b2*m1) / (m2 -m1)
    z = (b1 - b2) / (m2 - m1)

    return (f'{n1} x {n2}', x, z)


def find_end(plist):
    plist=[calc_slope_intercept(p,f'P{i}') for i,p in enumerate(plist)]

    results=[]
    for pair in combinations(plist,2):
        results.append(intersect_of(*pair))

    return results


if __name__ == '__main__':

    test=[ [-200, -40, 162.3],
           [-1103,  0, -166.0 ]
         ]

    enigmatica6_world3=[ [5687, 919, -179.9],
           [4931, 908, -144.6]
         ]

    AOF5_world8 = [ 
        [139.613, 32.967, 73.4],
        [89.282, 1333.258, 123.6]
    ]

    print(find_end(AOF5_world8))