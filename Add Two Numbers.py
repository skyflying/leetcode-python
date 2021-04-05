class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = ListNode(0)
        node = result
        te=0
        
        while l1 or l2  or te:
            if l1:
                te +=l1.val
                l1=l1.next
            if l2:
                te +=l2.val
                l2=l2.next
                
            node.next = ListNode(te%10)
            node=node.next
            te=te //10
        return result.next
