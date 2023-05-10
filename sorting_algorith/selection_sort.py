#selection sort method

def selection_sort(array_1):
    for i in range(len(array_1)):
        miniIndex = i
        for j in range(i+1, len(array_1)):
            if array_1[miniIndex] > array_1[j]:
                miniIndex = j
        array_1[i], array_1[miniIndex] = array_1[miniIndex], array_1[i]
    return array_1
