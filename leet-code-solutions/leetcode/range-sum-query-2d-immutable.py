class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        currentRow=len(matrix)
        currentCol=len(matrix[0])
        self.prefixMatrix=[[0]*(currentCol+1) for i in range(currentRow+1)]
        rows=len(self.prefixMatrix)
        cols=len(self.prefixMatrix[0])
        for i in range(1,rows):
            for j in range(1,cols):
                self.prefixMatrix[i][j]=matrix[i-1][j-1]+self.prefixMatrix[i-1][j]+self.prefixMatrix[i][j-1]-self.prefixMatrix[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixMatrix[row2+1][col2+1]-self.prefixMatrix[row1][col2+1]-self.prefixMatrix[row2+1][col1]+self.prefixMatrix[row1][col1]

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)