/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
import java.lang.*;
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode front = new ListNode(0);
        ListNode head = front;
        ListNode l1_P = l1;
        ListNode l2_P = l2;
        int carry = 0;
        int sum = 0;
        int ret_val;
        int l1val;
        int l2val;
        while(l1_P!=null||l2_P!=null||carry>0){
            
            l1val = (l1_P==null? 0:l1_P.val);
            l2val = (l2_P==null? 0:l2_P.val);

            sum = l1val + l2val + carry;

            carry = (int)Math.floor(0.1*sum);
            ret_val = sum - 10*carry;
            System.out.println(sum + " "+ carry);
            head.next = new ListNode(ret_val);
            
            head = head.next;
            if(l1_P !=null) l1_P = l1_P.next;
            if(l2_P !=null) l2_P = l2_P.next;
            
        }
        return front.next;
        
        
        
        
        
        
        
    }
}