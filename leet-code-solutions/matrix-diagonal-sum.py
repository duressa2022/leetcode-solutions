class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length=len(mat)
        result=0
        for i in range(length):
            result+=mat[i][i]
        row=0
        for j in range(length-1,-1,-1):
            result+=mat[row][j]
            row+=1
        if length%2==1:
            result=result-mat[length//2][length//2]
        return result

        

        