#  Talaba natijalarini tahlil qilish

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
grades = get_grades()

print("\nNATIJALAR")
print("Eng yuqori ball:", find_max_grade(grades))
print("Eng past ball:", find_min_grade(grades))
print("O'rtacha ball:", round(calculate_average(grades), 1))

passed = count_passed(grades)
print("60 va undan yuqori olganlar:", passed, "ta")

avg = calculate_average(grades)
yuqori = 0
for ball in grades:
    if ball > avg:
        yuqori += 1
print("O'rtachadan yuqori olganlar:", yuqori, "ta")









#  bankomat  18.3.2026
print("Assalomu alaykum!")
print("Qay turdagi amalni bajarasiz?")
print("1 - Balansni ko'rish")
print("2 - Pul yechish")
print("3 - Pul o'tkazish")
print("4 - PIN kodni o'zgartirish")
print("0 - Chiqish")
balans = 201
PIN = 1234
while True:
    while True:
        try:
            kiritilgan_pin = float(input("\nPIN kodni kiriting: "))
            if kiritilgan_pin == PIN:
                print("PIN to'g'ri! Xush kelibsiz.")
                break
            else:
                print("PIN noto'g'ri! Qayta urinib ko'ring.")
        except ValueError:
            print("Xato! PIN faqat raqamlardan iborat bo'lishi kerak.")
    def balans_korish():
        print(f"\nSizning balansingiz: {balans} $")
    def pul_yechish():
        global balans
        try:
            summa = float(input("Qancha pul yechmoqchisiz? "))
            if summa <= 0:
                print("Summa musbat bo'lishi kerak!")
            elif summa > balans:
                print("Hisobda yetarli mablag' yo'q!")
            else:
                balans -= (summa+summa/100)
                print(f"{summa} $ yechildi.")
                print(f"Kartadagi qolgan pul miqdori: {balans} $")
        except ValueError:
            print("Iltimos, faqat raqam kiriting!")
    def send_money():
        global balans
        try:
            summa = float(input("Qancha pul o'qazmoqchisiz? "))
            if summa <= 0:
                print("Summa musbat bo'lishi kerak!")
            elif summa > balans:
                print("Hisobda yetarli mablag' yo'q!")
            else:
                balans -= summa
                print(f"{summa} $ o'tqazildi.")
                print(f"Kartadagi qolgan pul miqdori: {balans} $")
        except ValueError:
            print("Iltimos, faqat raqam kiriting!")
    while True:
        tanlov = input("\nAmalni tanlang (1/2/3/4/0): ").strip()
        if tanlov == "1":
                balans_korish()
        elif tanlov == "2":
            pul_yechish()
        elif tanlov == "0":
            print("Jarayon tugallandi!")
            break
        else:
            print("Noto'g'ri tanlov! 1, 2, 3, 4 yoki 0 ni kiriting.")
        break

    stop = input("Dastur to'xtasinmi? (ha/yoq): ").strip().lower()
    if stop == "ha":
        print("Dastur to'xtadi.")
        break






#KUTUBXONA TIZIMI

kitoblar = {
    "ikki eshik orasi": 3,
    "o'tgan kunlar": 2,
    "mehrobdan chayon": 4,
    "ensiklopediya": 5,
    "mashinalar olami": 1,
    "supper va oddiy mashina farqi": 2,
    "lug'atlar": 6,
    "yo'riqnoma": 3,
    "xaritalar": 4
}

def show_books():
    print("\nMavjud kitoblar:")
    for nomi, soni in kitoblar.items():
        if soni > 0:
            print(f"   {nomi.capitalize()} — {soni} ta")
        else:
            print(f"   {nomi.capitalize()} — hozir yo'q")

def borrow_book():
    kerakli = input("\nQaysi kitobni olmoqchisiz? ").lower().strip()
    
    if kerakli in kitoblar and kitoblar[kerakli] > 0:
        print(f"{kerakli.capitalize()} kitobi mavjud.")
        
        ism = input("To'liq ismingizni kiriting: ").strip()
        pasport = input("Pasport seriya va raqamingizni kiriting: ").strip()
        manzil = input("Yashash manzilingizni kiriting: ").strip()
        
        if ism == "" or pasport == "" or manzil == "":
            print("Ma'lumotlaringiz to'liq emas! Kitob berilmaydi.")
            return
        
        muddat = input("Kitobni qancha vaqtda qaytarasiz? (7 kunda): ").strip()
        
        if muddat == "7 kunda" or muddat == "7 kun":
            kitoblar[kerakli] -= 1
            print(f"Kitobni oldingiz: {kerakli.capitalize()}")
            print("7 kun ichida qaytarishingiz kerak.")
        else:
            print("Faqat 7 kun muddat bilan kitob beriladi.")
            
    else:
        print("Kechirasiz, bu kitob hozir mavjud emas.")

def return_book():
    nomi = input("\nQaysi kitobni qaytaryapsiz? ").lower().strip()
    
    if nomi in kitoblar:
        kitoblar[nomi] += 1
        print(f"{nomi.capitalize()} kitobi qaytarildi.")
    else:
        print("Bu kitob ro'yxatda yo'q edi, lekin qabul qildik.")

def show_count():
    print(f"\nKutubxonada jami {len(kitoblar)} turdagi kitob bor.")

print("Assalomu alaykum! Kutubxonamizga xush kelibsiz.")

while True:
    print("\n" + "-" * 40)
    print("1. Barcha kitoblarni ko'rish")
    print("2. Kitob olish")
    print("3. Kitob qaytarish")
    print("4. Kitob turlarini ko'rish")
    print("0. Chiqish")
    print("-" * 40)
    
    tanlov = input("Tanlang (1-4 yoki 0): ").strip()
    
    if tanlov == "1":
        show_books()
    elif tanlov == "2":
        borrow_book()
    elif tanlov == "3":
        return_book()
    elif tanlov == "4":
        show_count()
    elif tanlov == "0":
        print("Xayr! Yana kelib turing.")
        break
    else:
        print("Noto'g'ri tanlov, qayta urinib ko'ring.")






# Imtihon natijasi bo‘yicha hisobot
def input_students():
    names = []
    scores = []
    n = int(input("Nechta talaba ma'lumotini kiritasiz? "))
    for i in range(n):
        ism = input(f"{i+1}-talaba ismi: ").strip()
        ball = int(input(f"{ism} ning balli: "))
        names.append(ism)
        scores.append(ball)
    return names, scores

def get_grade_level(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

def create_report(names, scores):
    print("\n=== TALABALAR HISOBOTI ===")
    for i in range(len(names)):
        baho = get_grade_level(scores[i])
        print(f"{names[i]} — {scores[i]} ball — {baho}")

def top_student(names, scores):
    max_ball = max(scores)
    index = scores.index(max_ball)
    print(f"\nEng yuqori ball: {names[index]} ({max_ball} ball)")

names, scores = input_students()
create_report(names, scores)
top_student(names, scores)

a_count = 0
for s in scores:
    if get_grade_level(s) == "A":
        a_count += 1
print("A baho olganlar soni:", a_count, "ta")




# Mehmonxona bron qilish tizimi
room_prices = {
    "oddiy": 150000,
    "yarim lux": 250000,
    "lux": 400000
}

def show_rooms():
    print("\nXona turlari va narxlari:")
    for xona, narx in room_prices.items():
        print(f"   {xona.capitalize()} — {narx} so'm/kun")

def calculate_cost(room_type, days, room_prices):
    if room_type in room_prices:
        return room_prices[room_type] * days
    else:
        print("Bunday xona turi mavjud emas!")
        return 0

def apply_discount(total, days):
    if days > 10:
        return total * 0.85   
    elif days > 5:
        return total * 0.90  
    return total

def make_booking():
    show_rooms()
    xona = input("\nQanday xona turini tanlaysiz? ").lower().strip()
    kun = int(input("Nechta kun qolasiz? "))
    
    umumiy = calculate_cost(xona, kun, room_prices)
    if umumiy == 0:
        return
    
    chegirma = apply_discount(umumiy, kun)
    print(f"\nUmumiy summa: {umumiy} so'm")
    print(f"Chegirma bilan: {int(chegirma)} so'm")

make_booking()


# isismlar va ballarni birlashtirish
names = ["Ali", "Vali","G'ani", "Diyor", "nuri"]
scores = [85, 45, 92, 78, 55]

def combine_data(names, scores):
    return list(zip(names, scores))

def get_passed(students):
    return [s for s in students if s[1] >= 60]

def get_high_scores(students):
    return list(filter(lambda s: s[1] >= 80, students))

def find_lowest(students):
    lowest = min(students, key=lambda s: s[1])
    print(f"Eng past ball: {lowest[0]} ({lowest[1]} ball)")

students = combine_data(names, scores)
print("O'tgan talabalar:", get_passed(students))
print("80+ ball olganlar:", get_high_scores(students))
find_lowest(students)




# Mahsulot va narxlar bilan ishlash

products = ["Telefon", "Noutbuk", "Sichqoncha", "Klaviatura", "Monitor"]
prices = [2500000, 8500000, 150000, 300000, 3200000]

def combine_products(products, prices):
    return list(zip(products, prices))

def expensive_products(data):
    return list(filter(lambda x: x[1] > 2000000, data))

def apply_discount(prices):
    return list(map(lambda p: int(p * 0.9), prices))

def find_most_expensive(data):
    max_item = max(data, key=lambda x: x[1])
    print(f"Eng qimmat mahsulot: {max_item[0]} — {max_item[1]} so'm")

data = combine_products(products, prices)
print("2000000 so'mdan qimmat mahsulotlar:", expensive_products(data))
print("10% chegirma bilan narxlar:", apply_discount(prices))
find_most_expensive(data)