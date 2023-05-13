# bubble sort algorithm

def bubble_sort(lst, n):
  for i in range(n):
    for j in range(0, n-i-1):
      if lst[j] > lst[j+1]:
         lst[j], lst[j+1] = lst[j+1], lst[j]
  return lst    

lst = [10, 1, 7, 6, 14, 9]
n = len(lst)
bubble_sort(lst, n)
