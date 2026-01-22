class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hm_list1 = {} # string:index
        res = []
        cur_sum = 0
        min_sum = float('inf')

        for i,s in enumerate(list1):
            hm_list1[s] = i

        for j,s in enumerate(list2):
            if s in hm_list1:
                cur_sum = j+hm_list1[s]
                if cur_sum<min_sum:
                    min_sum = cur_sum
                    res = [s]         # if we find cur_sum smaller than the previous sum we reset
                elif cur_sum == min_sum:
                    res.append(s)
                
        return res


        