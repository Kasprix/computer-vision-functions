import numpy as np
from scipy.optimize import linear_sum_assignment


cluster_point_1 = [14.167, 10.833, 12.5]

cluster_point_2 = [10,10,28.33]


feature_vector = [
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
        total = total + abs(list1[x] - list2[x])

    #cost_matrix = np.abs(arr1 - arr2[:, None])
    #pairs = linear_sum_assignment(cost_matrix)
    
    return round(total, 2)

for x in range(len(feature_vector)):
    print(sad(cluster_point_2, feature_vector[x]))
    print("\n")
