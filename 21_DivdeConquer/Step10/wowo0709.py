'''
<시간초과 잡은 방법>
1. 거리의 제곱으로 계산
2. y축으로 비교하는 부분에서 두 점이 모두 경계선보다 왼쪽에 있거나 오른쪽에 있는 경우는 pass
'''
import sys
input = sys.stdin.readline

def dist(x,y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2
def find_min_distance(l,r):
    if r-l == 3: # 점이 3개 남았다면,
        return min(dist(points[l], points[l+1]), dist(points[l+1], points[l+2]), dist(points[l], points[l+2]))
    if r-l == 2: # 점이 2개 남았다면,
        return dist(points[l], points[l+1])

    mid = (l+r) // 2
    l_d = find_min_distance(l,mid) # 경계선 기준 왼쪽 영역의 최소 거리
    r_d = find_min_distance(mid,r) # 경계선 기준 오른쪽 영역의 최소 거리
    d = min(l_d,r_d)
    # x좌표 차가 거리 d보다 작은 점들을 후보로 뽑는다. 
    tmp_points = []
    for idx in range(l,r): 
        if (points[mid][0] - points[idx][0])**2 <= d:
            tmp_points.append(points[idx])
    # y축으로 정렬하여 후보들을 뽑으며 최종적으로 최단 거리를 구한다. 
    tmp_points.sort(key=lambda point:point[1])
    for idx1 in range(len(tmp_points)-1):
        for idx2 in range(idx1+1,len(tmp_points)):
            # y좌표 차가 거리 d보다 큰 경우 이후 점들은 볼 필요 없음.
            if (tmp_points[idx2][1] - tmp_points[idx1][1])**2 > d:
                break
            # 경계선 기준 두 점이 모두 왼쪽 혹은 오른쪽에 있다면 d를 구할 때 이미 최소 거리를 구했으므로 pass한다. 
            if (tmp_points[idx1][0]-points[mid][0])*(tmp_points[idx2][0]-points[mid][0]) > 0:
                continue
            d = min(d,dist(tmp_points[idx1],tmp_points[idx2]))

    return d


n = int(input())
p = [[int(x) for x in input().split()] for _ in range(n)]
points = list(set(map(tuple,p)))

if len(points) != len(p):
    print(0)
else:
    points.sort()
    print(find_min_distance(0,len(points)))