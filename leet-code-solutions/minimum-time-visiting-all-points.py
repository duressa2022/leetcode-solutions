class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        i=0
        j=1
        time=0
        while j<len(points):
            x1,y1=points[i][0],points[i][1]
            x2,y2=points[j][0],points[j][1]
            current=max(abs(x2-x1),abs(y2-y1))
            time+=current
            i=i+1
            j=j+1
        return time
        