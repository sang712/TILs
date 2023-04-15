"""
우선 라임의 길이 f에 따라 for문을 돌려서
각 word의 마지막 f자리 글자를 키로 dictionary에 카운트하였음
그 후에 페어로 묶을 수 있는지 확인하여 더했고
그중에서 가장 큰 페어의 개수를 뽑아 출력하였음
"""
for T in range(int(input())):
    n, L, F = map(int, input().split())
    words = input().split()
    pairs = 0
    for f in range(F, L + 1):
        pseudo_rhyme = {}
        for word in words:
            rhyme = word[L-f:]
            pseudo_rhyme.setdefault(rhyme, 0)
            pseudo_rhyme[rhyme] += 1
        temp_pairs = 0
        for num_rhyme in pseudo_rhyme.values():
            temp_pairs += num_rhyme // 2
        pairs = max(pairs, temp_pairs)
    print(pairs)