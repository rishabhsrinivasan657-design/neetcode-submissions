class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxP=0
        price=0

        while r< len(prices):
            price=prices[r]-prices[l]
            maxP=max(maxP,price)
            if prices[l]>=prices[r]:
                l=r
            
            r+=1
        

        return(maxP)
                



            
            
            


                

        