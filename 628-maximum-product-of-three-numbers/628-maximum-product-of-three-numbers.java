import java.util.*;
class Solution {
    public int maximumProduct(int[] arr) {
        int n= arr.length;
        if (n < 3) {
            return -1;
        }
 
        // Sort the array in ascending order
        Arrays.sort(arr);
        /*
        for positive values
        Return the maximum of product of last three
        */
        /*
        for negative values
        Return the maximum of product of first elements
        */
        return Math.max(arr[0] * arr[1] * arr[n - 1],
                arr[n - 1] * arr[n - 2] * arr[n - 3]);
    
    }
}