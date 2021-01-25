import sys
input = sys.stdin.readline

n_city = int(input())
road_len = list(map(int,input().split()))
oil_price = list(map(int,input().split()))
cheapest_oil_price,min_price = oil_price[0],0
# 첫번째 도시부터 차례로 나아가며 가장 싼 도시의 기름 가격을 구하고,
# 해당 도시의 기름을 넣는다.  
for i in range(n_city-1):
    cheapest_oil_price = min(cheapest_oil_price,oil_price[i])
    min_price += cheapest_oil_price * road_len[i]
print(min_price)