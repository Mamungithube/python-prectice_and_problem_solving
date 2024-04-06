S = input().split()
reversed_words = [S[::-1] for S in S]
reversed_string =" ".join(reversed_words)
print(reversed_string)
