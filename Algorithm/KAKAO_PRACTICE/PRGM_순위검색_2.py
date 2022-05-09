# 출처: 프로그래머스 - 다른 사람의 풀이

def solution(info, query):
    # 조건을 담는 딕셔너리 생성
    ## combinations를 import 하지 않아도 되는 방법
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    # 조건을 담은 딕셔너리의 점수를 정렬하였음
    ## 찾을 때 찾는 부분만 정렬하면 시간 초과 나오므로 따로 빼서 작성해야함
    for k in data:
        data[k].sort()

    # 이분 탐색을 통해 조건을 만족하는 최소 점수를 찾기
    ## 이 문제는 항상 조건보다 큰 점수를 찾으므로 한쪽으로만 검색하면 됨
    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        # 이분 탐색
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
        answer.append(len(pool)-l)

    return answer