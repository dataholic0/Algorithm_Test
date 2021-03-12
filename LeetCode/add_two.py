class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# make test case
l1 = ListNode(9, None)
l1_1 = ListNode(9,l1)
l1_2 = ListNode(9,l1_1)
l1_3 = ListNode(9,l1_2)
l1_4 = ListNode(9,l1_3)
l1_5 = ListNode(9,l1_4)
l1_6 = ListNode(9,l1_5)

l2 = ListNode(9,None)
l2_1 = ListNode(9,l2)
l2_2 = ListNode(9,l2_1)
l2_3 = ListNode(9,l2_2)


class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        while l1 or l2:
        	if l1:
        		list1.append(str(l1.val))
        		l1 = l1.next
        	else:
        		list1.append('0')
        	if l2:
        		list2.append(str(l2.val))
        		l2 = l2.next
        	else:
        		list2.append('0')
        
        list1.reverse()
        list2.reverse()

        list1 = int(''.join(list1))
        list2 = int(''.join(list2))
        list3 = list(str(list1 + list2))
        list3.reverse()

        next_node = None
        answer = ListNode(list3.pop(), None)

        while list3:
        	answer = ListNode(list3.pop(),answer)       
        return answer