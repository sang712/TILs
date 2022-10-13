'''
연결 리스트에서 중간 노드를 자르고 앞과 뒤 노드를 연결하는 함수를 완성하는 문제
문제에서 head를 주지 않고, input과 주어진 함수의 입력은 서로 달라서 문제를 이해하기 어려웠음
return을 하지 말라는 것에 영감을 얻어서 구현만 하면 된다고 생각했고
다음과 같이 구현하였음
그렇지만 node = node.next가 왜 안 되는 것인지 이해는 되지 않음
-> 함수 내에서 처리를 하는 것이기 때문에 reference로 가져온 node만 변화하고
실제 ListNode에는 영향이 없음, 따라서 깊은 복사 하듯이 내부의 값을 변화 시켜주어야 함
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next