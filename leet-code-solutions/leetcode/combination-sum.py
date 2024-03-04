class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def helperFunction(candidates,right,target,path):
            if target<0:
                return 
            elif target==0:
                result.append(path[:])
                return 
            for i in range(right,len(candidates)):
                path.append(candidates[i])
                helperFunction(candidates,i,target-candidates[i],path)
                path.pop()

        helperFunction(candidates,0,target,[])
        return result
        