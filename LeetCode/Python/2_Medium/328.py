# [ LeetCode ] 328. Odd Even Linked List

class ListNode:
    def __init__(self, val: int, next: "ListNode") -> None:
        self.val = val
        self.next = next


def solution(head: ListNode) -> ListNode:
    if not head:
        return head
    
    odd_nodes: ListNode = head
    even_nodes: ListNode = head.next
    even_header: ListNode = head.next
    while even_nodes and even_nodes.next:
        odd_nodes.next = even_nodes.next
        odd_nodes = odd_nodes.next
        even_nodes.next = odd_nodes.next
        even_nodes = even_nodes.next
    odd_nodes.next = even_header
    return head
