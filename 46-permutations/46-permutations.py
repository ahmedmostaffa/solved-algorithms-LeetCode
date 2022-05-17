class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        from itertools import permutations  
          
        ans=[]
     
        
        permutations_str = list(permutations(nums))
        for perm in permutations_str:
            ans.append(perm)
            
        return permutations_str
                    
 
        