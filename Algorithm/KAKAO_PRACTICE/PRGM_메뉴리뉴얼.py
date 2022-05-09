from itertools import combinations as combi

def solution(orders, course):
    answer = []
    
    # 가능한 경우의 수와 해당 주문 수 딕셔너리에 정리
    comb = {}
    for comb_menu in orders:
        for i in course:
            for menu in combi(comb_menu,i):
                menu = ''.join(sorted(menu))
                comb.setdefault(''.join
                                (menu), 0)
                comb[menu] += 1
                
    # 2번 이상 주문된 세트를 메뉴의 종류 수에 맞게 리스트에 다시 정리
    courses = [[] for _ in range(11)]
    for key, value in comb.items():
        if value >= 2:
            courses[len(key)].append((key, value))
    
    # 리스트에 넣은 세트를 크기 순으로 정렬하고 가장 많이 주문된 것들만 answer리스트에 담음
    for comb_menu in courses:
        if len(comb_menu) > 0:
            list = sorted(comb_menu, key = lambda x: (-x[1], x[0]))
            max = list[0][1]
            for menu, value in list:
                if value == max:
                    answer.append(menu)
    
    # answer 리스트 사전순으로 정렬
    answer = sorted(answer)
    return answer