class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        wStart = 0
        minLen = sys.maxsize
        wSum = 0
        
        size = len(nums)
        
        for wEnd in range(size):
            wSum += nums[wEnd]
            
            while(wSum >= target):
                minLen = min(minLen, wEnd - wStart + 1)
                wSum -= nums[wStart]
                wStart += 1
        
        if minLen == sys.maxsize:
            return 0
        return minLen
