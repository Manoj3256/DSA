class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=prices[0]
        profit=0
        for  i in range(len(prices)):
            if prices[i] > buy:
                if len(prices)-1 ==i:
                    profit+=prices[i] -buy
                elif  prices[i+1] <prices[i]:
                    profit+=prices[i] -buy
                    buy=prices[i+1]
            elif buy>prices[i] and i != len(prices)-1:
                buy=prices[i]
       
        
        return profit