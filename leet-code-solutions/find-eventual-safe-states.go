func eventualSafeNodes(graph [][]int) []int {
    order:=[]int{}
    color:=make(map[int]int)
    for node:=0;node<len(graph);node++{
        if color[node]==2{
            continue
        }
        dfs(node,graph,color,&order)
    }
    sort.Ints(order)
    return order
}
func dfs(node int ,graph [][]int,color map[int]int,order *[]int)bool{

    if color[node]==1{
        return false
    }
    color[node]=1
    for _,neighbor:=range graph[node]{
        if color[neighbor]==2{
            continue
        }
        if !dfs(neighbor,graph,color,order){
            return false
        }
    }
    *order=append(*order,node)
    color[node]=2
    return true
}