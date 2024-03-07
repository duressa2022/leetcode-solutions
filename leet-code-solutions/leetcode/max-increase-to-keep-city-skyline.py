class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxRows=[]
        maxCols=[]
        for row in grid:
            maxRows.append(max(row))
        for i in range(len(grid)):
            maxValue=-1
            for j in range(len(grid)):
                maxValue=max(maxValue,grid[j][i])
            maxCols.append(maxValue)
        minCounter=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                minCounter+=min(maxRows[i],maxCols[j])-grid[i][j]
        return minCounter

        
        