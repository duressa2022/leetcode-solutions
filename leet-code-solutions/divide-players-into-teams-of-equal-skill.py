class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        flag=False
        result=0
        init_sum=skill[left]+skill[right]
        while left<right:
            if init_sum!=skill[left]+skill[right]:
                flag=True
                break
            result+=skill[left]*skill[right]
            left=left+1
            right=right-1
        return -1 if flag==True else result

        