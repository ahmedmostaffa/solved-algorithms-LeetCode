class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        if n not in nums:
            return n
        for val in range(0,n):
            if val not in nums:
                return val
        