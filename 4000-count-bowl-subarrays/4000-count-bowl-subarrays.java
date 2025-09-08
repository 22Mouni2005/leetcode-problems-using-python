class Solution {
    public long bowlSubarrays(int[] nums) {
       int n=nums.length;
       int[] leftmax=new int[n];
        leftmax[0]=nums[0];
        int[] rightmax=new int[n];
        rightmax[n-1]=nums[n-1];
        for(int i=1;i<n;i++){
            leftmax[i]=Math.max(leftmax[i-1],nums[i]);
        }
        for(int i=n-2;i>=0;i--){
            rightmax[i]=Math.max(rightmax[i+1],nums[i]);
        }
        long cnt=0;
        for(int i=1;i<n-1;i++){
            if(nums[i]<leftmax[i] && nums[i]<rightmax[i])
                cnt++;
        }
        return cnt;}}