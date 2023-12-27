class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hash_map={}
        for path in paths:
            ls_string=path.split()
            for index in  range(1,len(ls_string)):
                i=ls_string[index].find("(")
                j=ls_string[index].find(")")
                content=ls_string[index][i+1:j]
                prepared=ls_string[0]+"/"+ls_string[index][:i]
                if content not in hash_map:
                    hash_map[content]=[prepared]
                else:
                    prepared=ls_string[0]+"/"+ls_string[index][:i]
                    hash_map[content].append(prepared)
        result=[name for name in hash_map.values() if len(name)>=2]
        return result

        