grades = {"小明": 80, "小華": 90, "小美": 70}
total = 0

for name, score in grades.items():
    total += score

print(f"平均：{total / len(grades)}")