class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans=[]
        def findDuplicate():
            from collections import defaultdict
            n=len(nums)

            mp = defaultdict(lambda:0)
 
    # Insert all array elements in hash table
            for i in range(n):
                mp[nums[i]] += 1
            
            for key,val in mp.items():
                if val > 1:
                    return key

        def missing_number():
            n=len(nums)
            if n not in nums:
                return n
            for val in range(1,n):
                if val not in nums:
                    return val
                
      
        ans.append(findDuplicate())
        ans.append(missing_number())
        return ans
            
            

    
        