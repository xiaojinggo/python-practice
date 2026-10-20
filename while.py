import random

answer = random.randint(1, 10)
guess = 0
count = 0

while guess != answer and count < 5:
    guess = int(input("請猜一個 1 到 10 的數字："))

    if guess < 1 or guess > 10:
        print("請輸入 1 到 10 之間的數字")
    else:
        count += 1
        if guess > answer:
            print("太大了")
        elif guess < answer:
            print("太小了")

if guess == answer:
    print(f"恭喜你，答對了！你猜了 {count} 次才猜對")
else:
    print("很遺憾，你沒有在 5 次內猜對。")
    print(f"正確答案是：{answer}")