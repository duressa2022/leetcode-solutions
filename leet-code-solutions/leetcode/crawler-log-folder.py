class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for log in logs:
            if stack and log=="../":
                stack.pop()
            elif log=="./":
                continue
            else:
                if log!="../":
                    stack.append(log)
        return len(stack)

        