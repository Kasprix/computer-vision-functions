from cmath import sqrt
from distance_functions import sum_of_absolute_difference


template = [
    100,150,200,
    150,10,200,
    200,200,250
]

image_area = [
    50,40,40,
    100,100,80,
    20,200,80
]

def square(list):
    return [i ** 2 for i in list]



template_sqrt = sqrt(sum(square(template)))
image_area_sqrt = sqrt(sum(square(image_area)))

numerator = 0

for x in range(len(template)):
    numerator += template[x] * image_area[x]

similarity = numerator / (template_sqrt * image_area_sqrt)

print("Similarity =", round(similarity.real, 2))

sad = 0
for x in range(len(template)):
    sad += sum_of_absolute_difference(template[x], image_area[x])

print("SAD =", sad)