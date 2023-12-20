class Solution:
    def interpret(self, command: str) -> str:
        result=""
        i=0
        while i<len(command):
            if command[i]=="G":
                result+=command[i]
                i=i+1
            elif command[i:i+2]=="()":
                result+="o"
                i=i+2
            else:
                if command[i:i+4]=="(al)":
                    result+="al"
                    i=i+4
        return result
        