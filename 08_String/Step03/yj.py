S=list(input())
output = ['-1']*26
for i in range(len(S)):
    if output[ord(S[i])-97] != '-1':
        continue
    else: output[ord(S[i])-97]=str(i)

print(' '.join(output))