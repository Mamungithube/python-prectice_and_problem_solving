n = int(input())
lst = list(map(int,input().split()))
cnt = {}
for num in lst:
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1
remove = 0
for num in cnt:
    if cnt[num] >= num:
        remove+=cnt[num] - num
    else:
        remove+=cnt[num]
print(remove)