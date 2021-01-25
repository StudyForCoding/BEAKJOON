import sys
input = sys.stdin.readline
'''C++-like code'''
a,b = map(list,input().rstrip().split())
a,b = a[::-1],b[::-1]
answer = []
carry = 0
for idx in range(max(len(a),len(b))):
    try:
        tmp = int(a[idx]) + int(b[idx]) + carry
        if tmp >= 10:
            answer.append(tmp-10)  
            carry = 1
        else: 
            answer.append(tmp)
            carry = 0
    except:
        if len(a) > len(b):  tmp = int(a[idx]) + carry
        else:  tmp = int(b[idx]) + carry
        if tmp >= 10:
            answer.append(tmp-10)  
            carry = 1
        else: 
            answer.append(tmp)
            carry = 0

if carry:  answer.append(carry)
print(*answer[::-1],sep='')