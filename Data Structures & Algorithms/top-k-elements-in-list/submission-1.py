class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            
            else:
                count[i]+=1
            
        
        
        

        
        top_k_keys = sorted(count, key=count.get, reverse=True)[:k]

        return(top_k_keys)
        
        
          


        