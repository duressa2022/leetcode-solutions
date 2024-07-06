func canFinish(numCourses int, prerequisites [][]int) bool {

    //create dependency graph and indegree array or slice
    graph:=make(map[int][]int)
    indegree:=make([]int,numCourses)

    //init both graph and indegree structures
    for _,edge:=range prerequisites{
        graph[edge[1]]=append(graph[edge[1]],edge[0])
        indegree[edge[0]]+=1
    }

    //create queue and init by using node with indegree[node]==0
    queue:=[]int{}
    for node:=0;node<numCourses;node++{
        if indegree[node]==0{
            queue=append(queue,node)
        }
    }

    //Use bsf to create the order by which course is given
    order:=[]int{}
    for len(queue)>0{
        cur:=queue[0]
        queue=queue[1:]
        order=append(order,cur)

        for _,neighbor:=range graph[cur]{
            indegree[neighbor]-=1
            if indegree[neighbor]==0{
                queue=append(queue,neighbor)
            }
        }
    }
    //return based on the length of order
    return len(order)==numCourses

    
}