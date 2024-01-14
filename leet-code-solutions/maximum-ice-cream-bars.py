class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        counter=0
        left=0
        while left<len(costs):
            if costs[left]<coins:
                counter+=1
                coins-=costs[left]
                left=left+1
            else:
                if costs[left]==coins:
                    counter+=1
                break
        return counter
    
        