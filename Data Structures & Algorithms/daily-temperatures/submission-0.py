class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[] #pair: [temp,pos]
        for index,value in enumerate(temperatures):
            while stack and stack[-1][0]<value:
                [sTemp,sInd]=stack.pop()
                ans[sInd]=index-sInd
            
            stack.append([value,index])
        
        return ans


            


        