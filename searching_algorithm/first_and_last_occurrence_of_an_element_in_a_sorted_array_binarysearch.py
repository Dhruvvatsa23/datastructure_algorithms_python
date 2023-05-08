#first and last occurrence of an element in a sorted array

  
element = int(input())
lst = list(map(int, input().split()))

start = 0
end = (len(lst)-1)
mid = (start + (end - start)//2)  #optimality

def first_occurrence(start, end, mid, element):

    for i in range(len(lst)):

      if lst[mid] == element:
        ans_first = mid                   #storing value in a variable as the list's mid == key_element
                                          #so there is a possibility that there are key_elements 
                                          #present before that index also
        
        end = mid-1               #updating the end to check futher occurrences
      
      if element > lst[mid]:
        start = mid+1
      
      else:
        end = mid - 1 
      mid = (start + (end-start)//2)

    print("first occurrence of element is at index: ", ans_first)

def last_occurrence(start, end, mid, element):
    for i in range(len(lst)):
      
      if lst[mid] == element:
        ans_last = mid
        start = start + 1
      
      if element>mid:
        start = mid + 1

      else:
        end = mid - 1
      
      mid = (start + (end - start)//2)
      
    print("last occurrence of element is at index: ", ans_last)
    
    #function called
    first_occurrence(start, end, mid, element)
    last_occurrence(start, end, mid, element)
    
    
