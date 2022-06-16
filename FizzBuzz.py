#LeetCode 412 : Fizz Buzz
Given an integer n, return a string array answer (1-indexed) where:
  answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
  answer[i] == "Fizz" if i is divisible by 3.
  answer[i] == "Buzz" if i is divisible by 5.
  answer[i] == i (as a string) if none of the above conditions are true.
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
