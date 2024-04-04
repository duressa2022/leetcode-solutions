class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def solver(grid,row,col):
            if not inbound(row,col) or  grid[row][col]=="0":
                return 
            grid[row][col]="0"

            for dx,dy in directions:
                x=row+dx
                y=col+dy
                if inbound(x,y) and grid[x][y]=="1":
                    solver(grid,x,y)
        counter=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    solver(grid,i,j)
                    counter+=1
        return counter


        
        

        