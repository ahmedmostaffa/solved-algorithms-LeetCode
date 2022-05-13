/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    
    var num=Array.from(new Set(nums))
    num.sort((a,b)=>b-a);
    if(num.length<3){
        return num[0]
    }
    return num[2]
};