class Solution:
    def largestInteger(self, num: int) -> int:
        nums = list(map(int,str(num)))

        even = []
        odd = []

        for num in nums:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)

        even.sort(reverse = True)
        odd.sort(reverse = True)
        res = []
        e_idx = 0
        o_idx = 0
        for num in nums:
            if num%2 == 0:
                res.append(str(even[e_idx]))
                e_idx+=1
            else:
                res.append(str(odd[o_idx]))
                o_idx+=1

        return int(("".join(res)))
