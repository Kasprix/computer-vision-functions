
from math import sqrt
import math
import numpy as np
import pandas as pd

co_ordinates = [(0,0), (1,1), (2,2), (3,0)]
thetas = [0,45,90,135]

def hough_transform(width, height, thetas, co_ordinates):

    r_value = int( round( sqrt( (width-1)**2 + (height-1)**2) , 0))

    # x2 + 1 to factor in the zero
    d = pd.DataFrame(np.zeros((r_value*2+1, len(thetas))), columns=thetas)

    d.index = range(r_value,-r_value-1,-1)



    print(d)


    for x in range(len(co_ordinates)):
        print("Current coordinate)", co_ordinates[x])
        for y in thetas:

            # REMEMBER, values are in radians for cos and sin function
            value = round( (co_ordinates[x][1]* math.cos(( y / 180) * math.pi)) - (co_ordinates[x][0]*math.sin(( y / 180) * math.pi)), 1)

            if (float(value) % 1) >= 0.5:
                rounded = math.ceil(value)
            else:
                rounded = round(value)


            d.at[rounded, y] += 1

            print("Theta:", y, value)



    return d


print(hough_transform(3, 4 ,thetas ,co_ordinates))