class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        res=len(nums)+1
        sumVal=0

        for r in range(len(nums)):
            sumVal+=nums[r]
            while sumVal>=target:
                
                res=min(res,r-l+1)
                sumVal-=nums[l]
                l+=1
            
        
        if res==len(nums)+1:
            return 0
        
        else:
            return res
            
        
        
        



        
        