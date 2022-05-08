/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let n=digits.length;
    
    num=digits.join(''); 
    var nums=BigInt(num)+BigInt(1);
    var str=nums.toString()
    return str.split('')
    
    
    
};  