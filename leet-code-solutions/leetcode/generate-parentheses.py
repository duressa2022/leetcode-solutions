class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def helperFunction(path,left,right):
            if left==right==n:
                result.append(path)
                return 
            if left<n:
                helperFunction(path+"(",left+1,right)
            if right<left:
                helperFunction(path+")",left,right+1)
        helperFunction("",0,0)
        return result
        