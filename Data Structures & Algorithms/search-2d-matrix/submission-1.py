class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L=0
        R=len(matrix)-1
        
        while L<=R:
            MID=(L+R)//2
            


            if target > matrix[MID][-1]:
                L=MID+1

            elif target< matrix[MID][0]:
                R=MID-1
            
            elif target<=matrix[MID][-1] and target >= matrix[MID][0]:
                l=0
                r=len(matrix[MID])-1
                while l<=r:
                    mid=(l+r)//2
                    if target> matrix[MID][mid]:
                        l=mid+1
                    
                    elif target< matrix[MID][mid]:
                        r=mid-1
                    
                    elif target==matrix[MID][mid]:
                        return True
                
                return False

        return False            
        



            
                
                
            
            
        
       
            

            

        