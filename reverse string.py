#leetcode - 344

def reverseString(self, s: List[str]) -> None:
  """
  Do not return anything, modify s in-place instead.
  """
  #two pointer method : 199ms , 18 MB
  l ,r = 0, len(s)-1
  while l < r:
      s[l],s[r] = s[r],s[l]
      l,r = l+1, r-1
     
  #Pythonic solution : 300ms , 18.8 MB
  s[:] = s[::-1]
