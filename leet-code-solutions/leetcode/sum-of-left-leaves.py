# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack=[(root,None)]
        result=0
        while stack:
            current,prev=stack.pop()
            if prev and prev.left is current and not current.left and not current.right:
                result+=current.val
            if current.right:
                stack.append((current.right,current))
            if current.left:
                stack.append((current.left,current))
        return result
        