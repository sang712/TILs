'''
234번에서 알게된 답안을 떠올려 응용하였음
2 nodes씩 전진하는 fast과, 1 nodes씩 전진하는 slow로 끝에 도달했을 때 
slow를 출력하면 절반이 되도록 하였음
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow