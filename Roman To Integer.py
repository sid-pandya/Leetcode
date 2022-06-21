#LeetCode - 13 : Given a roman numeral, convert it to an integer.

#using .replace()
Time complexity – O(N)
Auxiliary Space – O(1)

```
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000
               }
        res = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            res += dict[char]
        return res
    
```
