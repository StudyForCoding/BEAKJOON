import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# make tree and get size of each subtree
def make_tree(currentNode,parentNode):
    for node in tree[currentNode]:
        if node != parentNode:
            size[currentNode] += make_tree(node,currentNode)
    return size[currentNode]

# main
N,R,Q = map(int,input().split()) # 정점의 수,루트의 번호,쿼리의 수
tree = [[] for _ in range(N+1)]
size = [1 for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)
make_tree(R,-1)
for query in range(Q):
    print(size[int(input())])

