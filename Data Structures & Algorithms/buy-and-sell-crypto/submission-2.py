class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxdiff = 0
        l, h = 0, 1
        #mini = prices.index(min(prices))
        for h in range(len(prices)):
            if prices[l] < prices[h]:
                diff = prices[h] - prices[l]
                maxdiff = max(maxdiff, diff)
            else:
                l = h # always get lowest
            h += 1
        if maxdiff <= 0:
            return 0
        return maxdiff