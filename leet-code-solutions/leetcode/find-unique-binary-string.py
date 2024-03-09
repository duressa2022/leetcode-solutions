class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        binary=set(nums)
        length=len(nums[0])
        result=[]
        def helperFunction(path):
            string="".join(path[:])
            if len(string)==length:
                if string not in binary:
                    result.append(string)
                    return 
            for num in ["0","1"]:
                if len(path)==length:
                    break
                path.append(num)
                helperFunction(path)
                path.pop()
        helperFunction([])
        return result[0]
        
            
        