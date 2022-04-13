'''
끝을 설정해주지 않아서 try except문으로 걸러 주었고
좀 더 특정지으려고 EOFError를 넣었음
각 단위별로 뽑아내서 각 숫자별 개수를 체크하고
2개 이상인 경우가 있으면 넘기고 아니면 1개씩 세는 방식으로 진행하기
'''
while True:
    try:
        N, M = map(int, input().split())
    except EOFError:
        break
    count = 0
    for num in range(N, M+1):
        counts = [0] * 10
        # 이거도 형변환 없이 while문으로 하고 나눗셈 이용해서 한자리씩 꺼내면 될 듯
        for char in str(num):
            counts[int(char)] += 1
        # 여기서 시간을 많이 잡아먹는 듯 함수로 만들어서 return하는 방식으로 빼야 할 듯
        if 2 in counts or 3 in counts or 4 in counts: 
            continue
        else:
            count += 1
    print(count)