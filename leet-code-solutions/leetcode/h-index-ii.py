class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left,right,length,best=0,len(citations)-1,len(citations),0
        while left<=right:
            mid=(left+right)//2
            if length-mid<=citations[mid]:
                best=length-mid
                right=mid-1
            else:
                left=mid+1
        return best

        