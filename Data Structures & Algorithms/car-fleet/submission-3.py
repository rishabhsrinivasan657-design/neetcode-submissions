class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed=[]
        stack=[]
        val=0
        for i in range (len(position)):
            posSpeed.append([position[i],speed[i]])
        
        posSpeed.sort(reverse=True)

        
        for car in posSpeed:
            time= (target-car[0])/car[1]
            if not stack:
                stack.append(time)

            elif stack and time>stack[-1]:
                stack.append(time)
            
            
            
            


            
            
           
        
        

        


            
             

        return len(stack)
        