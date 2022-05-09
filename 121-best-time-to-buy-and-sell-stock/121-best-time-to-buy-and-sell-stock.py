class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = sys.maxsize
        max_profit = 0
        
        for current_price in prices:
            if current_price < buy_price:
                buy_price = current_price
            else:
                max_profit = max(max_profit, current_price - buy_price)
                
        return max_profit