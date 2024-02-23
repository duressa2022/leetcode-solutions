class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashSet={key:index for index,key in enumerate(nums1)}
        ans=[-1]*len(nums1)
        stack=[]
        for index,num in enumerate(nums2):
            while stack and stack[-1]<num:
                temp=stack.pop()
                if temp in hashSet:
                    ans[hashSet[temp]]= num
            stack.append(num)
        return ans
            
            
        