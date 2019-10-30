"""
This problem is concerned with the problem of optimally buying and selling a
stock once, aas described on Page 2. As an example, consider the following
sequence of stock prices: <310,315,275,295,260,270,290,230,255,250>. The
maximum profit that can be made with one buy and one sell is 30—buy at 260 and
sell at 290. Note that 260 is not the lowest price, nor 290 the highest price.

Write a program that takes an array denoting the daily stock price, and returns
the maximum profit that could be made by buying and then selling one share of
that stock. There is no need to buy if no profit is possible.

"""

def buy_and_sell_stock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit
