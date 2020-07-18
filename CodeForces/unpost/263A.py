x = 0
i = 1
j = 1
for i in range(5):
    for j in range(5):
        x = input()
        if x == 1:
            print(abs(i-3)+abs(j-3))