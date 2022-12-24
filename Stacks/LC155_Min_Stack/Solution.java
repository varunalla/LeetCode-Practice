package Stacks.LC155_Min_Stack;

import java.util.Stack;

class MinStack {
    Stack<Integer> prim;
    Stack<Integer> min;
    public MinStack() {
        this.prim=new Stack<Integer>();
        this.min=new Stack<Integer>();
    }
    
    public void push(int val) {
        this.prim.push(val);
        int minval=val;
        if(!min.isEmpty()){
            minval=Math.min(minval,this.min.peek());
        }
        this.min.push(minval);
    }
    
    public void pop() {
        this.prim.pop();
        this.min.pop();
    }
    
    public int top() {
        return this.prim.peek();
    }
    
    public int getMin() {
        return this.min.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */

public class Solution {
    public static void main(String[] args) {
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin(); // return -3
        minStack.pop();
        minStack.top();    // return 0
        minStack.getMin(); // return -2
    }
}
