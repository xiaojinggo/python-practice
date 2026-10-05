import random

answer = random.randint(1, 10)
guess = int(input("請猜一個 1 到 10 的數字："))

if guess < 1 or guess > 10:
    print("請輸入 1 到 10 之間的數字")
elif guess == answer:
    print("恭喜你猜對了！")
elif guess > answer:
    print("太大了")
else:
    print("太小了")

print(f"正確答案是：{answer}")