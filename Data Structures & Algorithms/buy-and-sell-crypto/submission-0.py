class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxpro=0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[i]>prices[j]:
                    continue
                
                maxpro=max(maxpro,prices[j]-prices[i])


        return maxpro