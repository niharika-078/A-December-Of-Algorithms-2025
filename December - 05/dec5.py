def search(i, j):
    if i < 0 or i >= R or j < 0 or j >= C:
        return
    if grid[i][j] == 0:
        return

    grid[i][j] = 0   

    search(i+1, j)
    search(i-1, j)
    search(i, j+1)
    search(i, j-1)


R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

count = 0

for i in range(R):
    for j in range(C):
        if grid[i][j] == 1:
            count += 1
            search(i, j)

print(count)
