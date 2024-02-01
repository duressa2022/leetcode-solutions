class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def helperFunction(string1,string2):
            if string1+string2>string2+string1:
                return -1
            else:
                return 1
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        result=sorted(nums,key=cmp_to_key(helperFunction))
        return str(int("".join(result)))
        
            
        