class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxSize=0
        for [num,from1,to1] in trips:
            maxSize=max(maxSize,to1)
        prefix=[0]*(maxSize)
        for [num,from1,to1] in trips:
            if from1+1<maxSize:
                prefix[from1+1]+=num
            if to1+1<maxSize:
                prefix[to1+1]-=num
        running=0
        for i in range(maxSize):
            running+=prefix[i]
            if running>capacity:
                return False
            prefix[i]=running
        return False if trips[0][0]>capacity else True

        