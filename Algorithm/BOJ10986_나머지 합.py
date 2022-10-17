'''
구현으로 풀었을 때는 시간초과가 났음 (길이 N+1, idx 0의 값은 0으로 고정)
그래서 구간합을 구할 때 각 누적합을 서로 빼서 구하기 때문에
나눗셈에 영향이 없으므로 미리 M으로 나눠서 넣는 방법을 사용하였음
그리고 서로 같은 수가 나오는 것 끼리 묶어서 2개를 선택하는 조합 공식을 이용하였음
단 N+1로 구간합을 구한 것 처럼 0번 인덱스의 0또한 같이 고려해주어야했음
(처음부터 구간합은 0을 빼는 것으로 취급하므로)
972ms로 통과하였고
600ms대로 나오는 사람들이 궁금해서 조금 고민해보니
따로 구간합 list를 사용하여 이전 값을 호출하지 않고
계산한 값을 그대로 계속 사용할 수 있을 것 같아서
해당 방법으로 고쳐 792ms가 되었음

다른 사람의 속도를 따라가지 못하는 것은 아마 setdefault 함수 때문인 것 같음
0부터 m-1까지 인덱스를 갖는 리스트를 선언하여 계산하면 빠를 수도
'''
N, M = map(int, input().split())
A = list(map(int, input().split()))

# acc = [0] * (N+1)
nums = {0: 1}
remain = 0
for i in range(N):
    # remain = (acc[i] + A[i]) % M
    remain = (remain + A[i]) % M
    nums.setdefault(remain, 0)
    nums[remain] += 1
cnt = 0
for num, num_of_num in nums.items():
    cnt += (num_of_num * (num_of_num-1)) // 2
print(cnt)