from cmath import sqrt
import numpy as np
from scipy.optimize import linear_sum_assignment

from distance_functions import sum_of_absolute_difference


CLUSTER_POINT_1 = [14.167, 10.833, 12.5]

CLUSTER_POINT_2 = [10,10,28.33]

FEATURE_VECTOR = [
    [5, 10, 15],
    [10, 15, 30],
    [10, 10, 25],

    [10, 10, 15],
    [5, 20, 15],
    [10, 5, 30],

    [5, 5, 15],
    [30, 10, 5],
    [30, 10, 10]
]


def sad(list1, list2):
    total = 0
    for x in range(len(list1)):
        total = total + sum_of_absolute_difference(list1[x], list2[x])

    #cost_matrix = np.abs(arr1 - arr2[:, None])
    #pairs = linear_sum_assignment(cost_matrix)
    
    return round(total, 2)

for x in range(len(FEATURE_VECTOR)):
    print(sad(CLUSTER_POINT_2, FEATURE_VECTOR[x]))
    print("\n")
