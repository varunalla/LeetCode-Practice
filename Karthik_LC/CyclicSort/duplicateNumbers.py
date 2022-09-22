class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        size = len(nums)
        i = 0
        duplicates = []
        
        while i < size:
            j = nums[i] - 1
            
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
            
        for i in range(size):
            if nums[i] != i + 1:
                duplicates.append(nums[i])
        
        return duplicates
        
