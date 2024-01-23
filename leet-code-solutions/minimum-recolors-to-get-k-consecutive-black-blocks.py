class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        tempCounter=[0]*(len(blocks)+1)
        for i in range(1,len(blocks)+1):
            if blocks[i-1]=="W":
                tempCounter[i]=tempCounter[i-1]+1
            else:
                tempCounter[i]=tempCounter[i-1]
        left=0
        right=k
        minFinder=float("inf")
        while right<len(blocks)+1:
            current=tempCounter[right]-tempCounter[left]
            minFinder=min(current,minFinder)
            left=left+1
            right=right+1
        return minFinder
        
        