from cmath import sqrt


def sum_of_absolute_difference(x, y):
    result = abs(x - y)

    return result

def eucludian_distance(x, y):
    result = sqrt((x - y)**2)

    return result

def sum_of_squared_difference(x, y):
    result = (x - y)**2

    return result


image = [.1,.1,1]

others = [
    [1,.8,1],
    [.1,.1,.7],
    [1,.4,0],
    [1,1,0.9],
    [.5,.8,1]
]


for x in range(len(others)):
    result = 0
    for y in range(len(image)):
        result += sum_of_absolute_difference(image[y], others[x][y])
    print(result)