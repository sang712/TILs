count = 0
while True:
    in_val = list(map(int, input().split()))
    if not in_val[0]:
        break

    if count:
        print()

    for fst in range(1, in_val[0]-4):
        for snd in range(fst+1, in_val[0]-3):
            for thrd in range(snd+1, in_val[0]-2):
                for frth in range(thrd+1, in_val[0]-1):
                    for ffth in range(frth+1, in_val[0]):
                        for sxth in range(ffth+1, in_val[0]+1):
                            print(in_val[fst], in_val[snd], in_val[thrd], in_val[frth], in_val[ffth], in_val[sxth])
    count += 1
