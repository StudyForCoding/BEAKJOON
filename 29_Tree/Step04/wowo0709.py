import sys
input = sys.stdin.readline

def traverse(v):
    cl,cr = tree[v]
    ans1.append(v) # prefix
    if cl != '.': traverse(cl)
    ans2.append(v) # infix
    if cr != '.': traverse(cr)
    ans3.append(v) # postfix
    return
# main
N = int(input())
tree = {}
for _ in range(N):
    p,cl,cr = input().split()
    tree[p] = (cl,cr)
ans1,ans2,ans3 = [],[],[]
traverse('A') # root
print(''.join(ans1),''.join(ans2),''.join(ans3),sep='\n')
