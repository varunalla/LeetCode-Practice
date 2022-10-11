class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        totalSize = len(nums1) + len(nums2)
        
        half = totalSize // 2
        
        if len(B) < len(A):
            A, B = B, A
            
        left = 0
        right = len(A) - 1
        
        while True:
            aIndex = (left + right) // 2
            bIndex = half - aIndex - 2
            
            aLeft = A[aIndex] if aIndex >= 0 else float("-infinity")
            bLeft = B[bIndex] if bIndex >= 0 else float("-infinity")
            
            aRight = A[aIndex + 1] if (aIndex + 1) < len(A) else float("infinity")
            bRight = B[bIndex + 1] if (bIndex + 1) < len(B) else float("infinity")
            
            if aLeft <= bRight and bLeft <= aRight:
                if totalSize % 2:
                    return min(aRight, bRight)
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif bLeft > aRight:
                left = aIndex + 1
            else:
                right = aIndex - 1
                
