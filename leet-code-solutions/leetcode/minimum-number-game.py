class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        length=len(nums)
        result=[]
        while length>0:
            alice=0
            for i in range(length):
                if nums[alice]>nums[i]:
                    alice=i
            alice=nums.pop(alice)
            length=length-1
            bob=0
            for i in range(length):
                if nums[bob]>nums[i]:
                    bob=i
            bob=nums.pop(bob)
            length=length-1
            result.append(bob)
            result.append(alice)
        return result
        