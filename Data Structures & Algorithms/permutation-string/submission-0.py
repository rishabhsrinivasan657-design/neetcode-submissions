class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        target={}
        check={}
        for i in s1:
            target[i]=1+target.get(i,0)
        
        l=0
        for r in range(len(s1)-1,len(s2)):
            k={}
            for j in range(l, r+1):
                k[s2[j]]=1+k.get(s2[j],0)
            
            if target==k:
                return True

            
            
            l+=1
        
        return False

        