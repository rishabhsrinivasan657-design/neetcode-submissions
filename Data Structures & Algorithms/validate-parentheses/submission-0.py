class Solution:
    def isValid(self, s: str) -> bool:
        dict={
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack=[]

        for bracket in s:
            if bracket in dict:
                if stack and stack[-1]==dict[bracket]:
                    stack.pop()
                
                else:
                    return False
            
            else:
                stack.append(bracket)
            
        
        if stack:
            return False
        
        else:
            return True


                
            



        