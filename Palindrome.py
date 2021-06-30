#One way : 44ms & 14.2 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

#second way : 98ms & 14.4 MB
import math 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        rev = 0
        while x > 0:
            rev = (rev * 10) + (x % 10)
            x = x // 10
        return num == rev
