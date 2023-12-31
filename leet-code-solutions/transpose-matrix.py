class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed=[[0]*len(matrix) for cols in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transposed[j][i]=matrix[i][j]
        return transposed