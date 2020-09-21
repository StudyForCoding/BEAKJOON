n = int(input())
operand = tuple(map(int,input().split()))
opcode_list = list(map(int,input().split()))
opcode = {1:0,2:0,3:0,4:0}
for i in range(1,5):
  opcode[i] = opcode.get(i) + opcode_list[i-1]
max = -10**9; min = 10**9

def find(n,index,result):
  global max,min
  if(index == n-1):
    max = max>=result and max or result
    min = min<=result and min or result
    return

  for operator in opcode.items():
    if operator[1] == 0:
      continue
    opcode[operator[0]] -= 1
    if operator[0] == 1:
      result += operand[index+1]
    elif operator[0] == 2:
      result -= operand[index+1]
    elif operator[0] == 3:
      result *= operand[index+1]
    elif operator[0] == 4:
      if result<0:
        result = -(-result//operand[index+1])
      else:
        result //= operand[index+1]
    result_list[index+1] = result
    find(n,index+1,result_list[index+1])
    result = result_list[index]
    opcode[operator[0]] += 1

result_list = [0]*n
result_list[0] = operand[0]
find(n,0,result_list[0]) 
print(max,min,sep='\n')