# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helperFunction(root):
            if root!=None:
                result.append(root.val)
                helperFunction(root.left)
                helperFunction(root.right)
        result=[]
        helperFunction(root)
        return result

       
