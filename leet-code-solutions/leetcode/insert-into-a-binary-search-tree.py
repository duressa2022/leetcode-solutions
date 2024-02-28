# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insertFunction(node,val):
            if node is None:
                node=TreeNode(val)
            else:
                if node.val>val:
                    if node.left is None:
                        node.left=TreeNode(val)
                    else:
                        insertFunction(node.left,val)
                else:
                    if node.right is None:
                        node.right=TreeNode(val)
                    else:
                        insertFunction(node.right,val)
        if root is None:
            root=TreeNode(val)
        else:
            insertFunction(root,val)
        return root

        