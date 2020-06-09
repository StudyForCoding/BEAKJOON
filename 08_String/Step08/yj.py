alpha=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
num=0
for i in word:
    for j in alpha:
        if i in j:
            num += alpha.index(j)+3
print(num)
