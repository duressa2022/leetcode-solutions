class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions=[(1,0),(0,1),(0,-1),(-1,0)]
        def inbound(row,col):
            return 0<=row<len(image) and 0<=col<len(image[0])
        visted=set()
        temp=image[sr][sc]
        def solver(row,col):
            if not inbound(row,col) or (row,col) in visted or image[row][col]!=temp:
                return 
            visted.add((row,col))
            image[row][col]=color

            for dx,dy in  directions:
                x=row+dx
                y=col+dy
                if (x,y) not in visted:
                    solver(x,y)
        solver(sr,sc)
        return image
            
        