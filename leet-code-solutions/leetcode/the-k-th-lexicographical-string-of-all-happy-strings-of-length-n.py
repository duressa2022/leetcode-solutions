class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        candidates=["a","b","c"]
        result=[]
        def helperFunction(n,k,path):
            if n==len(path[:]):
                result.append(path[:])
                return
            for char in candidates:
                if len(result)==k:
                    return 
                if len(path[:])<1:
                    path.append(char)
                else:
                    if path[-1]==char:
                        continue
                    else:
                        path.append(char)
                helperFunction(n,k,path)
                path.pop()
        helperFunction(n,k,[])
        if len(result)<k:return ""
        return "".join(result[-1])

        