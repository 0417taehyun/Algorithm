# [ LeetCode ] 876. Middle of the Linked List

class ListNode:
    def __init__(self, val: int, next: "ListNode" | None) -> None:
        self.val = val
        self.next = next
        

def solution(head: ListNode) -> ListNode:
    def get_size_of_linked_list(head: ListNode) -> int:
        size: int = 0
        while head:
            size += 1
            head = head.next
        return size
    
    
    def get_middle_of_linked_list(
        head: ListNode, middle: int
    ) -> ListNode:
        index: int = 0
        while index < middle:
            head = head.next
            index += 1
        return head
    
    
    size: int = get_size_of_linked_list(head)
    middle: int = size // 2
    answer: ListNode = get_middle_of_linked_list(head, middle)
    return answer


def another_solution(head: ListNode) -> ListNode:
    slow_pointer: ListNode = head
    fast_pointer: ListNode = head
    
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    
    return slow_pointer
