class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        i = 0
        size = len(nums)
        
        while i < size:
            j = nums[i]
            
            if nums[i] < size and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for k in range(size):
            if nums[k] != k:
                return k
        
        return size
