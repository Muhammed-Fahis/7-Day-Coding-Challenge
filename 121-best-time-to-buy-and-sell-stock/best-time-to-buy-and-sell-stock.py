class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Two-pointer
        left,right=0,1
        profit=0

        while right < len(prices):
            #profitable
            if prices[right] > prices[left]:
                profit=max(profit,prices[right] - prices[left])
            else:
            #nonprofitable
                left=right
            right += 1
        return profit

        
        