"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result=[]
        def helperFunction(node):
            if root:
                result.append(node.val)
                for child in node.children:
                    if child is not None:
                        helperFunction(child)
        helperFunction(root)
        return result

        