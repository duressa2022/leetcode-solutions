# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        temp_result=[]
        result=[]
        if not root:
            return []
        stack=[(root,0,0)]
        while stack:
            node,row,col=stack.pop()
            temp_result.append([col,row,node.val])
            if node.right:
                stack.append((node.right,row+1,col+1))
            if node.left:
                stack.append((node.left,row+1,col-1))
        temp_result.sort()
        left,right=0,0
        length=len(temp_result)
        temp=[]
        while right<length:
            if temp_result[left][0]==temp_result[right][0]:
                temp.append(temp_result[right][2])
                right=right+1
            else:
                result.append(temp)
                temp=[]
                left=right
        result.append(temp)
        
        return result

        