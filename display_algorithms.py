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
        for j in range(l, r):
            global_info.data_array[j][1] = 'white'
        global_info.data_array[r][1] = 'green'
        global_info.data_array[i +
                               1], global_info.data_array[r] = global_info.data_array[r], global_info.data_array[i+1]
        yield i+1

    def quick_sort_algo(l, r):
        if (l < r):
            partition_obj = partition(l, r)
            while not next(partition_obj):
                yield True
            pi = next(partition_obj)
            obj1 = quick_sort_algo(l, pi-1)
            obj2 = quick_sort_algo(pi+1, r)
            while next(obj1):
                yield True
            while next(obj2):
                yield True
        yield False

    obj = quick_sort_algo(0, global_info.data_size-1)
    while next(obj):
        yield True

    for i in range(0, global_info.data_size):
        global_info.data_array[i][1] = 'green'
        yield True

    global_info.sorted = True
    yield True


def merge_sort(global_info):

    def merge(l, mid, r):
        n1 = mid - l + 1
        n2 = r - mid
        arr1 = []
        arr2 = []
        for i in range(0, n1):
            arr1.append(global_info.data_array[l + i])
        for i in range(0, n2):
            arr2.append(global_info.data_array[mid + i + 1])

        p1 = 0
        p2 = 0
        p = l

        while (p1 < n1 and p2 < n2):
            if (arr1[p1][0] < arr2[p2][0]):
                global_info.data_array[p] = arr1[p1]
                yield False
                p = p+1
                p1 = p1+1
            else:
                global_info.data_array[p] = arr2[p2]
                yield False
                p = p+1
                p2 = p2+1

        while (p1 < n1):
            global_info.data_array[p] = arr1[p1]
            yield False
            p = p + 1
            p1 = p1+1

        while (p2 < n2):
            global_info.data_array[p] = arr2[p2]
            yield False
            p = p+1
            p2 = p2+1
        yield True

    def merge_sort_algo(l, r):
        if (l < r):
            mid = (l+r)//2

            obj1 = merge_sort_algo(l, mid)
            obj2 = merge_sort_algo(mid+1, r)

            while next(obj1):
                yield True
            while next(obj2):
                yield True

            merge_obj = merge(l, mid, r)

            while not next(merge_obj):
                yield True
        yield False

    obj = merge_sort_algo(0, global_info.data_size-1)
    while next(obj):
        yield True

    for i in range(0, global_info.data_size):
        global_info.data_array[i][1] = 'green'
        yield True

    global_info.sorted = True
    yield True
