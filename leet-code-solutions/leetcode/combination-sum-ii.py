class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        def helperFunction(candidates,path,right,target):
            if target<0:
                return 
            elif target==0 and sorted(path) not in result:
                result.append(sorted(path[:]))
            for i in range(right,len(candidates)):
                if i>right and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                helperFunction(candidates,path,i+1,target-candidates[i])
                path.pop()
        helperFunction(candidates,[],0,target)
        return result

        