package Arrays.LC17_Letter_Combinations_Phone_Number;

import java.util.ArrayList;
import java.util.List;

public class Solution{
    String[] map= new String[]{"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    public List<String> letterCombinations(String digits) {
        if(digits==null||digits.length()==0){
            return new ArrayList<>();
        }
        ArrayList<String> result=new ArrayList<>();
        generate(digits,0,new StringBuilder(),result);
        return result;
    }
    public void generate(String digits,int index,StringBuilder sb,List<String> result){
            if(digits.length()==index){
                result.add(sb.toString());
                return;
            }
            String currmap=map[digits.charAt(index)-'0'];
            for(int i=0;i<currmap.length();i++){
                sb.append(currmap.charAt(i));
                generate(digits,index+1,sb,result);
                sb.setLength(sb.length()-1);
            }
    }
    public static void main(String[] args) {
        Solution sol=new Solution();
        List<String> strs= sol.letterCombinations("23");
        for(String str:strs){
            System.out.println(str);
        }
    }
}