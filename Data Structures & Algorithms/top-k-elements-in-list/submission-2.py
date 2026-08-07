class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        
        ctr=1
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
            
        freq = [[] for _ in range(len(nums) + 1)]
        for number,frequency in count.items():
            freq[frequency].append(number)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
            if len(res)==k:
                return res


        

            
        
        
        

            
        

            
        
        

        
        



        
        
          


        