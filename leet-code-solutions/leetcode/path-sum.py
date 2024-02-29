# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:return False
        stack=[(root,str(root.val))]
        while stack:
            current,value=stack.pop()
            if not current.left and not current.right:
                if int(value)==targetSum:
                    return True
            if current.right:
                stack.append((current.right,str(int(value)+current.right.val)))
            if current.left:
                stack.append((current.left,str(int(value)+current.left.val)))
        return False
        