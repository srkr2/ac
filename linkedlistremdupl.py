class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_duplicates(head):
    current = head

    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next

    return head

# Example usage:
linked_list = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))

print("Linked List before Removing Duplicates:")
current = linked_list
while current:
    print(current.value, end=" ")
    current = current.next

remove_duplicates(linked_list)

print("\nLinked List after Removing Duplicates:")
current = linked_list
while current:
    print(current.value, end=" ")
    current = current.next
