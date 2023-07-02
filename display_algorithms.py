def bubble_sort(global_info):
    n = global_info.data_size
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            global_info.data_array[j][1] = 'red'
            # global_info.draw_data(j)
            if (global_info.data_array[j][0] > global_info.data_array[j+1][0]):
                global_info.data_array[j], global_info.data_array[j +
                                                                  1] = global_info.data_array[j+1], global_info.data_array[j]
                global_info.data_array[j][1] = 'grey'
            else: 
                global_info.data_array[j][1] = 'yellow'
            yield True
        for j in range(0, n-i-1):
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
            # global_info.draw_data(j)
            # global_info.draw_data(j+1)
            j = j-1
            yield True
        global_info.data_array[j+1][1] = 'grey'
    for i in range(0, n):
        global_info.data_array[i][1] = 'green'
        yield True
    global_info.sorted = True
    yield True


def quick_sort(global_info):

    def partition(l, r):
        global_info.data_array[r][1] = 'red'
        pivot = global_info.data_array[r][0]
        i = l - 1
        for j in range(l, r):
            if global_info.data_array[j][0] < pivot:
                i = i + 1
                global_info.data_array[j][1] = 'grey'
                global_info.data_array[i], global_info.data_array[j] = global_info.data_array[j], global_info.data_array[i]
                yield False
            else:
                global_info.data_array[j][1] = 'yellow'
                yield False
        yield True
        for j in range(l,r):
            global_info.data_array[j][1] = 'white'
        global_info.data_array[r][1] = 'green'
        global_info.data_array[i +
                               1], global_info.data_array[r] = global_info.data_array[r], global_info.data_array[i+1]
        yield i+1

    def quick_sort_help(l, r):
        partition_obj = partition(l, r)
        if (l < r):
            while not next(partition_obj):
                yield True
            pi = next(partition_obj)
            obj1 = quick_sort_help(l, pi-1)
            obj2 = quick_sort_help(pi+1, r)
            while next(obj1):
                yield True
            while next(obj2):
                yield True
        yield False

    obj = quick_sort_help(0, global_info.data_size-1)
    while next(obj):
        yield True
    
    for i in range(0, global_info.data_size):
        global_info.data_array[i][1] = 'green'
        yield True

    global_info.sorted = True
    yield True


def merge_sort(global_info):
    global_info.sorted = True
    yield True
