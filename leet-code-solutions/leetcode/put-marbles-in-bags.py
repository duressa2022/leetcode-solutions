class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        sortedList=[]
        for i in range(len(weights)-1):
            sortedList.append(weights[i]+weights[i+1])
        sortedList.sort()
        minValue=0
        maxValue=0
        for i in range(k-1):
            minValue+=sortedList[i]
        for i in range(len(sortedList)-1,len(sortedList)-k,-1):
            maxValue+=sortedList[i]
            print(i)
        return maxValue-minValue
        


        