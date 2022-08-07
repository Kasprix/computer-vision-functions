def ransac(disparity_values, left_coordinates, right_coordinates):

    for x in disparity_values:
        print("FOR:", x)
        count = 0
        consensus_set = 0

        for left_disparity in left_coordinates:

            difference = 0

            x_value = left_disparity[0] - x[0] 
            y_value = left_disparity[1] - x[1]

            

            difference += sum_of_absolute_difference(x_value, right_coordinates[count][0])
            difference += sum_of_absolute_difference(y_value, right_coordinates[count][1])

           

            if difference < 20:
                consensus_set+=1
                print("INLIER", left_disparity)
                print(" ", left_disparity, "-", x, "=", "(" + str(x_value) + ", " + str(y_value) + ")")
                print("     Actual Match is ", right_coordinates[count])
            
            count += 1


ransac(disparity_values, left_image_coordinates, coordinate_match_list)