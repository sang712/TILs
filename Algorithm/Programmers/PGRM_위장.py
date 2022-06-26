def solution(clothes):
    clothes_dict = {}
    # 옷의 타입을 키값으로 하여 각 옷 타입에 맞게 옷을 정리함
    for cloth, cloth_type in clothes:
        clothes_dict.setdefault(cloth_type, [])
        clothes_dict[cloth_type].append(cloth)
        
    answer = 1
    # 정답에 옷의 개수+1 을 곱하여 옷을 선택하지 않을 경우를 포함시키고
    for clothes_type, clothes in clothes_dict.items():
        answer *= len(clothes) + 1

    # 리턴하기 전에 1을 빼서 아무런 옷을 선택하지 않는 경우를 제외함
    return answer -1