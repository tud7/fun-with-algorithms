'''
Given two sorted linked lists, merge them so that the resulting linked list is also sorted.
For example:
head1 -> 4 -> 8 -> 15 -> 19
head2 -> 7 -> 9 -> 10 -> 16

merged -> 4 -> 7 -> 8 -> 9 -> 10 -> 15 -> 16 -> 19

@Author: Tu Duong
@Date: 09/06/2020
'''


class LinkedListNode():

    def __init__(self, data):
        self.data = data
        self.next = None


def _to_list(head):

    ret_list = []
    walker   = head

    while walker is not None:
        ret_list.append(walker.data)
        walker = walker.next

    return ret_list


def merge_sorted(head1, head2):

    if head1 == None:
        return head2
    if head2 == None:
        return head1

    # Choose the head of the merged list
    merged_head = None
    if head1.data <= head2.data:
        merged_head = head1
        head1 = head1.next
    else:
        merged_head = head2
        head2 = head2.next
  
    # Maintain a head and a tail pointer on the merged linked list
    # Use tail pointer to add new element
    # Return the head pointer
    merged_tail = merged_head

    while (head1 != None) and (head2 != None):
    
        temp_node = None

        if head1.data <=head2.data:
            temp_node = head1
            head1 = head1.next
        else:
            temp_node = head2
            head2 = head2.next
    
        merged_tail.next = temp_node # Add "new node" to the merged list
        merged_tail      = temp_node # Update tail to point to the new tail node

    # We get here when one of the list runs out of element
    # Link the remaining list to the tail of the merged list.
    if head1 != None:
        merged_tail.next = head1
    if head2 != None:
        merged_tail.next = head2

    return merged_head



import unittest

class TestMergeSorted(unittest.TestCase):

    def test_merge_two_sorted_linkedlist(self):

        head1 = LinkedListNode(4)
        tail1 = head1
       
        tail1.next = LinkedListNode(8)
        tail1      = tail1.next
        tail1.next = LinkedListNode(15)
        tail1      = tail1.next
        tail1.next = LinkedListNode(19)
        tail1      = tail1.next
        tail1.next = LinkedListNode(22)
        tail1      = tail1.next
              
        head2 = LinkedListNode(7)
        tail2 = head2

        tail2.next = LinkedListNode(9)
        tail2      = tail2.next
        tail2.next = LinkedListNode(10)
        tail2      = tail2.next
        tail2.next = LinkedListNode(16)
        tail2      = tail2.next
        
        merged_head = merge_sorted(head1,head2)

        self.assertEqual(_to_list(merged_head), [4, 7, 8, 9, 10, 15, 16, 19, 22])


if __name__ == '__main__':

    unittest.main()


