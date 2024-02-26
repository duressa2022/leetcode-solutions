class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        else:
            prev=self.getRow(rowIndex-1)
            result=[1]
            for i in range(1,rowIndex):
                result.append(prev[i-1]+prev[i])
            result+=[1]
            return result
    

        