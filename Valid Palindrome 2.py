**LeetCode 680 -Given a string s, return true if the s can be palindrome after deleting at most one character from it.**

#one way : 68ms , 14.5 MB
class Solution:
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1
        #if len(s)< 3:
         #   return True
        if s == s[::-1]:
            return True
        while(left < right):
            if(s[left] != s[right]):
                one = s[left:right]
                two = s[(left + 1):(right + 1)]
                if one == one[::-1] or two == two[::-1]:
                    return True
                else:
                    return False
            left += 1
            right -= 1
        
        
#second way : 168ms , 14.5 MB
class Solution:
    def validPalindrome(self, s: str) -> bool: 
        left = 0
        right = len(s) - 1
        while( left < right):
            if s[left] != s[right]:
                return helper(s,left,right-1) or helper(s,left+1,right)
            left += 1
            right -= 1
        return True
    def helper(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1       
        return True

# third way : 74ms , 14.6 MB
class Solution:
    def validPalindrome(self, s: str) -> bool:      
        rev = s[::-1]
        if s == rev:   
            return True

        for i in range(len(s)):
            if s[i] != rev[i]:
                if i != 0:  
                    return s[:i] + s[i+1:] == rev[:-i-1] + rev[-i:] or rev[:i] + rev[i+1:] == s[:-i-1] + s[-i:]
                else:   
                    return s[1:] == rev[:-1] or s[:-1] == rev[1:]
