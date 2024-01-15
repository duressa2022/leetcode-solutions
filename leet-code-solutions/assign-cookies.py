class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        left,right=0,0
        counter=0
        g.sort()
        s.sort()
        while left<len(g) and right<len(s):
            if g[left]<=s[right]:
                left=left+1
                right=right+1
                counter+=1
            else:
                right=right+1
        return counter

        