# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete=set(to_delete)
        result=[]
        if root.val not in to_delete:
            result.append(root)
        stack=[(root,None)]
        while stack:
            cur,par=stack.pop()
            if cur.val in to_delete:
                if cur.left and cur.left.val not in to_delete:
                    result.append(cur.left)
                if cur.right and cur.right.val not in to_delete:
                    result.append(cur.right)

                if par:
                    if par.left and par.left.val==cur.val:
                        par.left=None
                    elif par.right and par.right.val==cur.val:
                        par.right=None

            if cur.right:
                stack.append((cur.right,cur))
            if cur.left:
                stack.append((cur.left,cur))
        return result
        


        