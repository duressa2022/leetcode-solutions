class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater=-float("inf")
        left=0
        right=len(height)-1
        while left<right:
            current=min(height[left],height[right])*(right-left)
            if current>maxWater:
                maxWater=current
            if height[left]>height[right]:
                right=right-1
            else:
                left=left+1
        return maxWater

        