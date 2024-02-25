class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score=0
        stack=[]
        for char in s:
            if char=="(":
                stack.append(score)
                score=0
            else:
                if score==0:
                    score=1
                else:
                    score=2*score
                score+=stack.pop()
        return score