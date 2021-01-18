def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

answers = []
for i in range(4730727, 4730818):
    if IsPrime(i):
        answers.append(i)


for index,item in enumerate(answers):
    print(str(index+1)+ ' '+ str(item))
