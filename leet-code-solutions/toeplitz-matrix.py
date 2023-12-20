class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        length=len(matrix)-1
        for u in range(length):
	        for v in range(len(matrix[0]) - 1):
		        if matrix[u][v] != matrix[u + 1][v + 1]:
			        return False
        return True
        

                

        