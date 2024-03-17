class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        left,mid,right=0,1,2
        length=len(mountain)
        result=[]
        while right<length:
            if mountain[left]<mountain[mid]>mountain[right]:
                result.append(mid)
            left=left+1
            mid=mid+1
            right=right+1
        return result
        
        