class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        allTriplets = []
        
        nums.sort()
        size = len(nums)
        
        for i in range(size):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            self.threeSumHelper(nums, -nums[i], i + 1, allTriplets)
        
        return allTriplets
    
    
    def threeSumHelper(self, arr, targetSum, left, allTriplets):
        size = len(arr)
        right = size - 1
        
        while left < right:
            
            curSum = arr[left] + arr[right]
            
            if curSum == targetSum:
                allTriplets.append([-targetSum, arr[left], arr[right]])
                left += 1
                right -= 1
                
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
                
            elif curSum < targetSum:
                left += 1
            else:
                right -= 1
                
        
