# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        stack=[root]
        while stack:
            current=stack.pop()
            if current is not None:
                result.append(current.val)
            if current is not None and current.right is not None:
                stack.append(current.right)
            if current is not None and current.left is not None:
                stack.append(current.left)
        return result
