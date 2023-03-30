class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0  # variable to store the maximum profit
        buy=float('inf')  # variable to store the minimum buying price, initialized as positive infinity
        for p in prices:  # loop through each price in the list of prices
            buy=min(buy,p)  # update the minimum buying price
            profit=max(profit,p-buy)  # calculate the profit by selling at the current price and buying at the minimum buying price
        return(profit)  # return the maximum profit
