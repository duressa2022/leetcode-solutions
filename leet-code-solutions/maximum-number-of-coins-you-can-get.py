class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        result=0
        left=0
        right=len(piles)-1
        nextMax=1
        while left<right:
            result+=piles[nextMax]
            left=nextMax+1
            nextMax=left+1
            right=right-1
        return result
        