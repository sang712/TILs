def solution(babbling):
    pronounce = ["aya", "ye", "woo", "ma"]
    answer = 0
    for babble in babbling:
        if not is_doubling(babble):
            for p in pronounce:
                babble = babble.replace(p, '')
        if babble == '':
            answer += 1
    return answer

def is_doubling(babble):
    double_pronounce = ["ayaaya", "yeye", "woowoo", "mama"]
    for p in double_pronounce:
        if p in babble:
            return True
    else:
        return False