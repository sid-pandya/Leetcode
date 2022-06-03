#First Way : 38 ms , 13.8 MB
#Dictionary and Stack(list) method
class Solution:
    
    def isValid(self, s: str) -> bool:
        match_dict = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }        
        stack = []
        for cha in s:
            if cha in match_dict:
                stack.append(cha)
            elif len(stack) == 0 or match_dict[stack.pop()] != cha:
                return False
        return len(stack) == 0
      
#Second Way : 78ms , 13.9 MB
#By .replace()
class Solution:
 
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()","").replace("{}","").replace("[]","")
        if s == "":
            return True
