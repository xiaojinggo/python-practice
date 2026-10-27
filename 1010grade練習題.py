def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
scores = {"小李": 100, "小王": 55, "小林": 80, "小城": 70, "小美": 90}
total = 0
count = 0

for name, score in scores.items():
    total += score
    grade = get_grade(score)
    if grade == "A":
        count += 1
    print(f"{name}：{score}（{grade}）")

print(f"A的人數：{count}")
print(f"平均分數：{total/len(scores)}")