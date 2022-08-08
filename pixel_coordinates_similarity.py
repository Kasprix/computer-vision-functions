from cmath import sqrt
import numpy as np
import pandas as pd

from distance_functions import sum_of_absolute_difference

# FROM TUTORIAL 6

WIDTH = 4
HEIGHT = 3

# Input mask with padding if needed
MASK = [4,7,6,3,4,5,8,7,6]
IMAGE = np.array([7, 6, 7, 5, 4, 5, 4, 5, 7, 6, 8, 7])


formatted = IMAGE.reshape(HEIGHT, WIDTH)


formatted_dataframe = pd.DataFrame(formatted, columns=range(1, WIDTH+1))
formatted_dataframe.index = range(1 ,HEIGHT+1)

print(formatted_dataframe)

def get_neighbours(image, x_coordinate, y_coordinate):

    sad_list = []

    # If height is 3
    for x in range(-1, 2, 1):

        # remember format for at is [row, column]
        try:
            sad_list.append( image.at[y_coordinate+x, x_coordinate-1] )
        except Exception as e:
            # pad zero
            sad_list.append(0)

        try:
            sad_list.append( image.at[y_coordinate+x, x_coordinate] )
        except Exception as e:
            # pad zero
            sad_list.append(0)

        try:
            sad_list.append( image.at[y_coordinate+x, x_coordinate+1] )
        except Exception as e:
            # pad zero
            sad_list.append(0)
                
    # print(sad_list)
    return sad_list


sum_of_absolute_differences = []


for y in range(1, HEIGHT+1):
    for x in range(1, WIDTH+1):
        sad_list = get_neighbours(formatted_dataframe, x, y)

        total = 0
        for x in range(len(MASK)):
            sad = sum_of_absolute_difference(MASK[x], sad_list[x])
            total += sad

        sum_of_absolute_differences.append(total)


sum_of_absolute_differences = np.array(sum_of_absolute_differences)
sum_of_absolute_differences = sum_of_absolute_differences.reshape(HEIGHT, WIDTH)
print(sum_of_absolute_differences)
