class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr=arr+[-1]
        length=len(arr)
        result=0
        stack=[-1]
        array=[0]*length
        for i,value in enumerate(arr):
            while stack and stack[-1]!=-1 and arr[stack[-1]]>value:
                _index=stack.pop()
                left=_index-stack[-1]
                right=i-_index
                result+=left*right*arr[_index]
            stack.append(i)
        return result%(10**9+7)

        