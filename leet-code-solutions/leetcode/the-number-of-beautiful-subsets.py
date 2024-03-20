class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        length=len(nums)
        nums.sort()
        counter=0
        def helperFunction(path,right):
            nonlocal counter
            if len(path[:])>0:
                counter+=1
            for i in range(right,length):
                if len(path[:])<1:
                    path.append(nums[i])
                else:
                    flag=False
                    for num in path:
                        if abs(num-nums[i])==k:
                            flag=True
                    if flag:
                        continue
                    else:
                        path.append(nums[i])
                helperFunction(path,i+1)
                path.pop()
        helperFunction([],0)
        return counter
        