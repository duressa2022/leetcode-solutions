class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #loop through the board
        for i in range(9):
            for j in range(9):
                #get result for row
                rows_result=self.checkForRows(board,i)
                #get result for cols
                cols_result=self.checkForCols(board,j)
                #get result for boxes
                boxs_result=self.checkforBoxs(board,i-i%3,j-j%3)
                #evalute the result
                result=rows_result and cols_result and boxs_result
                #return False if result==False
                if result==False:
                    return False
        #return True for unique elemnets
        return True
    #function to check uniqueness of each rows
    def checkForRows(self,board,row):
        #create set to hold the elements of the board
        hash_set=set()
        #loop through given board
        for i in range(9):
            #check if the value is the set
            if board[row][i] in hash_set:
                return False
            #check if the value is not equal with dot
            if board[row][i]!=".":
                #put value into the set
                hash_set.add(board[row][i])
        #return True for unique rows
        return True
    #function to check for uniqueness of each cols
    def checkForCols(self,board,cols):
        #create set to hold unique values of the board
        hash_set=set()
        #loop through given board
        for i in range(9):
            #check if the value in the set
            if board[i][cols] in hash_set:
                return False
            #check if value not equal to dot
            if board[i][cols]!=".":
                #put value into set
                hash_set.add(board[i][cols])
        #return True for unique value of cols
        return True
    #function to check for the box
    def checkforBoxs(self,board,rows,cols):
        #create hash_set to hold unique values
        hash_set=set()
        #loop through the given board
        for i in range(3):
            for j in range(3):
                #check if value is hash_set
                if board[rows+i][cols+j] in hash_set:
                    return False
                #check if value is not equal with dot
                if board[rows+i][cols+j]!=".":
                    #put value into hash_set
                    hash_set.add(board[rows+i][cols+j])
        #return True for unique elements in the box
        return True


        