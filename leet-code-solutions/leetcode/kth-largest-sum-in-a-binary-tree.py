# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        resultSum=[]
        queue=[root]
        while queue:
            length=len(queue)
            temp=0
            for i in range(length):
                current=queue.pop(0)
                temp+=current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            resultSum.append(temp)
        resultSum.sort()
        return -1 if len(resultSum)<k else resultSum[-k]

        