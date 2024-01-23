class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tempCounter=[0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            tempCounter[i]=tempCounter[i-1]+nums[i-1]
        left,right=0,1
        length=None
        print(tempCounter)
        while right<len(nums)+1 and left!=right:
            current=tempCounter[right]-tempCounter[left]
            print(current)
            if current<target:
                right=right+1
            else:
                if length is None:
                    length=right-left
                else:
                    length=min(length,right-left)
                left=left+1
        if length is None:
            return 0
        elif length==0:
            return 1
        else:
            return length
        


        