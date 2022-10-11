class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])
        
        result = 0
        count = 0
        
        s = 0
        e = 0
        
        while s < len(start):
            
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            
            result = max(result, count)
        
        return result
            
