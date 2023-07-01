def bubble_sort(global_info):
    n = global_info.data_size
    lst = global_info.data_array
    for i in range(0,n-1):
        for j in range(0, n-i-1):
            lst[j][1] = 'red'
            global_info.draw_data(j)
            if (lst[j][0] > lst[j+1][0]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
            lst[j][1] = 'white'
            yield lst
        lst[n-i-1][1] = 'green'
    lst[0][1] = 'green'
    global_info.sorted = True
    yield lst

def insertion_sort(global_info):
    