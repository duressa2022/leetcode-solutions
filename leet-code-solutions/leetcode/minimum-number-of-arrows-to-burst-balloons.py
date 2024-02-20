class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        result=1
        current=points[0][1]
        for i in range(1,len(points)):
            if current<points[i][0]:
                result+=1
                current=points[i][1]
        return result

        