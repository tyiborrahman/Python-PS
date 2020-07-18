n = list(map(int,input().split()))
min = 0
max = 0
n.sort()
for i in range(len(n)):
    if n[i] >= n[1]:
        max += n[i]
    if i < (len(n)-1):
        min += n[i]

print(min,max)