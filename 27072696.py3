num = int(input())
for i in range(num):
    x = str(input())
    score = 0
    bonus = 0
    for j in list(x):
        if j == "O":
            bonus += 1
            score += bonus
        elif j == "X":
            bonus = 0
    print(score)