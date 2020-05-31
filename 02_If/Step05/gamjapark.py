hour, minute = map(int, input().split())
print("%d %d"%(hour, minute - 45)) if minute >= 45 else (print("%d %d"%(hour - 1, 15 + minute)) if hour != 0 else print("%d %d"%(23, 15 + minute)))

