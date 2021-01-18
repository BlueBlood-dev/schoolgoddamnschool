def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

answer = []

for i in range(2532000, 2532161):
    if IsPrime(i) and i%10==7:
        answer.append(i)

for index, item in enumerate(answer):
    print(str(index+1)+' '+str(item))
