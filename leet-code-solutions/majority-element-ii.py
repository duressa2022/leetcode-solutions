class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frq=len(nums)//3
        map={}
        for val in nums:
            if val not in map:
                map[val]=1
            else:
                map[val]+=1
        result=[]
        for val in map:
            if map[val]>frq:
                result.append(val)
        return result

        