# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        stack=[]
        current=root
        while stack or current is not None:
            while current is not None:
                stack.append(current) 
                current=current.left
            if stack:
                temp=stack.pop()
                result.append(temp.val)
                current=temp.right
        return result
