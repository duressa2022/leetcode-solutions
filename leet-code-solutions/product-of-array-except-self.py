class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        left=[1]*(len(nums)+1)
        right=[1]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            left[i]=left[i-1]*nums[i-1]
        nums=nums[::-1]
        print(left)
        for i in range(1,len(nums)+1):
            right[i]=right[i-1]*nums[i-1]
        right=right[::-1]
        print(right)
        for i in range(1,len(nums)+1):
            current=left[i-1]*right[i]
            result.append(current)
        return result

        