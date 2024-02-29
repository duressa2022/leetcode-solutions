# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:return 
        result=TreeNode(0)
        temp=result
        current=root
        stack=[]
        while stack or current:
            while current:
                stack.append(current)
                current=current.left
            if stack:
                currentNode=stack.pop()
                temp.right=TreeNode(currentNode.val)
                temp=temp.right
                current=currentNode.right
        return result.right



        