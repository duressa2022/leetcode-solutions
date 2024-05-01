class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        numberOfEdges={}
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for node in range(n):
            numberOfEdges[node]=len(graph[node])
        queue=deque()
        for node in range(n):
            if numberOfEdges[node]==1:
                queue.append(node)
        while queue:
            if n<=2:
                return list(queue)
            length=len(queue)
            for _ in range(length):
                cur=queue.popleft()
                n-=1
                for neighbor in graph[cur]:
                    numberOfEdges[neighbor]-=1
                    if numberOfEdges[neighbor]==1:
                        queue.append(neighbor)
        return [0]

        