class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        minCost=0
        length=len(costs)
        for i in range(1,length+1):
            if i<=length//2:
                minCost+=costs[i-1][0]
            else:
                minCost+=costs[i-1][1]
        return minCost




        