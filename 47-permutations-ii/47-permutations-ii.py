class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations  
          
        ans=[]
     
        
        permutations_str = list(permutations(nums))
        for perm in permutations_str:
            ans.append(perm)
            
        setter=set(ans)
        ansr=list(setter)
        return ansr

        