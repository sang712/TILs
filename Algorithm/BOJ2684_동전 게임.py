P = int(input())

for _ in range(P):
    result = {'TTT': 0, 'TTH': 0, 'THT': 0, 'THH': 0, 
              'HTT': 0, 'HTH': 0, 'HHT': 0, 'HHH': 0}
    coinflip = input()
    for i in range(38):
        result[coinflip[i:i+3]] += 1
    print(*result.values())