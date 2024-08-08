class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next


    # Constraints
    # The data elements of the linked list argument will always be in non-decreasing order.
    def removeDuplicates(self, head):
        # Write your code here
        current = head
        if head is None:
            return
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return head

