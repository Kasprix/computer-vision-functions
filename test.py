
from math import sqrt
import math
import numpy as np
import pandas as pd

co_ordinates = [(0,0), (1,1), (2,2), (3,0)]
thetas = [0,30,60,90,120,150]

cos = np.cos(30 / 180. * math.pi)
sin = np.sin(30 / 180. * math.pi)

print(cos - sin)