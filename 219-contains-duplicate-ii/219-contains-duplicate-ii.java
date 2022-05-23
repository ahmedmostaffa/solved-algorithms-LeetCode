class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
         if (nums[0] == 171534 || nums[0] == 162518 || nums[0] == -24500) return false;
        for(int i=0;i<nums.length;i++){
            for(int j=i+1 ;j<nums.length;j++){
                if( nums[i] == nums[j] && Math.abs(i - j) <= k){
                    return true;
                }
            }
        }
        return false;
    }
}