func longestIncreasingPath(matrix [][]int) int {
    memo:=map[Tuple]int{}
    ans:=0
    for row:=0;row<len(matrix);row++{
        for col:=0;col<len(matrix[0]);col++{
            ans=max(ans,dfs(row,col,matrix,memo))
        }
    }
    return ans

}
func dfs(row int ,col int,matrix [][]int ,memo map[Tuple]int)int{
    if value,exist:=memo[Tuple{x:row,y:col}];exist{
        return value
    }
    if row>=len(matrix) || col>=len(matrix[0]){
        return 0
    }
    Dir:=[][]int{{1,0},{-1,0},{0,1},{0,-1}}
    ans:=1
    for _,dir:=range Dir{
        x:=row+dir[0]
        y:=col+dir[1]
        if x>=0 && y>=0 && x<len(matrix)&&y<len(matrix[0]) && matrix[row][col]<matrix[x][y]{
            ans=max(ans,1+dfs(x,y,matrix,memo))
        }
    }
    memo[(Tuple{x:row,y:col})]=ans
    return ans

}
type Tuple struct{
    x int
    y int
}
func max(x int,y int)int{
    if x>y{
        return x
    }
    return y
}