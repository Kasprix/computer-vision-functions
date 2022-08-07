from cmath import sqrt
import numpy as np
import pandas as pd

from distance_functions import sum_of_absolute_difference

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







'''def hough_transform(width, height, thetas, coordinates):

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


print(hough_transform(3, 4 ,thetas ,co_ordinates))'''


