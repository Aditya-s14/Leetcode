class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        big = []
        res = []
        count = 0
        for num in nums:
            if num<pivot:
                small.append(num)
            elif num>pivot:
                big.append(num)
            elif num == pivot:
                count+=1

        for s in small:
            res.append(s)

        while count:
            res.append(pivot)
            count-=1

        for b in big:
            res.append(b)
        
        return res

