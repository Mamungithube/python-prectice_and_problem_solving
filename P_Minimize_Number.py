n = int(input())
lst = list(map(int,input().split()))
tmp = 0
for i in range(n):
    cnt = 0
    if(lst[i] % 2 == 1):
        tmp = 0
        break
    while(lst[i] % 2 ==0):
        cnt += 1
        lst[i] /= 2
    if i == 0 or cnt < tmp:
        tmp = cnt
print(tmp)