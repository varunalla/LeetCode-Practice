class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            hash[num] = 1 + hash.get(num, 0)
        
        for key,value in hash.items():
            freq[value].append(key)
            
        result = []
        
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                result.append(j)
            
            if len(result) == k:
                return result
            
