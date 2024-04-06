A = input()
cnt_L = 0
cnt_R = 0
lst = []
B =''
for char in A:
    B += char
    if(char == 'L'):
        cnt_L +=1
    elif(char == 'R'):
        cnt_R +=1
    if(cnt_L==cnt_R):
        lst.append(B)
        B=''
print(len(lst))
for i in lst:
    print(i)
