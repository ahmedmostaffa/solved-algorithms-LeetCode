import java.util.*;
class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int ans=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==ans){
                ans+=1;
            }
            else if(ans<nums[i]){
                return ans;
            }
        }
        
        
        return ans;
    }
}