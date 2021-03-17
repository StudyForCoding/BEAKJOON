import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find_preorder(in_start,in_end,post_start,post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = postorder[post_end]
    ans.append(root)
    # in_root_idx = inorder.index(root) -> 시간초과
    in_root_idx = in_loc[root]
    # postorder는 각 범위의 마지막 노드가 root 노드이기 때문에 다음 범위가 앞으로 1씩 밀립니다. 
    offset = in_start - post_start
    find_preorder(in_start,in_root_idx-1,post_start,in_root_idx-1-offset)
    find_preorder(in_root_idx+1,in_end,in_root_idx-offset,post_end-1)

# main
n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
ans = []
# 시간초과 해결을 위해 위치를 미리 저장
in_loc = [0 for _ in range(n+1)]
for i in range(n): in_loc[inorder[i]] = i
find_preorder(0,n-1,0,n-1)
print(*ans)
