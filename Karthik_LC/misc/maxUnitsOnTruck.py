class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x : -x[1])
        totalUnits = 0
        
        for box,units in boxTypes:
            if truckSize > box:
                truckSize -= box
                totalUnits += box * units
            else:
                totalUnits += truckSize * units
                return totalUnits
                
        return totalUnits
        
