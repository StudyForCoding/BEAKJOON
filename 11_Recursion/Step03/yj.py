def rm(i, j, size): 
    if size == 1: 
        return 
    new_size = size//3 
    for ri in range(3): 
        for rj in range(3): 
            if ri == 1 and rj == 1: 
                for ti in range(i + ri*new_size, i + (ri+1)*new_size): 
                    for tj in range(j + rj*new_size, j + (rj+1)*new_size): 
                        table[ti][tj] = ' ' 
                continue 
            rm(i + ri*new_size, j + rj*new_size, new_size) 

n = int(input()) 
table = [['*']*n for _ in range(n)] 
rm(0, 0, n) 
for t in table: 
    print(''.join(t))
