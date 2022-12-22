package Arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

/*
 * from LeetCode root Directory
 * javac -cp . Arrays/LC49_Group_Anagrams.java
 * java -cp . Arrays/LC49_Group_Anagrams
 */
class LC49_Group_Anagrams {
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
        LC49_Group_Anagrams sol=new LC49_Group_Anagrams();
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