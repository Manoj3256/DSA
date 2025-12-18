class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell=buy=prices[0]
        p=0
        for i,price in enumerate(prices[1:]):
            if price<buy and not i==len(prices)-1:
                buy=sell=price
            if sell<price:
                sell=price
                if sell-buy>p:
                    p=sell-buy
        return p