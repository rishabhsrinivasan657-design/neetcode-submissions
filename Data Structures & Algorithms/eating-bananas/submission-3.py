
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r

        while l<=r:
            k=(l+r)//2
            minTime=0
            
            for pile in piles:
                minTime+= -(-pile // k)
            
            if minTime<=h:
                res=min(k,res)
                r=k-1
            
            else:
                l=k+1
        
        return res


       
            
        

        