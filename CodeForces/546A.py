inp = input().split()
k = int(inp[0])
n = int(inp[1])
w = int(inp[2])
print(k,n,w)
mn = 0
for i in range(w+1):
    mn = mn + (i*k)
print(mn - n)