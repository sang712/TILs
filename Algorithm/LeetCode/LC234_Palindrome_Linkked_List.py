'''
처음으로 linked list가 구현된 문제를 접해 보았음
ListNode 클래스로 정의된 객체였고
head를 리스트 처럼 접근하려니 타입이 달라 불가하다는 내용이 떴음
프린트 해보니 val로 정수값과 next로 ListNode객체를 갖는 node의 연속으로 이루어져 있었음
그래서 for문을 돌려서 값만 추출하여 list형태로 바꾸어 사용하였음
for-else문 다음의 주석된 1줄 코드는 for-else문을 대체하는 간단한 코드이지만 
40ms 정도 시간을 늘임 (1600ms에서 40ms가 의미가 있긴 한가 싶지만)

my_isPalindrome 하단의 isPalindrome은 linked list를 이해하여 문제를 푸는 모습이여서 가져와봤음
1430ms 로 내 코드보다 200ms 가량 빠른 코드임

첫 시작은 fast와 slow를 head에 위치 시키고
루프를 돌면서 fast를 2 nodes 씩 전진시킴
그럴때마다 slow를 한칸씩 전진시키고 rev에는 지나온 node를 역순으로 저장함
nodes의 개수가 홀수이면 slow와 rev를 비교하기 전 slow를 한 칸 더 전진시킴
slow와 rev의 node를 비교하면서 전진하는데, 서로 다르면 중간에 탈출해서 rev가 존재하고
slow와 reve의 nodes가 모두 같으면 None이 되므로 각각 False와 True 리턴

easy 문제였지만 처음으로 linked list를 다뤄본지라 easy하게 다가 오지 않았음
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def my_isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_ = []
        while head:
            list_.append(head.val)
            head = head.next
        length = len(list_)
        for i in range(length//2):
            if not list_[i] == list_[-(1+i)]:
                return False
        else:
            return True
        # return list_ == list_[::-1]
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev