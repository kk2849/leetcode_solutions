/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    
    public ListNode carryOver(ListNode n1, ListNode n2) {
        n1.val += n2.val;
        if (n1.val >= 10) {
            n1.val = n1.val%10;
            if (n2.next != null) {
                n1.next = carryOver(new ListNode(1), n2.next);
            }
            else {
                n1.next = new ListNode(1);
            }
        }
        else { // no overflow
            if (n2.next == null) {
                return n1;
            }
            else {
                n1.next = carryOver(new ListNode(0), n2.next);
            }
        }
        return n1;
    }
    
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode sum = new ListNode(0);
        ListNode t = sum;
        
        while (l1 != null || l2 != null) {
            if (l1 == null) {
                t = carryOver(t, l2);
                return sum;
            }
            else if (l2 == null) {
                t = carryOver(t, l1);
                return sum;
            }
            else { //neither are null
               t.val += l1.val+l2.val;
               if (t.val >= 10) {
                   t.val = t.val%10;
                   t.next = new ListNode(1);
               }
               else {
                    if (l1.next == null && l2.next == null) {
                        return sum;
                    }
                   else {
                        t.next = new ListNode(0);
                    }
                }
            }
            t = t.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        
        return sum;
    }
}