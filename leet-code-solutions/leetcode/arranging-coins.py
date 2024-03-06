class Solution:
    def arrangeCoins(self, n: int) -> int:
        left,right,best=1,n,-1
        while left<=right:
            mid=(left+right)//2
            if mid*(mid+1)/2<=n:
                best=mid
                left=mid+1
            else:
                right=mid-1
        return best
        