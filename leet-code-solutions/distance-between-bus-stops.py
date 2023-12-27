class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, end: int) -> int:
        totaldistance=sum(distance)
        clockWiseDistance=0
        if start>end:start,end=end,start
        while start<end:
            clockWiseDistance+=distance[start]
            start+=1
        return min(clockWiseDistance,totaldistance-clockWiseDistance)
        
        