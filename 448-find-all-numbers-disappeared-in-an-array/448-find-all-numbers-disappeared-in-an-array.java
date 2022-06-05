import java.util.*;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List <Integer> result = new ArrayList <Integer>();
        HashSet <Integer> mark = new HashSet <Integer>();
        
        for(int i : nums)
            mark.add(i);
        for(int i = 1 ; i <= nums.length ; i++)
            if(!mark.contains(i))
                result.add(i);
        return result;
    }   
}