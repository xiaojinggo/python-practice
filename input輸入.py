name = input("請輸入名字：")
age = input("請輸入年齡：")
print(f"我的名字是{name}，我的年齡是{age}歲")

items = input("請輸入商品名稱：")
price = float(input("請輸入商品單價："))
quantity = int(input("請輸入購買數量："))
total = price * quantity
print(f"{name} 你好，你要買 {quantity} 個{items}，總共 {total:.0f} 元。歡迎再次光臨")