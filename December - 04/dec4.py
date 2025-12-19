def list_sum(arr, K):
    s = 0
    seen = {0: -1}

    for i in range(len(l)):
        s += l[i]

        if s - K in seen:
            st = seen[s - K] + 1
            end = i
            print(st, end)
            return

        seen[s] = i

    print(-1, -1)


# INPUT
N, K = map(int, input().split())
l = list(map(int, input().split()))

list_sum(l, K)
