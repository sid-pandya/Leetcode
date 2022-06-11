#Time: O(√n)

import math
def IsPrime(n):
  if n < 2:
    return False
  if n < 4:
    return True
  for i in range(2,int(math.sqrt(n)+1)):
    if n % i == 0:
      return False
  return True
