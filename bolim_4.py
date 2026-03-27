# =============================================
# 1-MASALA: Talaba natijalarini tahlil qilish
# =============================================

def get_grades():
    grades = []
    print("8 ta talabaning ballarini kiriting:")
    for i in range(8):
        ball = int(input(f"{i+1}-talaba balli: "))
        grades.append(ball)
    return grades

def find_max_grade(grades):
    max_ball = grades[0]
    for ball in grades:
        if ball > max_ball:
            max_ball = ball
    return max_ball

def find_min_grade(grades):
    min_ball = grades[0]
    for ball in grades:
        if ball < min_ball:
            min_ball = ball
    return min_ball

def calculate_average(grades):
    summ = 0
    for ball in grades:
        summ += ball
    return summ / len(grades)

def count_passed(grades):
    count = 0
    for ball in grades:
        if ball >= 60:
            count += 1
    return count

# Asosiy dastur
grades = get_grades()

print("\n=== NATIJALAR ===")
print("Eng yuqori ball:", find_max_grade(grades))
print("Eng past ball:", find_min_grade(grades))
print("O'rtacha ball:", round(calculate_average(grades), 1))

passed = count_passed(grades)
print("60 va undan yuqori olganlar:", passed, "ta")

# Qo'shimcha: o'rtachadan yuqori olganlar
avg = calculate_average(grades)
yuqori = 0
for ball in grades:
    if ball > avg:
        yuqori += 1
print("O'rtachadan yuqori olganlar:", yuqori, "ta")