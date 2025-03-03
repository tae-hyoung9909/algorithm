N, M, K =  map(int, input().split())
arr = sorted(list(map(int, input().split())))

first = arr[-1:][0]
second = arr[-2:-1][0]

count = 0

while True:
    for _ in range(K):
        if M == 0:
            break
        count += first
        M -= 1
    if M == 0:
        break
    count += second
    M -= 1

print(count)