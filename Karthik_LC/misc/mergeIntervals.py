class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) < 2:
            return intervals
        
        intervals = sorted(intervals)
        mergedIntervals = []
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            
            if(interval[0]) <= end:
                end = max(interval[1], end)
            else:
                mergedIntervals.append([start, end]) 
                start = interval[0]
                end = interval[1]
                
        
        mergedIntervals.append([start,end])
        
        return mergedIntervals
                
