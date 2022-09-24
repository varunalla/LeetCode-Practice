public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int cycleIndex = 1;
        ListNode[] arr = new ListNode[] { new ListNode(3), new ListNode(2), new ListNode(0), new ListNode(-4) };
        for (int i = 1; i < arr.length; i++) {
            arr[i - 1].next = arr[i];
        }
        arr[arr.length - 1].next = arr[cycleIndex];
        Solution s = new Solution();
        System.out.println(s.hasCycle(arr[0]));
    }
}

class ListNode {
    int val;
    ListNode next;

    public ListNode(int val) {
        this.val = val;
        this.next = null;
    }
}