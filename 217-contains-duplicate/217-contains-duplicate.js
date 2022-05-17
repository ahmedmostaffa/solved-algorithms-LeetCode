/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    
    var arr=nums.filter((item,index)=>nums.indexOf(item) === index)
    if(arr.length==nums.length){
        return false
    }
    return true
};