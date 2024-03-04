# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue=[(root,1,0)]
        result=-float("inf")
        prevNumber=1
        prevLevel=0

        while queue:
            node,number,level=queue.pop(0)
            if level>prevLevel:
                prevLevel=level
                prevNumber=number
            result=max(result,number-prevNumber+1)
            if node.left:
                queue.append((node.left,number*2,level+1))
            if node.right:
                queue.append((node.right,number*2+1,level+1))
        return result
        
        