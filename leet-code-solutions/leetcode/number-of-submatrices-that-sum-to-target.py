class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        lengthRow=len(matrix)
        lengthCol=len(matrix[0])
        prefixMatrix=[[0]*(lengthCol+1) for row in range(lengthRow+1)]
        for i in range(1,lengthRow+1):
            for j in range(1,lengthCol+1):
                prefixMatrix[i][j]=prefixMatrix[i][j-1]+prefixMatrix[i-1][j]+matrix[i-1][j-1]-prefixMatrix[i-1][j-1]
        result=0
        for i in range(lengthRow):
            for j in range(i,lengthRow):
                    prefixCounter=defaultdict(int)
                    prefixCounter[0]=1
                    for col in range(lengthCol):
                        current=prefixMatrix[j+1][col+1]-prefixMatrix[i][col+1]
                        if current-target in prefixCounter:
                            result+=prefixCounter[current-target]
                        prefixCounter[current]+=1
        return result




        