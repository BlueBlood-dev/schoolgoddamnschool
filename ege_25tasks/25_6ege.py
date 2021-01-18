for i in range(251811, 251827):
    k=0
    answer = []
    for j in range(1, i+1):
        if i%j == 0:
            answer.append(j)
            k+=1
    if k==4:
        print(*answer)