# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack=[root]
        first=float("inf")
        second=float("inf")
        while stack:
            current=stack.pop()
            if current.val<first:
                if first!=second:
                    second=first
                first=current.val
            if current.val>first and current.val<second:
                second=current.val
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return second if second!=float("inf") else -1
        