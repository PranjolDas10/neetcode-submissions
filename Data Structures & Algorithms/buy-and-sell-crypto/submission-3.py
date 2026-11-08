class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        buy = 0
        sell = 1
        # keep sure sell high stays in range
        # if it is a profit situations, get the diff and check if it is a max
        # then push sell++ to compare next with buy position same place
        # else there is a lower value so we switch our low pos to the high and sell++
        # this goes through all, while keeping our low pos at its lowest
        # return maxdiff if it is a profit

        for sell in range(len(prices)): # fast pointer makes sure it stays in range
            if prices[sell] > prices[buy]:
                maxDiff = max(maxDiff, prices[sell] - prices[buy])
                sell += 1
            else:
                buy = sell
                sell += 1
            if maxDiff <= 0:
                maxDiff = 0
        return maxDiff

