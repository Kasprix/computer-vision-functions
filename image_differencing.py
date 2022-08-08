
# TUTORIAL 8
from distance_functions import sum_of_absolute_difference


frame_1 = [190, 200, 90, 110, 90]
frame_2 = [110, 170, 160, 70, 70]
frame_3 = [100, 60, 170, 200, 90]
frame_4 = [90, 100, 100, 190, 190]

THRESHOLD = 50


answer_1 = []

for x in range(len(frame_1)):
    result = sum_of_absolute_difference(frame_2[x],frame_3[x])
    if result >= 50:
        result = 1
    else: result = 0


    answer_1.append(result)

print(answer_1)