class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left,right,best=1,max(nums),1
        while left<=right:
            mid=(left+right)//2
            
            calculated=0
            for num in nums:
                calculated+=ceil(num/mid)
            
            if calculated<=threshold:
                best=mid
                right=mid-1
            else:
                left=mid+1
        return best

        