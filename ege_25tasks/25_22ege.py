for i in range(190201,190281):
    k=0
    answer = []
    for j in range(i+1,1,-1):
        if i%j == 0 and j%2==0:
            k+=1
            answer.append(j)
    if k==4:
        print(*answer)
