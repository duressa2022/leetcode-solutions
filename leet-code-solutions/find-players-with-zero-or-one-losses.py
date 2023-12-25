class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        result=[]
        hash_map={}
        for u,v in matches:
            if u not in hash_map:
                hash_map[u]=0
            if v not in hash_map:
                hash_map[v]=1
            else:
                hash_map[v]+=1
        result1=[]
        result2=[]
        for player in hash_map:
            if hash_map[player]==0:
                result1.append(player)
            if hash_map[player]==1:
                result2.append(player)
        result.append(sorted(result1))
        result.append(sorted(result2))
        return result
        
        