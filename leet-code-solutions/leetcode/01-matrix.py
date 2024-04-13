class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        DIR=[(1,0),(-1,0),(0,1),(0,-1)]
        length_row=len(mat)
        length_col=len(mat[0])
        visted=set()
        def inbound(row,col):
            return 0<=row<length_row and 0<=col<length_col
        result=[[0]*length_col for _ in range(length_row)]
        def solver():
            queue=deque()
            visted=set()
            for i in range(length_row):
                for j in range(length_col):
                    if mat[i][j]==0:
                        queue.append((i,j,0))
                        visted.add((i,j))
            while queue:
                curx,cury,move=queue.popleft()
                result[curx][cury]=move

                for dx,dy in DIR:
                    x=curx+dx
                    y=cury+dy
                    if inbound(x,y) and (x,y) not in visted :
                        queue.append((x,y,move+1))
                        visted.add((x,y))
        solver()
        return result
        
                  
        
                
                    






        