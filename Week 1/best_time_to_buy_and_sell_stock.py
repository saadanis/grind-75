class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)

        lowest_buying_price = prices[0]
        max_profit = 0

        for i in range(1, len_prices):
            if prices[i] < lowest_buying_price:
                lowest_buying_price = prices[i]
            else:
                new_profit = prices[i] - lowest_buying_price
                if new_profit > max_profit:
                    max_profit = new_profit
        
        return max_profit
    