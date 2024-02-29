# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        queue=[root]
        result=[]
        while queue:
            length=len(queue)
            maxValue=-float("inf")
            for index in range(length):
                current=queue.pop(0)
                maxValue=max(current.val,maxValue)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(maxValue)
        return result
        