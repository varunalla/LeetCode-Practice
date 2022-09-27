class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxCurrent = maxSoFar = nums[0]
        
        for i in nums[1:]:
            maxCurrent = max(i, maxCurrent + i)
            maxSoFar = max(maxSoFar, maxCurrent)
            
        return maxSoFar
            
