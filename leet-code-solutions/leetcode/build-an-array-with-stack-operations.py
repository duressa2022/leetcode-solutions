class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result=[]
        stack=[]
        number=1
        index=-1
        while stack!=target and number<=n:
            if len(stack)==len(target):
                result.append("Pop")
                stack.pop()
                index-=1
            else:
                if stack and stack[-1]!=target[index]:
                    result.append("Pop")
                    stack.pop()
                    index-=1
                else:
                    result.append("Push")
                    stack.append(number)
                    number+=1
                    index=index+1
        return result

        