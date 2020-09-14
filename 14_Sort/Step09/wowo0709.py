import sys
N = int(input())
member = []
for i in range(N):
  age,name = sys.stdin.readline().split()
  member.append([int(age),name])
for mem in sorted(member,key=lambda m: (m[0])):
  sys.stdout.write(str(mem[0])+" "+mem[1]+"\n")