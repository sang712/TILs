V = int(input())
votes_for_B = len(input().replace('A', ''))
if V - votes_for_B > votes_for_B:
    print('A')
elif V - votes_for_B < votes_for_B:
    print('B')
else:
    print('Tie')