# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1=[]
        leaf2=[]
        stack1=[root1]
        stack2=[root2]
        while stack1 or stack2:
            if stack1:   
                current1=stack1.pop()
                if not current1.left and not current1.right:
                    leaf1.append(current1.val)
                if current1.left:
                    stack1.append(current1.left)
                if current1.right:
                    stack1.append(current1.right)
            if stack2:
                current2=stack2.pop()
                if not current2.left and not current2.right:
                    leaf2.append(current2.val)
                if current2.left:
                    stack2.append(current2.left)
                if current2.right:
                    stack2.append(current2.right)
        return leaf1==leaf2
            
        
        