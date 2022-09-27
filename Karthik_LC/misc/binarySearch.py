class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        start = 0
        end = n - 1
        
        while start <= end:
            mid = (start + end)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                start = mid + 1
            
            if nums[mid] > target:
                end = mid - 1
            
        return -1
                
        
