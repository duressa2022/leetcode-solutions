class Solution:
    def mySqrt(self, x: int) -> int:
        left,right,best=0,x,0
        while left<=right:
            mid=(left+right)//2
            if mid**2>x:
                right=mid-1
            else:
                left=mid+1
                best=mid
        return best
        
                
            


        