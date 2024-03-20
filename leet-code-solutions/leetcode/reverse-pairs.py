class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def solver(nums):
            if len(nums)<=1:
                return (0,nums)
            mid=len(nums)//2
            leftCounter,left=solver(nums[:mid])
            rightCounter,right=solver(nums[mid:])
            mergedCounter,merged=self.mergeCounter(left,right)
            return (leftCounter+rightCounter+mergedCounter,merged)
        (result,result_)=solver(nums)
        return result
    def mergeCounter(self,left,right):
        counter=0
        result=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i]>2*right[j]:
                counter+=len(left[i:])
                j=j+1
            else:
                i=i+1
        i=j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i=i+1
            else:
                result.append(right[j])
                j=j+1
        while i<len(left):
            result.append(left[i])
            i=i+1
        while j<len(right):
            result.append(right[j])
            j=j+1
        return (counter,result)

        
        