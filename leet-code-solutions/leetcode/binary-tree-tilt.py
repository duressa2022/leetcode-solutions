# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        result=0
        def helperFunction(node):
            nonlocal result
            if not node:
                return 0
            left=helperFunction(node.left)
            right=helperFunction(node.right)
            current=abs(left-right)
            result+=current
            return left+right+node.val
        helperFunction(root)
        return result
        
        