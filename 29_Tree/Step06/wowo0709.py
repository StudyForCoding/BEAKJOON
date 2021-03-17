import sys
sys.setrecursionlimit(10**9)
def find_postorder(start, end):
    if start > end:
        return
    else:
        root = preorder[start]
        div = end + 1
        for pos in range(start+1, end+1):
            if root < preorder[pos]:
                div = pos
                break
        find_postorder(start+1, div-1)
        find_postorder(div, end)
        print(root)

preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        find_postorder(0,len(preorder)-1)
        sys.exit(0)