class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        from itertools import permutations  
          
        ans=[]
     
        
        permutations_str = list(permutations(nums))
      
        return permutations_str
                    
 
        