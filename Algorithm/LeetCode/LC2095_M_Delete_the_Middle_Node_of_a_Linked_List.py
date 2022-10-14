'''
해시값을 가진 객체가 갖는 얕은 복사 특성을 이용해서 필요한 부분을 따로 삭제하는 방법으로
요구사항을 구현하였음
지난 linked list 문제와 같이 slow, fast를 이용하여 절반이 되는 부분을 찾았고
해당 부분을 다음 Node와 연결해주면서 마무리 하였음
단 linked list의 길이가 1일 때를 따로 고려해 주어야 했음
첫 시도는 fast, slow 이외에도 node = slow로 다른 노드를 추가하였는데, 
이는 시간을 4536ms 정도 잡아먹었음
고민한 결과 node는 필요없다고 판단하여 해당 코드를 삭제 하였음
이 경우 linked list의 길이가 2일 때의 경우를 새로 생각해주어야 해서 해당 조건을 넣었음(3425ms)
그 후에 해당 조건을 중간부분을 찾지 않고도 검사할 수 있다는 것을 알아서 상단으로 옮겼더니
시간이 절반가량 줄었음(1806ms)
linked list 문제 재미있는 것 같음
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        elif not head.next.next:
            head.next = None
            return head
        
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        slow.val = slow.next.val
        slow.next = slow.next.next
        
        '''
        node = head
        if node.next == None:
            return None
        while True:
            if node.next == slow:
                node.next = slow.next
                break
            node = node.next
        '''
            
        return head