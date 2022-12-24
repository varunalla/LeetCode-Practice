package Arrays.LC347_TopK_Frequent_Elements;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

/***
 * java -cp . Arrays/LC347_TopK_Frequent_Elements/Solution.java
 */
public class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> cache=new HashMap<>();
        PriorityQueue<Map.Entry<Integer,Integer>> q=new PriorityQueue<>((a,b)->b.getValue()-a.getValue());
        for(int i=0;i<nums.length;i++){
            cache.put(nums[i],cache.getOrDefault(nums[i],0)+1);
        }
        for(Map.Entry<Integer,Integer> entry: cache.entrySet()){
            q.offer(entry);
        }
        int[] result=new int[k];
        int i=0;
        while(q.size()>0&&k>0){
            Map.Entry<Integer,Integer> entry=q.poll();
            result[i]=entry.getKey();
            k--;
            i++;
        }
        return result;
    }
    public static void main(String[] args) {
        Solution sol=new Solution();
        int[] input=new int[]{1,1,1,2,2,3};
        int[] answer=sol.topKFrequent(input, 2);
        for(int i=0;i<answer.length;i++){
            System.out.println(answer[i]);
        }
    }
}