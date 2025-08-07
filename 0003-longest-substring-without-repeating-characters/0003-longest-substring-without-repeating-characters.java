class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n=s.length(),maxLen=0,left=0,right=0;
        Set<Character>strSet=new HashSet<>();
        while(right<n){
            if(!strSet.contains(s.charAt(right))){
                strSet.add(s.charAt(right));
                maxLen=Math.max(maxLen,right-left+1);
                right++;
            }
            else{
                strSet.remove(s.charAt(left));
                left++;
            }
        }
        return maxLen;
    }
}