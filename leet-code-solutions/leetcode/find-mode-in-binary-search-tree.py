# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 0
        stack=[root]
        count_nodes=defaultdict(int)
        while stack:
            current=stack.pop()
            count_nodes[current.val]+=1
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        mode=0
        freq=-float("inf")
        for key in count_nodes:
            if count_nodes[key]>freq:
                freq=count_nodes[key]
                mode=key
        return [key for key in count_nodes if count_nodes[key]==freq]


        