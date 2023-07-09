def swap(global_info, x, y):
    global_info.data_array[x], global_info.data_array[y] = global_info.data_array[y], global_info.data_array[x]
    global_info.colors[x], global_info.colors[y] = global_info.colors[y], global_info.colors[x]


def bubble_sort(global_info):
    n = global_info.data_size
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            global_info.colors[j] = 'red'
            # global_info.draw_data(j)
            if (global_info.data_array[j] > global_info.data_array[j+1]):
                swap(global_info, j, j+1)
                global_info.colors[j] = 'grey'
            else:
                global_info.colors[j] = 'yellow'
            yield True
        for j in range(0, n-i-1):
            global_info.colors[j] = 'white'
        global_info.colors[n-i-1] = 'green'
    global_info.colors[0] = 'green'
    global_info.sorted = True
    yield True


def insertion_sort(global_info):
    n = global_info.data_size
    global_info.colors[0] = 'grey'
    for i in range(1, n):
        global_info.colors[i] = 'red'
        curr = global_info.data_array[i]
        j = i-1
        while ((global_info.data_array[j] > curr) & (j >= 0)):
            global_info.data_array[j+1] = global_info.data_array[j]
            global_info.data_array[j] = curr
            # global_info.draw_data(j)
            # global_info.draw_data(j+1)
            j = j-1
            yield True
        global_info.colors[j+1] = 'grey'
    for i in range(0, n):
        global_info.colors[i] = 'green'
        yield True
    global_info.sorted = True
    yield True


def quick_sort(global_info):

    def partition(l, r):
        global_info.colors[r] = 'red'
        pivot = global_info.data_array[r]
        i = l - 1
        for j in range(l, r):
            if global_info.data_array[j] < pivot:
                i = i + 1
                global_info.colors[j] = 'cyan'
                swap(global_info, i, j)
            else:
                global_info.colors[j] = 'yellow'
            yield False
        yield True
        for j in range(l, r):
            global_info.colors[j] = 'white'
        global_info.colors[r] = 'green'
        swap(global_info, i+1, r)
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
        global_info.colors[i] = 'green'
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
            global_info.colors[l+i] = 'yellow'
            yield False
        for i in range(0, n2):
            arr2.append(global_info.data_array[mid + i + 1])
            global_info.colors[mid + i + 1] = 'cyan'
            yield False

        p1 = 0
        p2 = 0
        p = l

        while (p1 < n1 and p2 < n2):
            if (arr1[p1] < arr2[p2]):
                global_info.data_array[p] = arr1[p1]
                global_info.colors[p] = 'grey'
                yield False
                p = p+1
                p1 = p1+1
            else:
                global_info.data_array[p] = arr2[p2]
                global_info.colors[p] = 'grey'
                yield False
                p = p+1
                p2 = p2+1

        while (p1 < n1):
            global_info.data_array[p] = arr1[p1]
            global_info.colors[p]= 'grey'
            yield False
            p = p + 1
            p1 = p1+1

        while (p2 < n2):
            global_info.data_array[p] = arr2[p2]
            global_info.colors[p] = 'grey'
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
        global_info.colors[i] = 'green'
        yield True

    global_info.sorted = True
    yield True


def selection_sort(global_info):
    for i in range(global_info.data_size):
        for j in range(i+1, global_info.data_size):
            global_info.colors[j] = 'white'
        global_info.colors[i] = 'yellow'
        min_idx = i
        for j in range(i+1, global_info.data_size):
            if (global_info.data_array[min_idx] > global_info.data_array[j]):
                min_idx = j
                global_info.colors[min_idx] = 'red'
            yield True
            global_info.colors[j] = 'grey'
        global_info.colors[i] = 'grey'
        global_info.colors[min_idx] = 'green'
        swap(global_info, i, min_idx)
        yield True

    global_info.sorted = True
    yield True


def radix_sort(global_info):

    def counting_sort():

        global exp1
        exp1 *= 10

        n = global_info.data_size

        output = [0]*(n)
        count = [0]*(10)

        for i in range(0, n):
            index = global_info.data_array[i][0] // exp1
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = global_info.data_array[i][0] // exp1
            output[count[index % 10] - 1] = global_info.data_array[i][0]
            count[index % 10] -= 1
            i -= 1

        i = 0
        for i in range(0, global_info.data_size):
            global_info.data_array[i][0] = output[i]
            yield True

    max1 = -1
    for i in global_info.data_array:
        max1 = max(max1, i[0])

    global exp1
    exp1 = 1
    obj1 = counting_sort()
    while max1 / exp1 >= 1:
        next(obj1)
        yield True

    for i in range(0, global_info.data_size):
        global_info.data_array[i][1] = 'green'
        yield True

    global_info.sorted = True
    yield True
