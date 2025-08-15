class Solution {
    public boolean isPowerOfFour(int n) {
        if(n<=0||n>=((int)Math.pow(2,31))-1){
            return false;
        }
        while(n%4==0){
            n/=4;
        }
        return n==1;
    }
}