# Binary Search
# Complexity : O(log n)

lst = [2, 3, 45, 25, 85, 7, 4]
lst.sort()                    # binary search assumes that the array which is provided for searching is a "sorted" array
lst
start = 0
end = len(lst)-1
mid = (start + end)//2        #floor division
element = int(input())
while start<=end:
    if element == lst[mid]:
        print("Element found: ", mid)
        break
    # go to right part of the array
    if element > lst[mid]:
        start = mid + 1
    # go to left part of the array
    else:
        end = mid - 1

    # update mid value
    mid = (start+end)//2
else
  print("Element not found!!")
