class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        from collections import defaultdict
        n=len(nums)

        mp = defaultdict(lambda:0)
 
    # Insert all array elements in hash table
        for i in range(n):
            mp[nums[i]] += 1
            
        for key,val in mp.items():
            if val > 1:
                return key
                
                    
            