package TwoPointers.LC167_TwoSum;

public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left=0;
        int right=numbers.length-1;
        while(left<right){
            int sum=numbers[left]+numbers[right];
            if(sum==target){
                return new int[]{left+1,right+1};
            }
            if(sum>target){
                right--;
            }
            else{
                left++;
            }
            while(left>0&&numbers[left]==numbers[left-1]){
                left++;
            }
            while(right<numbers.length-1&&numbers[right]==numbers[right+1]){
                right--;
            }
        }
        return new int[]{-1,-1};
    }
    public static void main(String[] args) {
        Solution sol=new Solution();
        int[] result=sol.twoSum(new int[]{10,25,75}, 100);
        System.out.println("["+result[0]+","+result[1]+"]");
        result=sol.twoSum(new int[]{2,7,11,15}, 9);
        System.out.println("["+result[0]+","+result[1]+"]");
        result=sol.twoSum(new int[]{2,3,4}, 6);
        System.out.println("["+result[0]+","+result[1]+"]");
        result=sol.twoSum(new int[]{-1,0}, -1);
        System.out.println("["+result[0]+","+result[1]+"]");
    }
}
