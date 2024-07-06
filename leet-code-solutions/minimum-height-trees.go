func findMinHeightTrees(n int, edges [][]int) []int {

    //create graph and degree...for information storage
    graph:=make(map[int][]int)
    degree:=make([]int,n)

    //populate both storage unit...graph and degree
    for _,edge:= range edges{
        graph[edge[0]]=append(graph[edge[0]],edge[1])
        graph[edge[1]]=append(graph[edge[1]],edge[0])
        degree[edge[0]]+=1
        degree[edge[1]]+=1
    }

    //create queue and init with degree[node]==1
    queue:=[]int{}
    for node:=0;node<n;node++{
        if degree[node]==1{
            queue=append(queue,node)
        }
    }

    //perform bfs......until two or less nodes left inside the queue
    for len(queue)>0{
        length:=len(queue)
        if n<=2{
            return queue
        }
        for length>0{
            cur:=queue[0]
            queue=queue[1:]
            length--
            n--
            for _,neighbor:=range graph[cur]{
                degree[neighbor]-=1
                if degree[neighbor]==1{
                    queue=append(queue,neighbor)
                }
            }
        }

    }
    return []int{0}
    
}