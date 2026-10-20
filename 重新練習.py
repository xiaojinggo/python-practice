scores = {"小李":100, "小王":55,"小林":80, "小城":70}
total = 0
count = 0

for n, s in scores.items():
    total += s
    if s>=60:
        result = "及格"
        count += 1
    else:
        result = "不及格"

    print(f"{n}:{s}({result})")


print(f"及格人數：{count}人")
print(f"總分數：{total}分")
print(f"平均分數：{total/len(scores)}")     

#len(scores)  # 4筆

def add(a, b):
    return a + b

print(add(3, 5))    # 8
