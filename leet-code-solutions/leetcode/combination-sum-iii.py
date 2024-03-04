class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        def helperFunction(current,path,target):
            if len(path)==k:
                if target<0:
                    return 
                elif target==0:
                    result.append(path[:])
                return 
            for i in range(current,10):
                path.append(i)
                helperFunction(i+1,path,target-i)
                path.pop()
        helperFunction(1,[],n)  
        return result
        