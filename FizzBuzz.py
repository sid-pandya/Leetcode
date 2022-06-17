#LeetCode 412 : Fizz Buzz
Given an integer n, return a string array answer (1-indexed) where:
  answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
  answer[i] == "Fizz" if i is divisible by 3.
  answer[i] == "Buzz" if i is divisible by 5.
  answer[i] == i (as a string) if none of the above conditions are true.

 # 60 ms , 15 MB
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        
        for i in range(1,n + 1):
            div_3 = (i % 3 == 0)
            div_5 = (i % 5 == 0)
            
            if div_3 and div_5:
                ans.append("FizzBuzz")
            elif div_3:
                ans.append("Fizz")
            elif div_5:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans

  
```
def fizzbuzz(num):
    for i in num:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
```
