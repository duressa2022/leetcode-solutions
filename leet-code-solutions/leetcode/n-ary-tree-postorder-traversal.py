"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result=[]
        def helperFunction(node):
            if node:
                for child in node.children:
                    helperFunction(child)
                result.append(node.val)
        helperFunction(root)
        return result






        