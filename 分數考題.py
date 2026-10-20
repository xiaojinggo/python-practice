scores = {"小明": 85, "小華": 55, "小美": 92, "小強": 60}
total = 0
count = 0
result = 0

for name, score in scores. items():
    total += score
    
    if score >= 60:
        result = "pass"
        count += 1
    else:
        result = "fail"
    print(f"{name}:{score}({result})")
        

print(f"及格人數：{count}人")
print(f"平均分數：{total/len(scores)}")