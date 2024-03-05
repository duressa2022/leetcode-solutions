# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        result=[]
        def helperFunction(node):
            if node:
                helperFunction(node.left)
                result.append(node.val)
                helperFunction(node.right)
        def buildTree(array):
            if not array:
                return None
            mid=len(array)//2
            root=TreeNode(array[mid])
            root.left=buildTree(array[:mid])
            root.right=buildTree(array[mid+1:])
            return root
        helperFunction(root)
        return buildTree(result)
        