N = int(input())
def check(word):
    if len(word) <3: return 1
    else:
        for j in range(len(word)-1):
            if word[j]!=word[j+1] and word[j] in word[j+2:]:
                return 0
        return 1
num=0
for i in range(N):
    word = input()
    num+=check(word)
print(num)