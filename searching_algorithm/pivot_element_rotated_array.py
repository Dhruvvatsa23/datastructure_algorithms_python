#finding pivot point in a rotated array

lst = list(map(int, input().split()))

start = 0
end = (len(lst)-1)
mid = (start + (end - start)//2)

while start < end:
  
  if lst[mid]>=lst[0]:
    start = mid +1
  
  else:
    end = mid
  
  mid = (start + (end - start)//2)

print("The pivot element is at index: ", start)
