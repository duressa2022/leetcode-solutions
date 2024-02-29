# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        stack=[(root,str(root.val))]
        result=[]
        while stack:
            current,value=stack.pop()
            if not current.left and not current.right:
                result.append(value)
            if current.right:
                stack.append((current.right,value+"->"+str(current.right.val)))
            if current.left:
                stack.append((current.left,value+"->"+str(current.left.val)))

        return result
        