'''
프로그래머스의 유명한 문제와 같은 문제 같음

우선 옷을 카테고리별로 분류하고 같은 이름의 옷이 없다고 했으니 그냥 카운팅만 해주었음
그렇게 해서 카테고리의 옷을 안 고르는 경우를 포함해서 1에다가 누적으로 곱해주었고
아무 카테고리의 옷을 안 고르는 경우를 제외하기 위해서 1을 빼서 출력하도록하였음
예외의 경우는 아무런 옷도 입력으로 주어지지 않은 경우와
옷의 카테고리가 1개뿐인 경우로
아무런 옷이 없는 경우는 0을 출력하도록,
카테고리가 1개뿐인 경우는 그냥 그 수를 출력하도록 하였음

56ms가 소요되었는데 조금 개선하려면 setdefault 함수를 쓰는 것 대신
Collections의 Counter객체를 이용하면 더욱 빠른 결과를 얻을 수 있을 것임
'''
for tc in range(int(input())):
    n = int(input())
    categories = {}
    for _ in range(n):
        cloth, category = input().split()
        categories.setdefault(category, 0)
        categories[category] += 1
    
    if not categories:
        print(0)
        continue
    if len(categories.values()) == 1:
        print(list(categories.values())[0])
        continue
    combi = 1
    for num in categories.values():
        combi *= num + 1
        
    print(combi - 1)