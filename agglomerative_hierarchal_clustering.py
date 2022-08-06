import numpy as np
from scipy.optimize import linear_sum_assignment




feature_vector = [
    [6.67, 8.33, 15],
    [10, 15, 30],
    [10, 10, 25],

    [5, 20, 15],
    [10, 5, 30],

    [30, 10, 7.5],
]



def agglo_round(feature_vector):
    for x in feature_vector:
        print("\nCurrent Vector:", x)
        for y in feature_vector:
            total = sad(x,y)
            if total == 0:
                break

            print(sad(x, y))            



def sad(list1, list2):
    total = 0 
    for x in range(len(list1)):
        total = total + abs(list1[x] - list2[x])

    #cost_matrix = np.abs(arr1 - arr2[:, None])
    #pairs = linear_sum_assignment(cost_matrix)
    
    return round(total, 2)

"""
for x in range(len(feature_vector)):
    print(sad(cluster_point_2, feature_vector[x]))
    print("\n")
"""

agglo_round(feature_vector)

'''
# input pairs to find average
average = round((feature_vector[0][0] + feature_vector[3][0] + feature_vector[6][0]) /3, 3)
print(average)
'''

'''
# input pairs to find average (THIS VERSION IS WHEN YOU'RE ADDING A NEW VALUE TO A GROUPING)
average = round(((feature_vector[0][0] * (LENGTH OF GROUP)) + feature_vector[3][0] /3, 3)
print(average)
'''