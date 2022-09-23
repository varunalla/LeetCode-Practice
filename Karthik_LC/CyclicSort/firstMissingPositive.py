class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        size = len(nums)
        i = 0
        
        while i < size:
            j = nums[i] - 1
            if nums[i] > 0 and nums[i] <= size and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i in range(size):
            if nums[i] != i + 1:
                return i + 1
        
        return size + 1
