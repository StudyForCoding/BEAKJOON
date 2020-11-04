#'-'를 기준으로 리스트를 나눔
arr=input().split('-')
plus2=[]
for i in arr:
    plus1=0
    a=i.split('+')
    for j in a:
        plus1+=int(j)
    plus2.append(plus1)
        
result=plus2[0]
for i in range(1, len(plus2)):
    result-=plus2[i]


print(result)
