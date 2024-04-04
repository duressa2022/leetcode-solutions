class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def inbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        Directions=[(1,0),(-1,0),(0,1),(0,-1)]
        visted=set()
        def solver(grid,row,col):
            nonlocal counter
            if not inbound(row,col) or grid[row][col]==0 or (row,col) in visted:
                return 
            visted.add((row,col))
            counter+=1
            for dx,dy in Directions:
                x=row+dx
                y=col+dy
                solver(grid,x,y)
        maxValue=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visted and grid[i][j]==1:
                    counter=0
                    solver(grid,i,j)
                    maxValue=max(maxValue,counter)
        return maxValue
            



        