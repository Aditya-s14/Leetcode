class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        freq = {}
        result = 0

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for n, count in freq.items():
            if count == 2:
                result ^= n

        return result
