class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns=set()
        leftDiag=set()
        rightDiag=set()
        board=[["."]*n for i in range(n)]
        result=[]
        def helperFunction(row):
            if row>=n:
                temp=["".join(value) for value in board]
                result.append(temp[:])
                return 
            for col in range(n):
                if col in columns or (col-row) in rightDiag or (col+row) in leftDiag:
                    continue
                columns.add(col)
                leftDiag.add(col+row)
                rightDiag.add(col-row)
                board[row][col]="Q"
                helperFunction(row+1)
                columns.remove(col)
                leftDiag.remove(col+row)
                rightDiag.remove(col-row)
                board[row][col]="."
        helperFunction(0)
        return result



                
                

        return result
        