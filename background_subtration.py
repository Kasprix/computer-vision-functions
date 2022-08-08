
# TUTORIAL 8
from distance_functions import sum_of_absolute_difference


frame_1 = [190, 200, 90, 110, 90]
frame_2 = [110, 170, 160, 70, 70]
frame_3 = [100, 60, 170, 200, 90]
frame_4 = [90, 100, 100, 190, 190]



Frame_1_new = [95.0, 100.0, 45.0, 55.0, 45.0]
Frame_2_new = [7.5, 35.0, 57.5, 7.5, 12.5]


THRESHOLD = 38

B = 0.5

frames = [
[190, 200, 90, 110, 90],
[110, 170, 160, 70, 70],
[100, 60, 170, 200, 90],
[90, 100, 100, 190, 190],   
]



# INITIAL CALCULATION

follow_through = []

moving_value = []

for x in range(len(frames[0])):
    moving_value.append(0.5*frames[0][x])


print(moving_value)

for iteration in range(1,len(frames)):
    new_update = []
    new_sad = []
    for x in range(len(moving_value)):
        result = 0.5*moving_value[x] + 0.5*frames[iteration][x]

        difference = sum_of_absolute_difference(result, moving_value[x])

        new_update.append(result)
        new_sad.append(difference)

    
    print(new_update)
    print(new_sad, "\n")
    moving_value = new_update







'''
for iteration in range(len(frames)):
    answer = []




    for x in range(len(frames[0])):

        result = sum_of_absolute_difference(0.5*(new_pass[x]), 0.5*(frames[iteration][x]))


        if result >= 50:
            result = 1
        else: result = 0


        answer.append(result)

        print(answer)

'''