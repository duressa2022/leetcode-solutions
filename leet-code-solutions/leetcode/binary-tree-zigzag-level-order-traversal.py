# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=[root]
        index=1
        result=[]
        while queue:
            length=len(queue)
            temp=[]
            for i in range(length):
                current=queue.pop(0)
                temp.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            if index%2==1:
                result.append(temp)
            else:
                temp=temp[::-1]
                result.append(temp)
            index+=1
        return result
            

        