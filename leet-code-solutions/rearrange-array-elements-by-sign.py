class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        list=[i for i in nums if i>0]+[i for i in nums if i<0]
        result=[]
        i=0
        j=len(nums)//2
        while i<len(list)//2 and j<len(list):
            result.append(list[i])
            result.append(list[j])
            i=i+1
            j=j+1
        return result

        