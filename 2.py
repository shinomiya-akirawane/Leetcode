class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        currNode = l1
        num1 = 0
        digit = 1
        while currNode != None:
            temp = currNode.val
            num1 += temp*digit
            currNode = currNode.next
            digit *= 10

        currNode = l2
        num2 = 0
        digit = 1
        while currNode!= None:
            temp = currNode.val
            num2 += temp*digit
            currNode = currNode.next
            digit *= 10

        sum = num1 + num2
        ans = []
        if sum == 0:
            return ListNode()
        while sum > 0:
            digit = sum%10
            ans.append(digit)
            sum //= 10
        preNode = ListNode(ans[0])
        head = preNode
        for num in ans[1:]:
            newNode = ListNode(num)
            preNode.next = newNode
            preNode = newNode
        return head

s = Solution()
l1 = ListNode(2)
newNode1 = ListNode(4)
l1.next = newNode1
newNode11 = ListNode(3)
newNode1.next = newNode11
l2 = ListNode(5)
newNode2 = ListNode(6)
l2.next = newNode2
newNode22 = ListNode(4)
newNode2.next = newNode22
s.addTwoNumbers(l1,l2)