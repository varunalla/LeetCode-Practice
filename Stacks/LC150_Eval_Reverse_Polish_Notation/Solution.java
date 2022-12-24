package Stacks.LC150_Eval_Reverse_Polish_Notation;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Stack;

public class Solution {
    
    public int evalRPN(String[] tokens) {
        HashSet<String> chars=new HashSet<>(Arrays.asList(new String[]{"+","-","*","/"}));    
        Stack<Integer> st=new Stack<>();
        for(int i=0;i<tokens.length;i++){
            if(chars.contains(tokens[i])){
                //pop top two of stacks
                int operand2=st.pop();
                int operand1=st.pop();
                switch(tokens[i]){
                    case "+": st.push(operand1+operand2);
                            break;
                    case "-":st.push(operand1-operand2);
                            break;
                    case "*":st.push(operand1*operand2);
                            break;
                    default:st.push((int)Math.floor(operand1/operand2));
                            break;
                }
            }
            else{
                st.push(Integer.parseInt(tokens[i]));
            }
        }
        return st.peek();
    }
    public static void main(String[] args) {
        Solution sol=new Solution();
        System.out.println(sol.evalRPN(new String[]{"2","1","+","3","*"}));
        System.out.println(sol.evalRPN(new String[]{"4","13","5","/","+"}));
        System.out.println(sol.evalRPN(new String[]{"10","6","9","3","+","-11","*","/","*","17","+","5","+"}));
    }
}
