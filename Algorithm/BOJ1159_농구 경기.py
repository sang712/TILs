if __name__ == '__main__':
    n = int(input())
    name_list = []
    for i in range(n):
        z = input()
        name_list.append(z[0])
        
        call_name = set (name_list)
        result = []
        for j in call_name:
            if name_list.count(j) >= 5:
                result.append(j)
                
    if len(result) > 0:
        print(''.join(sorted(result)))
    else:
        print("PREDAJA")