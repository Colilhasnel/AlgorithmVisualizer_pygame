def bubble_sort(global_info):
    n = global_info.data_size
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            global_info.data_array[j][1] = 'red'
            global_info.draw_data(j)
            if (global_info.data_array[j][0] > global_info.data_array[j+1][0]):
                global_info.data_array[j], global_info.data_array[j +
                                                                  1] = global_info.data_array[j+1], global_info.data_array[j]
            yield True
            global_info.data_array[j][1] = 'white'
        global_info.data_array[n-i-1][1] = 'green'
    global_info.data_array[0][1] = 'green'
    global_info.sorted = True
    yield True


def insertion_sort(global_info):
    n = global_info.data_size
    global_info.data_array[0][1] = 'grey'
    for i in range(1, n):
        global_info.data_array[i][1] = 'red'
        curr = global_info.data_array[i]
        j = i-1
        while ((global_info.data_array[j][0] > curr[0]) & (j >= 0)):
            global_info.data_array[j+1] = global_info.data_array[j]
            global_info.data_array[j] = curr
            j = j-1
            yield True
        global_info.data_array[j+1][1] = 'grey'
    for i in range(0,n):
        global_info.data_array[i][1] = 'green'
        yield True
    global_info.sorted = True
    yield True

def quick_sort(global_info):
    global_info.sorted = True
    yield True


def merge_sort(global_info):
    global_info.sorted = True
    yield True
