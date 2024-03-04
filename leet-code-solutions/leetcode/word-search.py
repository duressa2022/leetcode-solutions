class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLength=len(board)
        colLength=len(board[0])
        path=set()
        def helperFunction(row,col,index):
            if index==len(word):
                return True
            if row<0 or col<0:
                return False
            if row>=rowLength or col>=colLength:
                return False
            if (row,col) in path:
                return False
            if word[index]!=board[row][col]:
                return False
            path.add((row,col))
            result1=helperFunction(row+1,col,index+1)
            result2=helperFunction(row-1,col,index+1)
            result3=helperFunction(row,col+1,index+1)
            result4=helperFunction(row,col-1,index+1)
            path.remove((row,col))
            return result1 or result2 or result3 or result4
        for i in range(rowLength):
            for j in range(colLength):
                if helperFunction(i,j,0):
                    return True
        return False
        