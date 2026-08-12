class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        cal=[]
        for i,a in enumerate (tokens):
            
            if a=="+":
                r=cal.pop()
                l=cal.pop()
                res=l+r
                cal.append(int(res))
            elif a=="-":
                r=cal.pop()
                l=cal.pop()
                res= l- r
                cal.append(int(res))
            elif a=="*":
                r=cal.pop()
                l=cal.pop()
                res= l* r
                cal.append(int(res))
            elif a=="/":
                r=cal.pop()
                l=cal.pop()
                res= l/ r
                cal.append(int(res))
            
            else:
                cal.append(int(a))
                
                
        
        return cal[0]


        


        