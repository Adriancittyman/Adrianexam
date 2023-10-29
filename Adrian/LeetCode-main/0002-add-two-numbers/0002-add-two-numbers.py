# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # list 1 
        my_list1 = []
        current = l1
        while current:
            my_list1.insert(0, current.val)
            current = current.next
        result_number1 = int(''.join(map(str, my_list1)))

        # list 2 
        my_list2 = []
        current = l2
        while current:
            my_list2.insert(0, current.val)
            current = current.next
        result_number2 = int(''.join(map(str, my_list2)))

        final = result_number1 + result_number2
        # print(final)
        final = str(final)
        reverse_string = final
        

        head = None
        for char in reverse_string:
            new_node = ListNode(int(char))
            new_node.next = head
            head = new_node
        current = head

        current1=current
        while current:
            print(current.val)
            current=current.next
        return current1
        

            

        
        
        
        
        
        
        
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
# node4 = ListNode(54)

node1.next=node2
node2.next=node3
# node3.next=node4

node12 = ListNode(5)
node22 = ListNode(6)
node32 = ListNode(4)
# node4 = ListNode(54)

node12.next=node22
node22.next=node32
# node3.next=node4

sol = Solution()
sol.addTwoNumbers(node1,node12)
# current = node1

# while current:
#     print(current.val)
#     current=current.next  