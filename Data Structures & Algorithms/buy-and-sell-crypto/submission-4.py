class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        high = 0
        diff = 0
        for i in range(len(prices)):
            if prices[high] < prices[low]:
                low = high
                high += 1
            else:
                diff = max(diff, prices[high] - prices[low])
                high += 1
        return diff