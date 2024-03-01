# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDifference=0
        def helperFunction(node):
            compareValue=node.val
            stack=[node]
            maxDifference=-float("inf")
            while stack:
                current=stack.pop()
                maxDifference=max(maxDifference,abs(compareValue-current.val))
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
            return maxDifference
        def computeMax(node):
            nonlocal maxDifference
            if node:
                current=helperFunction(node)
                maxDifference=max(maxDifference,current)
                computeMax(node.left)
                computeMax(node.right)
        computeMax(root)
        return maxDifference
                

                

        