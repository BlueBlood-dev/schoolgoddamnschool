def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

count = 0
answer = []

for i in range(2532000, 2532161):
    if IsPrime(i) and count<5:
        answer.append(i)
        count+=1

for index,item in enumerate(answer):
    print(str(index+1)+' '+str(item))

