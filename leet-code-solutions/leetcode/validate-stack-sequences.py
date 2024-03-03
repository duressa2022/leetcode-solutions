class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        left,right=0,-1
        length=len(pushed)
        stack=[]
        while left<length:
            current=popped[left]
            if stack and stack[-1]==current:
                stack.pop()
                left=left+1
            else:
                for i in range(right+1,length):
                    if current==pushed[i]:
                        right=i
                        break
                    stack.append(pushed[i])
                if right<length and pushed[right]==current:
                    left=left+1
                else:
                    return False
        return True
                
                
        