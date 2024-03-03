# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=[root]
        max_result=-float("inf")
        min_level=0
        current_level=0
        while queue:
            length=len(queue)
            current_sum=0
            for i in range(length):
                current=queue.pop(0)
                current_sum+=current.val
                if current.right:
                    queue.append(current.right)
                if current.left:
                    queue.append(current.left)
            current_level+=1
            if max_result<current_sum:
                max_result=current_sum
                min_level=current_level
        return min_level




        