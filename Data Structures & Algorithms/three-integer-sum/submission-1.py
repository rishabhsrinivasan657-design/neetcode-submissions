class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        
        

        for start in range(len(nums)):
            if start>0 and nums[start]==nums[start-1]:
                continue
            
            
            
                

            
            left=start+1
            right=len(nums)-1
            target=0-nums[start]
            while left< right:
                if nums[left]+nums[right]> target:
                    right-=1
                elif nums[left]+nums[right]< target:
                    left+=1
                
                elif nums[left]+nums[right]== target:
                    ans.append([nums[start], nums[left], nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                    

                    

                
                
                    
                
        
        return ans


        