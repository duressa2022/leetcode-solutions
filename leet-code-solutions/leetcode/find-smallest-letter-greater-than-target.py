class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left,right,best=0,len(letters)-1,0
        while left<=right:
            mid=(left+right)//2
            if target<letters[mid]:
                best=mid
                right=mid-1
            else:
                left=mid+1
        return letters[best]
        