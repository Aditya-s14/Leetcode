class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        max_profit = 0
        while right<(len(prices)):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit,profit)

            else:
                left = right
            right+=1
        
        return max_profit

#kadene algo
"""class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_profit = 0

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            curr_profit = max(0, curr_profit + diff)
            max_profit = max(max_profit, curr_profit)

        return max_profit"""



        