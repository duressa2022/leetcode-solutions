class Solution:
    def totalNQueens(self, n: int) -> int:
        column=set()
        leftDiag=set()
        rightDiag=set()
        board=[["."]*n for i in range(n)]
        counter=0
        def helperFunction(row):
            nonlocal counter
            if row>=n:
                counter+=1
                return 
            for col in range(n):
                if col in column or (col-row) in rightDiag or (col+row) in leftDiag:
                    continue
                column.add(col)
                rightDiag.add(col-row)
                leftDiag.add(col+row)
                board[row][col]="Q"
                helperFunction(row+1)

                column.remove(col)
                rightDiag.remove(col-row)
                leftDiag.remove(col+row)
                board[row][col]="."
        helperFunction(0)
        return counter


                
        