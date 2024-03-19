class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rowLength=len(grid)
        colLength=len(grid[0])
        counter=0
        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j]<0:
                    counter+=1
        return counter
        