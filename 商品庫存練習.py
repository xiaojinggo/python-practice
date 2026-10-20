stock = {"蘋果": 10, "香蕉": 8, "橘子": 5, "葡萄": 20}
total = 0
out_of_stock = 0

for name, qty in stock.items():
    print(f"{name}：{qty}")
    total += qty
    if qty == 0:
        out_of_stock += 1

print(f"總庫存：{total}")
print(f"缺貨商品：{out_of_stock} 種")