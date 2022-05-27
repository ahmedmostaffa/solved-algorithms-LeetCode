class Solution {
    public boolean check_even(int x){
        boolean flag=false;
        if(x%2==0){
            flag=true;
            return flag;
        }
        return flag;
    }
    public int numberOfSteps(int num) {
        int count =0;
        while(num!=0){
            if(check_even(num)==true){
                num=num/2;
                count+=1;
                
            // even code
            }
            else{
                num--;
                count+=1;
            // odd code
            
            
            }    
        }
        return count;
        
    }
    
}