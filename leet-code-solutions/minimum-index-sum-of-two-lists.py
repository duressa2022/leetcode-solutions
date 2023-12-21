class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map={val:index for index,val in enumerate(list2)}
        result=[0]
        cur_min=float("inf")
        for i in range(len(list1)):
            if list1[i] in map:
                if cur_min>map[list1[i]]+i:
                    result.pop()
                    result.append(list1[i])
                    cur_min=map[list1[i]]+i
                else:
                    if cur_min==map[list1[i]]+i:
                        result.append(list1[i])
        return result




        