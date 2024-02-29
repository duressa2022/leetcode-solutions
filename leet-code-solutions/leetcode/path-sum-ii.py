# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:return []
        stack=[[root,root.val,[root.val]]]
        result=[]
        while stack:
            current,value,temp=stack.pop()
            if not current.left and not current.right:
                if value==targetSum:
                    result.append(temp)
            if current.right:
                stack.append([current.right,value+current.right.val,temp+[current.right.val]])
            if current.left:
                stack.append([current.left,value+current.left.val,temp+[current.left.val]])
        return result

        