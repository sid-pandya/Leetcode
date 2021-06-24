class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            rev = int(str(x)[::-1])
        elif x < 0:
            rev = -1 * int(str(x*-1)[::-1])
        else:
            return 0
        mina = -2**31  
        maxa = 2**31 - 1  
        if rev not in range(mina, maxa):  
            return 0  
        else:
            return rev
    
