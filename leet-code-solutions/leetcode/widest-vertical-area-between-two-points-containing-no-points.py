class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xcordinate=[]
        for x,y in points:
            xcordinate.append(x)
        xcordinate.sort()
        left,right=0,1
        maxWidth=0
        while right<len(points):
            maxWidth=max(maxWidth,xcordinate[right]-xcordinate[left])
            left=left+1
            right=right+1
        return maxWidth
        