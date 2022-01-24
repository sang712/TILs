budget = int(input())

prediction = list(map(int, input().split()))

cash_JH = budget
cash_SM = budget
stock_JH = 0
stock_SM = 0
serial = 0
for i in range(len(prediction)):
    bid = prediction[i]
    if cash_JH >= bid:
        buying = cash_JH//bid
        stock_JH += buying
        cash_JH -= buying*bid

    if i > 0:
        if bid > prediction[i-1]:
            if serial >= 0:
                serial += 1
            else:
                serial = 1
        elif bid < prediction[i-1]:
            if serial <= 0:
                serial -= 1
            else:
                serial = -1
        else:
            serial = 0

    if serial >= 3:
        cash_SM += stock_SM * bid
        stock_SM = 0
    elif serial <= -3: # -3과 같을 때는 안 팔더니 작거나 같으니 파네 이상하네
        buying = cash_SM//bid
        stock_SM += buying
        cash_SM -= buying * bid

    if i == len(prediction) - 1:
        cash_JH += stock_JH * bid
        cash_SM += stock_SM * bid
        
        if cash_JH > cash_SM:
            print("BNP")
        elif cash_JH < cash_SM:
            print("TIMING")
        else:
            print("SAMESAME")