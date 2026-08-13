class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we should calculate the profit for each part of the window 
        max_profit = 0
        left = 0

        for right in range(1,len(prices)):
            # we essentially want to maximize profit so for each window
            # calculate the profit and then update max_profit if needed
            max_profit = max(max_profit,prices[right]-prices[left])
            # now an invalid window would be one where profit negative
            while prices[right]-prices[left]<0 and right>left:
                left+=1
        return max_profit

        