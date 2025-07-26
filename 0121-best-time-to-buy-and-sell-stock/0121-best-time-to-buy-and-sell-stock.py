class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        mini_price=prices[0]
        for i in prices:
            if i>mini_price:
                maxi=max(maxi,i-mini_price)
            else:
                mini_price=i
        return maxi