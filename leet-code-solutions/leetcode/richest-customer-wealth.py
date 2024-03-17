class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rowLength=len(accounts)
        colLength=len(accounts[0])
        result=0
        for i in range(rowLength):
            temp=0
            for j in range(colLength):
                temp+=accounts[i][j]
            result=max(result,temp)
        return result
        