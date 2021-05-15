"""
This problem is concerned with the problem of optimally buying and selling a stock once,
as described on Page 2. As an example, consider the following sequence of stock prices:
<31.0,31.5,275,295,260,270,290,230,255,250>. The maximum profit that can be made with one buy
and one sell is 30-buy at 260 and sell at 290. Note that 250 is not the lowest price, nor 290 the
highest price.
"""


def maximum_profit(stocks: list[int]) -> int:
    profit: int = 0
    if not stocks:
        return profit
    lowest_price: int = stocks[0]
    for i in range(1, len(stocks)):
        profit = max(profit, stocks[i] - lowest_price)
        lowest_price = min(lowest_price, stocks[i])
    return profit


if __name__ == "__main__":
    assert(maximum_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 30)
    assert(maximum_profit([310, 215, 200, 140]) == 0)
    assert(maximum_profit([150, 160, 170, 180, 200]) == 50)
    assert(maximum_profit([]) == 0)
