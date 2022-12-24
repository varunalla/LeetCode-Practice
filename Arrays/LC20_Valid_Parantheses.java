package Arrays;

import java.util.HashMap;
import java.util.Stack;

public class LC20_Valid_Parantheses {
    
    public boolean isValid(String s) {
        HashMap<Character,Character> mapchars=new HashMap<>();
        mapchars.put(')', '(');
        mapchars.put('}', '{');
        mapchars.put(']', '[');
        Stack<Character> st=new Stack<>();
        for(int i=0;i<s.length();i++){
            char c=s.charAt(i);
            if(mapchars.containsKey(c)){
                //validade peek is correct mapping then pop or return false
                if(!st.empty()){
                    if(st.peek().charValue()==mapchars.get(c).charValue()){
                        st.pop();
                    }
                    else{
                        return false;
                    }
                }
                else{
                    st.push(c);
                }
            }
            else{
                st.push(c);
            }
        }
        return st.empty();
    }
    public static void main(String[] args) {
        LC20_Valid_Parantheses sol=new LC20_Valid_Parantheses();
        System.out.println("()");
        System.out.println(sol.isValid("()"));
        System.out.println("()[]{}");
        System.out.println(sol.isValid("()[]{}"));
        System.out.println("(]");
        System.out.println(sol.isValid("(]"));
        System.out.println("]");
        System.out.println(sol.isValid("]"));
    }
}
