class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result=[]
        holder={}
        hold_start=[]
        for i in range(len(intervals)):
            holder[intervals[i][0]]=i  
            hold_start.append(intervals[i][0])  
        hold_start.sort()
        length=len(hold_start)
        for i in range(len(intervals)):
            finder=bisect_left(hold_start,intervals[i][1])
            if finder==length:
                result.append(-1)
            else:
                result.append(holder[hold_start[finder]])
        return result
