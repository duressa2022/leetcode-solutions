class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result=[]
        for num in nums:
            result.extend(self.getDigit(num))
        return result
    def getDigit(self,num):
        result=[]
        while num>0:
            result.append(num%10)
            num//=10
        return result[::-1]
        