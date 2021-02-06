# 暴力法
'''class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        cur = res
        digit = 0
        while l1 != None or l2 ! = None:
            total = digit
            if l1 ! = None:
                total + = l1.val
                l1 = l1.next
            if l2 != None:
                total += l2.val
                l2 = l2.next
            digit = total//10
            cur.next = ListNode(total % 10)
            cur = cur.next
        if digit != 0:
            cur.next = ListNode(digit)
            cur = cur.next
        return res.next
'''


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        total = l1.val + l2.val
        digit = total//10
        remain = total % 10
        res = ListNode(remain)
        if l1.next or l2.next or digit:
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += digit
            res.next = self.addTwoNumbers(l1, l2)
        return res
