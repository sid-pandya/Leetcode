**LeetCose 392**

#36ms , 13.8 MB
def isSubsequence(self, s: str, t: str) -> bool:
    #check potential subsequence is smaller than main String
    if len(s) > len(t):
        return False
    i=0
    #loop for each char n main string
    for item in t:
        if len(s)==i:
            return True
        #compare the subsequence char with main string char
        if s[i] == item:
            i+=1
    if i==len(s):
        return True
    return False
    
    
#89ms, !4.1 MB
def isSubsequence(self, s: str, t: str) -> bool:
    if len(s) > len(t):
        return False
    if len(s) < 1:
        return True
    i, j = 0, 0
    while i < len(s) and j <len(t):
        if s[i] == t[j]:
            i+=1
        j += 1
    return i == len(s)
