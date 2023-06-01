import random

lower_limit = 1
upper_limit = 100
array_length = 10  # Specify the desired length of the array

random_array = random.sample(range(lower_limit, upper_limit + 1), array_length)
data_array = random.sample(range(1, 101), 15)

some_array = []

for index, element in enumerate(data_array):
    some_array += [(element, True)]

def Bubble_Sort():
    for i in range(0, len(some_array)):
        for j in range(0,i):
            if (some_array[j] > some_array[i]):
                temp = some_array[j]
                some_array[j] = some_array[i]
                some_array[i] = temp 

print(some_array)
Bubble_Sort()
print(some_array)