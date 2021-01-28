'''
히스토그램을 중간을 경계선으로 나누면서 왼쪽, 오른쪽, 경계선 포함 직사각형 중
가장 큰 직사각형을 구한다. 
'''
import sys
input = sys.stdin.readline

def find_largest_rectangle(l,r):
    if l == r: # 너비가 1이 되었으면 높이를 반환(1*h)
        return h[l]
    
    m = (l+r) // 2
    tmp_l,tmp_r = m,m+1 # 경계선을 포함하는 가장 작은 직사각형부터 시작
    tmp_h = min(h[tmp_l],h[tmp_r])
    tmp_w = 2
    tmp_S = tmp_w*tmp_h
    # 왼쪽 또는 오른쪽으로 더 갈 수 있을 때
    while not ((h[tmp_l]==0 or tmp_l==l) and (h[tmp_r]==0 or tmp_r==r)):
        if (h[tmp_l]==0 or tmp_l==l): # 왼쪽이 막혔다면, 오른쪽으로
            tmp_h = min(tmp_h,h[tmp_r+1])
            tmp_r += 1
        elif (h[tmp_r]==0 or tmp_r==r): # 오른쪽이 막혔다면, 왼쪽으로
            tmp_h = min(tmp_h,h[tmp_l-1])
            tmp_l -= 1
        else: # 양쪽 모두 가능하다면 높이가 더 높은 쪽으로!
            if h[tmp_l-1] > h[tmp_r+1]:
                tmp_h = min(tmp_h,h[tmp_l-1])
                tmp_l -= 1
            else:
                tmp_h = min(tmp_h,h[tmp_r+1])
                tmp_r += 1

        tmp_w += 1
        tmp_S = max(tmp_S,tmp_w*tmp_h)

    return max(find_largest_rectangle(l,m),find_largest_rectangle(m+1,r),tmp_S)

while True:
    h = list(map(int,input().rstrip().split()))
    if h[0] == 0:  break
    print(find_largest_rectangle(1,len(h)-1))