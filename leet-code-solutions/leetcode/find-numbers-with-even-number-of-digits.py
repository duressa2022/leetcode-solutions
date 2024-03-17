class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        length=len(nums)
        counter=0
        for i in range(length):
            if self.digitCounter(nums[i])%2==0:
                counter+=1
        return counter
    def digitCounter(self,num):
        counter=0
        while num>0:
            num=num//10
            counter+=1
        return counter
        