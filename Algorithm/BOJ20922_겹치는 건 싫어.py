"""
투포인트를 적용하여
오른쪽 포인터를 움직이며 주어진 숫자를 차례로 탐색하면서 개수를 세며 저장하고
탐색하던 수가 k가 넘어가면 왼쪽 포인터를 움직이며 개수를 빼며 저장하는 방식으로 구현하였음
카운터를 딕셔너리로 하다가 다른 사람보다 100ms정도 시간이 더 걸려서 그냥 리스트로 구현했더니 272ms가 나왔음
"""
N, K = map(int, input().split())
ai = list(map(int, input().split()))

left, right = 0, 0
checker = [0] * 100_001
length = max_length = 0
while right < N:
    a_right = ai[right]
    if checker[a_right] < K:
        checker[a_right] += 1
        length += 1
        right += 1
        max_length = max(max_length, length)
    else:
        checker[ai[left]] -= 1
        length -= 1
        left += 1
print(max_length)