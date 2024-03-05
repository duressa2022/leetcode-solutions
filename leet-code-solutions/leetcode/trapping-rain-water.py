class Solution:
    def trap(self, heights: List[int]) -> int:
        counter=0
        stack=[]
        for index,height in enumerate(heights):
            while stack and heights[stack[-1]]<=height:
                temp=stack.pop()
                if stack:
                    min_height=min(height,heights[stack[-1]])-heights[temp]
                    width=index-stack[-1]-1
                    counter+=min_height*width
            stack.append(index)
        return counter

        

