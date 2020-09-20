y = 0
for i in range(4):
    x = list(map(int, input().split()))
    for j in range(5):
        if x[j] == 1:
            y = abs(i - 1) + abs(j - 1)
print(y)