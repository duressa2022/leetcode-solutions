class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        length=len(board)
        def solverFunction(board):
            for row in range(length):
                for col in range(length):
                    if board[row][col]==".":
                        for move in range(1,10):
                            if validFunction(board,row,col,str(move)):
                                board[row][col]=str(move)
                                if solverFunction(board):
                                    return True
                                board[row][col]="."
                        return False
            return True
        def validFunction(board,row,col,move):
            for i in range(9):
                if board[row][i]==move:
                    return False 
                if board[i][col]==move:
                    return False
            row=3*(row//3)
            col=3*(col//3)
            for i in range(row,row+3):
                for j in range(col,col+3):
                    if board[i][j]==move:
                        return False
            return True
        solverFunction(board)


        