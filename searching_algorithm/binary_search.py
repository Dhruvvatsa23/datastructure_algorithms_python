# Binary Search

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
else:
  print("Element not found!!")
