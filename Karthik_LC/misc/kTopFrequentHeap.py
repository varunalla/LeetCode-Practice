class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash = {}
        
        for num in nums:
            hash[num] = 1 + hash.get(num, 0)
            
        heap = []
        
        for key,value in hash.items():
            heapq.heappush(heap, [value,key])
            
            if len(heap) > k:
                heapq.heappop(heap)
            
               
        result = []
        
        for i in heap:
            result.append(i[1])
        
        return result
