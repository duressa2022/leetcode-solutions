class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        length=len(s)
        result=[]
        def helperFunction(path,index):
            if index>=length:
                result.append("".join(path[:]))
                return 
            current=s[index]
            for char in {current.lower(),current.upper()}:
                path.append(char)
                helperFunction(path,index+1)
                path.pop()
        helperFunction([],0)
        return result

        