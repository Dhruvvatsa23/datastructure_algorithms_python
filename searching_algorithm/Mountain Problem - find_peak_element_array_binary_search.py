# find the peak index in a mountain array

lst = list(map(int, input().split()))

start = 0
end = len(lst)
mid = (start + (end - start)//2)

def find_peak(start, end, mid):
    for i in range(len(lst)):
      
      if lst[mid] < lst[mid+1]:
        start = mid + 1
      
      else: 
        end = mid                       # this condition is different than the one used in regular binary search because "mid" can be at the peak element so
                                        # so if we use the condition i.e (end = mid - 1) we will be getting wrong answer as the mid will shift to the left-side
                                        # of the peak element
      
      mid = (start + (end - start)//2)
    
    print("Peak element is at index: ", start)
    
    find_peak(start, end, mid
