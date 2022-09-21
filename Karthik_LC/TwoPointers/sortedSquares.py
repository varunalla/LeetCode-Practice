class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        
        squares = [0 for i in range(size)]
        
        left = 0
        right = size - 1
        
        indexToInsert = size - 1
        
        while(left <= right):
            leftSq = nums[left] * nums[left]
            rightSq = nums[right] * nums[right]
            
            if leftSq > rightSq:
                squares[indexToInsert] = leftSq
                left += 1
            else:
                squares[indexToInsert] = rightSq
                right -= 1
            
            indexToInsert -= 1
            
        
        return squares
                
