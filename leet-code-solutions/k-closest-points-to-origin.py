class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result=[]
        for point in points:
            x,y=point
            distance=x**2+y**2
            result.append((distance,[x,y]))
        result.sort()
        answer=[]
        for i in range(k):
            answer.append(result[i][1])
        return answer
