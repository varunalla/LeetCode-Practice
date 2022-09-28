class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x : x[0])
        
        rooms = [intervals[0][1]]
        heapq.heapify(rooms)
        
        for interval in intervals[1:]:
            if interval[0] >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])
        
        return len(rooms)
