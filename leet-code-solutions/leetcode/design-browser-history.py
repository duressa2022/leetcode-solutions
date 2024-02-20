class linkedNode:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
class BrowserHistory:
    def __init__(self, homepage: str):
        self.vist=linkedNode(homepage)

    def visit(self, url: str) -> None:
        new_node=linkedNode(url)
        self.vist.right=new_node
        new_node.left=self.vist
        self.vist=new_node

    def back(self, steps: int) -> str:
        while self.vist.left is not None and steps>0:
            self.vist=self.vist.left
            steps=steps-1
        return self.vist.val

    def forward(self, steps: int) -> str:
        while self.vist.right is not None and steps>0:
            self.vist=self.vist.right
            steps=steps-1
        return self.vist.val
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)