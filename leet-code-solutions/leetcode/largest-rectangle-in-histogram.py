class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights=heights+[-1]
        length=len(heights)
        stack=[-1]
        span_array=[0]*length
        for i,value in enumerate(heights):
            while stack and stack[-1]!=-1 and heights[stack[-1]]>value:
                _index=stack.pop()
                left=_index-stack[-1]
                right=i-_index-1
                span_array[_index]=left+right
            stack.append(i)
        maxValue=-float("inf")
        for i in range(length):
            maxValue=max(maxValue,heights[i]*span_array[i])
        return maxValue


                
        