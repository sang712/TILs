def nextPermutation(arr):
    i = len(arr)-2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    if i == -1: # arr의 길이는 1이상이므로 i==-1이면 1자리의 단어
        return False

    j = len(arr)-1
    while arr[i] >= arr[j]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    result = arr[:i+1]
    result.extend(list(reversed(arr[i+1:]))) # 정렬 하는 것이 아니라 뒤집는 것
    # 어차피 i를 찾을 때 그냥 넘어간 구간은 끝에서부터 작은 순서대로 정렬되어 있음
    # 그래서 i를 자기 값에 맞는 공간에 찾아 넣고 거꾸로 뒤집으면 오름차순 정렬이 되는 것
    return result

T = int(input())
for _ in range(T):
    word = list(input())
    answer = nextPermutation(word)
    if not answer:
        print(''.join(word))
    else:
        print(''.join(answer))

# 거꾸로 뒤집나 정렬하나 걸리는 시간은 똑같음