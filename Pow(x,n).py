#LettCode-50 : Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

#Time Complexity: O(logN) , Space Complexity: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        result = self.myPow(x, n // 2)
        return result * result * (x if n % 2 else 1)
    
#Second approach
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return self.myPow(1/x,-n)
        temp = self.myPow(x,n//2)
        if n % 2 == 0:
            return temp * temp
        if n % 2 == 1:
            return x * temp * temp
