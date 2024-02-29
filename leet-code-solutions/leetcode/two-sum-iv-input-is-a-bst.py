# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        stack=[root]
        seen=set()
        while stack:
            current=stack.pop()
            if current.val in seen:
                return True
            seen.add(k-current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return  False


        