class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter=Counter(tiles)
        length=len(tiles)
        result=set()
        def helperFunction(path):
            if len(path[:])!=0:
                result.add(tuple(path[:]))
            if len(path[:])>=length:
                return 
            for char in tiles:
                if counter[char]!=0:
                    path.append(char)
                    counter[char]-=1
                    helperFunction(path)
                    counter[char]+=1
                    path.pop()
        helperFunction([])
        return len(result)

            

        
        