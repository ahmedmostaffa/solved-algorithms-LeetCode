/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    nums.sort((a,b)=>a-b);
    var i=0;
    while (nums[i]<1){
        i=i+1
    }
    var ans =1;
    for (let j=i;j<nums.length;j++){
        if (nums[j]==ans){
            ans+=1
        }
        
        else if(nums[i]>ans){
            return ans
        
        }
        
    
    }
    return ans
    
    
};