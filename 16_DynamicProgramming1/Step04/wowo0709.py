t = int(input())
waveband = [0]*101
waveband[0:4] = [1,1,1,2,2]
for test in range(t):
    n = int(input())
    if n in range(waveband.index(0)):
        print(waveband[n-1])
        continue
    for wb in range(waveband.index(0),n):
        waveband[wb] = waveband[wb-1] + waveband[wb-5]
    print(waveband[n-1])