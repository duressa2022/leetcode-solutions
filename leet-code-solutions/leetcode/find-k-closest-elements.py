class Solution:

    def findClosestElements(self,arr: List[int], k: int, x: int) -> List[int]:
        left,right=0,len(arr)-1
        while left<=right:
            mid=(left+right)//1
            if arr[mid]==x:
                index=mid
                break
            elif arr[mid]>x:
                right=mid-1
            else:
                left=mid+1
        else:
            index=left
        left,right=index-1,index
        while k>0:
            if left>=0 and right<len(arr):
                if abs(x-arr[left])<=abs(x-arr[right]):
                    left=left-1
                else:
                    right=right+1
            elif left>=0:
                left-=1
            else:
                right+=1
            k=k-1
        return arr[left+1:right]


 
        