#One way : 44ms & 14.2 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

#Second Way : 79ms & 14.4 MB
# Two pointer method
class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = 0
        l = len((s))-1
        s = s.lower()
        while f < l:
            if not s[f].isalnum():
                f += 1
            elif not s[l].isalnum():
                l -= 1
            else:
                if s[f] != s[l]:
                    return False
                else:
                    f += 1
                    l -= 1
        return True
    
    
#Third way : 98ms & 14.4 MB
import math 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        rev = 0
        while x > 0:
            rev = (rev * 10) + (x % 10)
            x = x // 10
        return num == rev
