package Arrays.LC49_Group_Anagrams;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

/*
 * from LeetCode root Directory
 * java -cp . Arrays/LC49_Group_Anagrams/Solution.java
 * 
 */
public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result=new ArrayList<>();
        HashMap<String,List<String>> cache=new HashMap<>();
        for(int i=0;i<strs.length;i++){
            char[] str=strs[i].toCharArray();
            Arrays.sort(str);
            String key=new String(str);
            List<String> bucket=cache.getOrDefault(key,new ArrayList<String>());
            bucket.add(strs[i]);
            cache.put(key,bucket);
        }
        for(String key : cache.keySet()){
                result.add(cache.get(key));
        }
        return result;
    }
    public static void main(String[] inputs){
        Solution sol=new Solution();
        String[] input=new String[]{"eat","tea","tan","ate","nat","bat"};
        List<List<String>> groups=sol.groupAnagrams(input);
        int i=0;
        for(List<String> group:groups){
            System.out.println("Group "+((1+i++))+"");
            for(String str:group)
            {
                System.out.println(str);
            }
            System.out.println("-------------------");
        }
    }
}