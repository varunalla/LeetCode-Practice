package Greedy.LC1647_Min_Del_Char_Freq_Unique;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class Solution {
    public int minDeletions(String s) {
        int[] chars=new int[26];
        for(int i=0;i<s.length();i++){
            chars[s.charAt(i)-'a']++;
        }
        ArrayList<Integer> list=new ArrayList<>();
        for(int i=0;i<26;i++){
           if(chars[i]>0) list.add(chars[i]);
        }
        Collections.sort(list,(a,b)->a.compareTo(b));
        HashSet<Integer> visited=new HashSet<>();
        int del=0;
        for(int i=0;i<list.size();i++){
            int currCount=list.get(i);
            while(currCount>0&&visited.contains(currCount)){
                del++;
                currCount--;
            }
            if(currCount>0)
            {
                visited.add(currCount);
            }
        }
        return del;
    }
    public static void main(String[] args) {
        Solution sol=new Solution();
        System.out.println(sol.minDeletions("aab"));
        System.out.println(sol.minDeletions("aaabbbcc"));
        System.out.println(sol.minDeletions("ceabaacb"));
    }
}
