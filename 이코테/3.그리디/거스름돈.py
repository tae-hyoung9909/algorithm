# 거슬러 줘야 할 돈(n)은 항상 10의 배수이다.
# 거슬러 줘야 할 동전의 최소 개수는?(동전은 500원, 100원, 50원 10원)
n = int(input());

# print(type(n))
charges = [500, 100, 50, 10]
count = 0

for charge in charges:
    count += n // charge
    n %= charge

print(count)