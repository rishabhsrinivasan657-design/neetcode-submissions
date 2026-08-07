class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!= len(t):
            return False
        

        letter={}
        for i in s:
            if i not in letter:
                letter[i]=1
            else:
                letter[i]+=1
        

        for i in t:
            if i not in letter:
                return False
            
            else:
                letter[i]-=1
        

        for ctr in letter.values():
            if ctr >0:
                return False
            
        
        else:
            return True
            
        

        