class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone={"2":"abc",
               "3":"def",
               "4":"ghi",
               "5":"jkl",
               "6":"mno",
               "7":"pqrs",
               "8":"tuv",
               "9":"wxyz"}
        result=[]
        def helperFunction(digits,path,right):
            if len(digits)==len(path):
                result.append("".join(path[:]))
                return 
            current=digits[right]
            for char in phone[current]:
                path.append(char)
                helperFunction(digits,path,right+1)
                path.pop()
        if not digits:
            return []
        helperFunction(digits,[],0)
        return result
            
        