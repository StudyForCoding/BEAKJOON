def count_num(N,num):
    count = 0
    while N != 0:
        N //= num
        count += N
    return count

n,m = map(int,input().split())
print(min(count_num(n,5)-count_num(n-m,5)-count_num(m,5),
            count_num(n,2)-count_num(n-m,2)-count_num(m,2)))