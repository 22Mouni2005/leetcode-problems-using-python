class Solution {
    public boolean isPowerOfThree(int n) {
        int s=1,i=0;
        if(n<=0 || n>=((int)Math.pow(2,31))-1){
        return false;
        }
        while(s<n){
            s=(int) Math.pow(3,i);
            i+=1;
        }
        if(s==n){
            return true;
        }
        else
        return false;        
    }
}