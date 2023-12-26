class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        array=sorted(nums,reverse=True)
        for i in range(len(array)-2):
            if array[i]<array[i+1]+array[i+2]:
                return array[i]+array[i+1]+array[i+2]
        return 0
        
        