def binarySearch(arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:
        # Element is not present in the array
        return -1

        
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if binarySearch(nums,0,len(nums)-1,target)==-1:
            i=0
            while i<len(nums) and target>nums[i]:
                i+=1
            return i     
            
            
        else:
            return binarySearch(nums,0,len(nums)-1,target)
        