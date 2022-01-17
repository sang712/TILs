for _ in range(3):
    start_time, end_time = input().split(" ")
    start_h, start_m, start_s = map(int, start_time.split(":"))
    end_h, end_m, end_s = map(int, end_time.split(":"))

    count = 0
    h = start_h
    m = start_m
    s = start_s
    while True:
        if s >= 60:
            s %= 60
            m += 1
            if m >= 60:
                m %= 60
                h += 1
                if h >= 24:
                    h %= 24
        count += 1 if not (h + m + s) % 3 else 0
        if h == end_h and m == end_m and s == end_s:
            break
        s += 1
    print(count)