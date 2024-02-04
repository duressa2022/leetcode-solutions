class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        #define rows and cols of the grid
        rows,cols=len(grid),len(grid[0])
        #check wether the cols and roes of the grid are correct
        if rows<3 and cols<3:
            return
        #define max value for the finder
        maxFinder=-float("inf") 
        #loop through the matrix
        for i in range(rows-2):
            for j in range(cols-2):
                #calculate the sum
                current=(grid[i][j]+grid[i][j+1]+grid[i][j+2])+(grid[i+1][j+1]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2])
                #compare with previous sum
                maxFinder=max(maxFinder,current)
        #return max of the the sum
        return maxFinder
        