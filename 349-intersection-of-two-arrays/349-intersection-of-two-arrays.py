class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_1=list(set(nums1))
        num_2=list(set(nums2))
        from collections import defaultdict
        
        mp = defaultdict(lambda:0)
        ans=[]
 
    # Insert all array elements in hash table
        for i in range(len(num_1)):
            mp[num_1[i]] += 1
        for j in range(len(num_2)):
            mp[num_2[j]] += 1
            
        for key,val in mp.items():
            if val==2:
                ans.append(key)
        return ans        
                
                    
        