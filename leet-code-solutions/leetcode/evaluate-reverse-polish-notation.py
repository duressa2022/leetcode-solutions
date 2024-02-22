class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        hashSet={"+","-","*","/"}
        for char in tokens:
            if char in  hashSet:
                xvalue=stack.pop()
                yvalue=stack.pop()
                if char =="+":
                    stack.append(xvalue+yvalue)
                elif char=="-":
                    stack.append(yvalue-xvalue)
                elif char=="*":
                    stack.append(xvalue*yvalue)
                else:
                    if (xvalue>0 and yvalue<0) or (xvalue<0 and yvalue>0) :
                        stack.append(ceil(yvalue/xvalue))
                    else:
                        stack.append(yvalue//xvalue)
            else:
                stack.append(int(char))
        return stack.pop()

                
        