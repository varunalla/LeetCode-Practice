class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}
        
        for i in range(len(nums)):
            partnerNumber = target - nums[i]
            
            if partnerNumber in hashMap:
                return [i, hashMap[partnerNumber]]
            else:
                hashMap[nums[i]] = i
                
