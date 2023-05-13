#selection sort algorithm (stable version)

def stableSelectionSort(array, n):
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        key = array[min_idx]
        while min_idx > i:
            array[min_idx] = array[min_idx - 1]
            min_idx -= 1
        array[i] = key
 
def printArray(array, n):
    for i in range(n):
        print("%d" % array[i], end=" ")
     
# Driver Code
array = [4, 5, 3, 2, 4, 1]
n = len(array)
stableSelectionSort(array, n)
printArray(array, n)
