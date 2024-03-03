# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        counter=0
        stack=[(root,-float("inf"))]
        while stack:
            current,path=stack.pop()
            if path<=current.val:
                counter=counter+1
            if current.right:
                stack.append((current.right,max(current.val,path)))
            if current.left:
                stack.append((current.left,max(current.val,path)))
        return counter
        