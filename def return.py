def get_result(score):
    if score > 60:
        return "及格"
    else:
        return "不及格"

scores = {"小李": 100, "小王": 60, "小林": 80, "小城": 70}
total = 0
count = 0

for name, score in scores.items():
    total += score
    result = get_result(score)
    if result == "及格":
        count += 1
    print(f"{name}：{score}（{result}）")

print(f"及格人數：{count}人")
print(f"總分數：{total}分")
print(f"平均分數：{total / len(scores)}分")