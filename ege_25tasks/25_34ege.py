def findNums(number):
    request = []
    count = 0
    for i in range(number+1, 1, -1):
        if count == 2:
            break
        else:
            if (number % i == 0):
                request.append(i)
                count+=1
    return request

maxk = 0

for i in range(586132, 586430):
    k=0
    for j in range(1,i+1):
        if i%j==0:
            k+=1
            if k>maxk:
                maxk=k

answer = []

for i in range(586132, 586430):
    k = 0
    for j in range(1, j+1):
        if i%j==0:
            k+=1
        if k==maxk:
            answer.append(i)

minimal, maximal = answer[0],answer[len(answer)-1]
requestMin,requestMax = findNums(minimal), findNums(maximal)
print(maxk, *requestMin)
print(maxk, *requestMax)
