prices = [10, 20, 30]
count = 0
total = 0

for p in prices:
    if p > 100:
        print(p)
        count += 1
        total += p
print(f"最高價：{max(prices)}")
print(f"超過 100 元的有 {count} 件，總和 {total} 元")