# find sqaure root of an element (rounding up to closest integer) using binary search

class solution:
    # n = int(input())  
    
    def binary_search_1(self, n):
      start = 0
      end = n
      mid = start + (end - start)//2

      while start <= end:
        square = mid * mid
        if square == n:
          return mid
        if square < n:
          ans = mid
          start = mid + 1
        else: 
          end = mid -1
        mid = start + (end - start)//2
      return ans

    def find_square_root(self, x):
      return self.binary_search_1(x)
s = solution()
s.find_square_root(64)   #any number you want to get sqaure root of
