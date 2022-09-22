class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        disappearedNumbers = []
        
        size = len(nums)
        i = 0
        
        while i < size:
            j = nums[i] - 1
            
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
            
        for i in range(size):
            if nums[i] != i + 1:
                disappearedNumbers.append(i + 1)
            
        return disappearedNumbers
