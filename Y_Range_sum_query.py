# Input N and Q
N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = []
for i in range(Q):
    L, R = map(int, input().split())
    queries.append((L, R))
for query in queries:
        L, R = query 
        L -= 1
        R -= 1
        sum_of_range = sum(A[L:R+1])
        print(sum_of_range)
