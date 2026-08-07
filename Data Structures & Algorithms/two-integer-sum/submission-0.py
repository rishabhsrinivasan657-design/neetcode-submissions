class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        ans=[]
        for i in range(len(nums)):
            
            temp=target-nums[i]
            if temp in seen:
                n=seen[temp]
                return [n,i]
            else:
                seen[nums[i]]=i


            


            
            




        