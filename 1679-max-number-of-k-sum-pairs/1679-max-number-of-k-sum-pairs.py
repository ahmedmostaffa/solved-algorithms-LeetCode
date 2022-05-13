class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
         # Sort array in increasing order
        nums = sorted(nums)
 
    # Stores the final result
        result = 0
 
    # Initialize the left and right pointers
        start, end = 0, len(nums) - 1
     
    # Traverse array until start < end
        while (start < end):
            if (nums[start] + nums[end] > k):
 
            # Decrement right by 1
                end -= 1
 
            elif (nums[start] + nums[end] < k):
 
            # Increment left by 1
                start += 1
             
        # Increment result and left
        # pointer by 1 and decrement
        # right pointer by 1
            else:
                start += 1
                end -= 1
                result += 1
        return result