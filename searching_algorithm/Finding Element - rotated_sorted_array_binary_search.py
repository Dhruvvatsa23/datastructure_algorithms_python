#find an element in a rotated and sorted array

lst = list(map(int, input().split()))

def pivot_element():
    s = 0
    n = len(lst)
    e = n-1
    mid = s + (e - s)//2

    while s < e: 
        if lst[mid] > lst[0]:
            s = mid + 1 
        else:
            e = mid
        mid = s + (e - s)//2
    return s, n

def binary_search(start, end, element):
    while start <= end:
        mid = start + (end - start) // 2
        if lst[mid] == element:
            return mid
        elif lst[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def findPosition():
    pivot, n = pivot_element()
    k = int(input())
    
    # binary search on second line
    if k >= lst[pivot] and k <= lst[n-1]:
        return binary_search(pivot, n-1, k)

    # binary search on first line
    else:
        return binary_search(0, pivot-1, k)

index = findPosition()

if index == -1:
    print("element not found!!")
else:
    print("element found at index", index)
