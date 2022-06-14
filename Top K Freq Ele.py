# LeetCode -347 : Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Time Complexity: O(n log n) : for loop O(n) + .sort() O(log n)
# Space Complexity: O(1)

#183 ms , 18.7 MB
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
       
        for element in nums:
            if element not  in freq:
                freq[element] = 1
            else:
                freq[element] += 1
        freq = (sorted(freq.items(), key=lambda x: x[1], reverse=True))
        
        ret = []
        for i in range(k):
            ret.append(freq[i][0])
            
        return ret
    
          

#236 ms , 18.8 MB
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
       
        for element in nums:
            if element not  in freq:
                freq[element] = 1
            else:
                freq[element] += 1
        freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        result = list(freq.keys())[:k]
        return result
      
