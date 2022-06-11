#Time:O(√n), Space: O(1)

import Math

#helper method
def IsPrime(n):
  if n < 2:
    return False
  if n < 4:
    return True
  for i in range(2,int(math.sqrt(n)+1)):
    if n % i == 0:
      return False
  return True

def NextPrime(n):
  if n < 2:
    return 2
  n += 1
  while True:
    if IsPrime(n):
      return n
    n += 1
