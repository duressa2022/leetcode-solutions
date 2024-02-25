class Solution:
    def simplifyPath(self, path: str) -> str:
        list_path=[path for path in path.split("/") if path!="" and path!="."]
        stack=[]
        print(list_path)
        for path in list_path:
            if path=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(path)
        return "/"+"/".join(stack)
        