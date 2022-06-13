#LettCode-50 : Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



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
