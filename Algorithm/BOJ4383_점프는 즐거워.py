"""
1부터 n-1까지 모든 수가 존재해야 하므로 하나라도 겹치면 안 됨
따라서 해당 범위 바깥이거나 중복인 경우로 필터링 하였고
몇개의 입력이 들어온다는 이야기가 없었기 때문에 try-except구문으로 처리하였음
"""
while True:
    try:
        n, *nums = map(int, input().split())
        check_jolly = set()
        for i in range(1, len(nums)):
            num = abs(nums[i - 1] - nums[i])
            if num in check_jolly or num < 1 or num >= n:
                print('Not jolly')
                break
            else:
                check_jolly.add(num)
        else:
            print('Jolly')

    except ValueError:
        break
    except EOFError:
        break
