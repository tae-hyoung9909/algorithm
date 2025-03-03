# n은 행, m은 열
n, m = map(int, input().split())

cards = []
result_cards = []

for _ in range(n):
    cards.append(list(map(int, input().split())))


for col in cards:
    result_cards.append(min(col))

print(max(result_cards))