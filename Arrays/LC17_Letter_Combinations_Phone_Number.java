package Arrays;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

class LC17_Letter_Combinations_Phone_Number{
    public List<String> letterCombinations(String digits) {
        HashMap<String,List<String>> map=new HashMap<>();
        map.put("2",Arrays.asList(new String[]{"a","b","c"}));
        map.put("3",Arrays.asList(new String[]{"d","e","f"}));
        map.put("4",Arrays.asList(new String[]{"g","h","i"}));
        map.put("5",Arrays.asList(new String[]{"j","k","l"}));
        map.put("6",Arrays.asList(new String[]{"m","n","o"}));
        map.put("7",Arrays.asList(new String[]{"p","q","r","s"}));
        map.put("8",Arrays.asList(new String[]{"t","u","v"}));
        map.put("9",Arrays.asList(new String[]{"w","x","y","z"}));
        return generate(digits,map);
    }
    public List<String> generate(String digits,HashMap<String,List<String>> map){
            List<String> result=new ArrayList<>();
            if(digits.length()==1){
                result= map.get(""+digits.charAt(0));
            }
            else{
                List<String> newmap=generate(digits.substring(1,digits.length()),map);
                List<String> src=map.get(""+digits.charAt(0));
                HashSet<String> result_int=new HashSet<>();
                for(String s:newmap){
                    for(String src_s:src){
                        result_int.add(src_s+""+s);
                    }
                }
                result=new ArrayList<>(result_int);
            }
            return result;
    }
    public static void main(String[] args) {
        LC17_Letter_Combinations_Phone_Number sol=new LC17_Letter_Combinations_Phone_Number();
        List<String> strs= sol.letterCombinations("23");
        for(String str:strs){
            System.out.println(str);
        }
    }
}