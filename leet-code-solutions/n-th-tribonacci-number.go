func tribonacci(n int) int {
    return solver(n,map[int]int{})
    
}
func solver(n int,memo map[int]int)int{
    if value,ok:=memo[n];ok{
        return value
    }
    if n==0{
        return 0
    }
    if n==1{
        return 1
    }
    if n==2{
        return 1
    }
    memo[n]=solver(n-1,memo)+solver(n-2,memo)+solver(n-3,memo)
    return memo[n]
}