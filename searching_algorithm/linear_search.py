#Linear Search

element = int(input())
lst = [2, 5, 7, 8, 10 , 78, 42, 12, 66]
#lst = list(map(int, input().split()))           if you want user to enter the elements in the list
for i in range(len(lst)):                        #traversing through the list using a for loop same can be done using a 
                                                 #while loop also you will have to initialize value of "i" equals to 0
                                                 #and for the condition i<len(list) the loop will continue to run...
  if lst[i] == element:
    print("Element found at index: ", i)
    break  
else:
  print("Element not found!!")
