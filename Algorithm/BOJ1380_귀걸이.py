"""
입력 받은 여학생들은 dictionary 자료구조로,
귀걸이 압수, 회수 여부는 set 자료구조로 저장하여
마지막에 남는 학생의 번호를 이용해 학생의 이름을 출력하도록 하였음
"""
scenario = 1
while True:
    
    n = int(input())
    if n == 0:
        break
    
    girls = {}
    for i in range(1, n + 1):
        girls[i] = input()
    
    numbers = set()
    for _ in range(2 * n - 1):
        num, _ = input().split()
        if num in numbers:
            numbers.discard(num)
        else:
            numbers.add(num)
    
    print(scenario, girls[int(numbers.pop())])
    
    scenario += 1