scores = [80, 90, 70, 85]
total = 0

for s in scores:
    print(f"分數：{s}")
    total += s

print(f"總和：{total}")

average = total / len(scores)
print(f"平均：{average}")