class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        index = 1
        size = len(nums)
        
        for i in range(1,size):
            
            if nums[i-1] != nums[i]:
                nums[index] = nums[i]
                index += 1
        
        return index
