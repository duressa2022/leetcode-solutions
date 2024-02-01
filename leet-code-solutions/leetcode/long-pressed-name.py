class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left,right=0,0
        length_name,length_typed=len(name),len(typed)
        while left<length_name and right<length_typed:
            if name[left]==typed[right]:
                temp=name[left]
                counter=0
                while left<length_name and name[left]==temp:
                    counter+=1
                    left=left+1
                while right<length_typed and typed[right]==temp:
                    counter-=1
                    right=right+1
                if counter>0:
                    return False
            else:
                return False
        while left<length_name and name[left]==temp:
            left=left+1
        while right<length_typed and typed[right]==temp:
            right=right+1
        return left==length_name and right==length_typed
        
        
        