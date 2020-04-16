# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):

        num1 = str()
        num2 = str()

        while not l1 == None:
            num1 += str(l1.val)
            l1 = l1.next

        while not l2 == None:
            num2 += str(l2.val)
            l2 = l2.next

        res = (str(int(num1[::-1]) + int(num2[::-1])))[::-1]

        resList = ListNode(int(res[0]))
        counter = resList

        for i in range(1, len(res)):
            new = ListNode(int(res[i]))
            counter.next = new
            counter = counter.next
        return resList












