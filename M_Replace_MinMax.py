N = int(input())
A = list(map(int, input().split()))

min_val = min(A)
max_val = max(A)

min_index = A.index(min_val)
max_index = A.index(max_val)
A[min_index], A[max_index] = A[max_index], A[min_index]

for num in A:
    print(num, end=" ")
