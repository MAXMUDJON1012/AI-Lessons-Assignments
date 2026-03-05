                                             # STRING 1.PART
# 2.question
isim=input("Ismingiz nima?")
print(isim.lower())
#3.question
familiya=input("familyangiz nima?")
print(len(familiya) and familiya.__len__())
# 4.question
print(familiya[-1])
# 5 Question
matn = input("Matn kiriting: ")
print(matn[0])

# 6 Question
matn = input("Matn kiriting: ")
print(matn[-1])

# 7 Question
matn = "Hello, World!"
print(matn.replace("World", "Python"))

# 8 Question
s1 = input("Birinchi matn: ")
s2 = input("Ikkinchi matn: ")
print(s1 + s2)

# 9 Question
matn = input("Matn kiriting: ")
for belgi in matn:
    print(belgi)

# 10 Question
matn = input("Matn kiriting: ")
print(matn[::-1])

# 11 Question
soz = input("So'z kiriting: ")
print(len(soz))

# 12 Question
print("Hello, Python!".upper())

# 13 Question
matn = input("Matn kiriting: ")
print(matn.lower().count("a"))

# 14 Question
matn = input("Matn kiriting: ")
if len(matn) >= 2:
    print(matn[0], matn[-1])

# 15 Question
s1 = input("Birinchi matn: ")
s2 = input("Ikkinchi matn: ")
if len(s1) > len(s2):
    print("Birinchi uzunroq")
elif len(s2) > len(s1):
    print("Ikkinchi uzunroq")
else:
    print("Uzunliklari teng")


                                                   #LIST PART 2
# 1. Question
royxat = []
print("1. Bo'sh ro'yxat:", royxat)

# 2.Question 
royxat = ["olma", "banan", "shaftoli"]
print("2. Mevalar:", royxat)

# 3.Question
print("3. Birinchi meva:", royxat[0])

# 4. Question
royxat.append("anor")
print("4. Yangi ro'yxat:", royxat)

# 5. Question
son=[]
for s in range(5):
    krit=int(input("son kiriting?"))
    son.append(krit)
print(son)

# 6. Question
print("6. Oxirgi son:", son[-1])

# 7. Question
son[1] = 100
print("7. Ikkinchi element o'zgartirilgandan keyin:", son)

# 8. question
royxat.sort()
print("8. Mevalar alifbo tartibida:", royxat)

# 9. Question
ismlar = []
print("\n9. Iltimos 3 ta ism kiriting:")
for i in range(3):
    ism = input("Isim kiriting! ")
    ismlar.append(ism)

print("Kiritilgan ismlar:", ismlar)

# 10. Question
print("\n10. Ismlar ro'yxati (for tsikli bilan):")
for ism in ismlar:
    print(ism)

# 11.Question
royxat.append("apelsin")
royxat.append("kiwi")
print("\n11. Yangi mevalar qo'shilgandan keyin:", royxat)
print("Elementlar soni:", len(royxat))

# 12.Question
royxat.remove("banan")
print("12. Banan olib tashlangandan keyin:", royxat)

# 13. Question
print("13. Teskari tartibda:", royxat[::-1])

# 14. Question
royxat.clear()
print("14. Ro'yxat tozalandi:", royxat)


# Qo'shimcha: Ikkita ro'yxatni birlashtirish
print("\n--- Ikkita ro'yxatni birlashtirish misoli ---")
ro_yxat1 = ["olma", "anor", "behi"]
ro_yxat2 = ["shaftoli", "o'rik", "gilos"]

# 1-usul: + operatori bilan
birlashtirilgan = ro_yxat1 + ro_yxat2
print("1-usul (+):", birlashtirilgan)

# 2-usul: extend() metodi bilan
ro_yxat1.extend(ro_yxat2)
print("2-usul (extend):", ro_yxat1)
                                                                   
                                                                   
                                                                    #  TUPLE part3

# 1. Bo'sh kortej yarating va uni chop eting
t1 = ()
print("1. Bo'sh kortej:", t1)

# 2. Uchta elementli kortej yarating va uni chop eting
t2 = (15, 7, 42)
print("\n2. Uch elementli kortej:", t2)

# 3. Kortejning birinchi elementini chop eting
print("\n3. Birinchi element:", t2[0])

# 4. Foydalanuvchidan 4 ta raqam so'rang va ularni kortejga joylashtiring
print("\n4. Iltimos 4 ta butun son kiriting:")
a = int(input("→ "))
b = int(input("→ "))
c = int(input("→ "))
d = int(input("→ "))
t4 = (a, b, c, d)
print("Siz kiritgan kortej:", t4)

# 5. Kortej ichidagi elementlarni for tsikli yordamida chop eting
print("\n5. Elementlarni birma-bir:")
for x in t4:
    print(x)

# 6. Kortejning uzunligini aniqlang va chop eting
print("\n6. Uzunligi:", len(t4))

# 7. Kortejdagi oxirgi elementni chop eting
print("\n7. Oxirgi element:", t4[-1])

# 8. Ikkita kortejni birlashtirib, yangi kortej yarating
t5 = ("python", "tuple", "immutable")
t6 = t2 + t5
print("\n8. Birlashtirilgan kortej:", t6)

# 9. Kortejdagi eng katta va eng kichik elementni chop eting
numbers = (18, 5, 92, 3, 47, 81, 12)
print("\n9. Sonlar:", numbers)
print("Eng katta:", max(numbers))
print("Eng kichik:", min(numbers))

# 10. Kortejda bitta element mavjudligini tekshiring
print("\n10. Tekshiruvlar:")
print("92 borligi:", 92 in numbers)
print("100 borligi:", 100 in numbers)
print("'python' borligi:", "python" in t6)

# 11. Kortejdan kesma (slice) olish
print("\n11. Kesmalar (slice):")
print("Birinchi 3 ta:", numbers[:3])
print("Oxirgi 3 ta:", numbers[-3:])
print("2-indexdan 5-indexgacha:", numbers[2:6])
print("Har ikkinchi element:", numbers[::2])
print("Teskarisiga:", numbers[::-1])

# 12. Kortejdagi barcha raqamlarni yig'indisini toping
print("\n12. Yig'indi:", sum(numbers))

# 13. Kortejni alifbo tartibida chop eting (sorted → yangi list qaytaradi)
fruits = ("shaftoli", "olma", "anor", "banan", "uzum")
print("\n13. Mevalar:", fruits)
print("Alifbo tartibida:", tuple(sorted(fruits)))

# 14. Kortejdagi qiymatlar sonini sanash (.count())
colors = ("qizil", "yashil", "ko'k", "qizil", "sariq", "qizil", "yashil")
print("\n14. Ranglar:", colors)
print("'qizil' necha marta:", colors.count("qizil"))
print("'yashil' necha marta:", colors.count("yashil"))
print("'oq' necha marta:", colors.count("oq"))

# 15. Kortejdagi raqamlarni teskari tartibda chop eting
print("\n15. Teskari tartibda:")
print("Asl tartib:   ", numbers)
print("Teskari:      ", numbers[::-1])
print("Teskari sorted:", tuple(sorted(numbers, reverse=True)))

                                                        #SET part5

# 1. QUESTION
s1 = set()
print("1. Bo'sh to'plam:", s1)

# 2. QUESTION
s2 = {10, 25, 7}
print("2. Uchta elementli to'plam:", s2)

# 3.QUESTION
s2.add(42)
print("3. Yangi element qo'shilgandan keyin:", s2)

# 4.QUESTION
print("4. Iltimos 5 ta butun son kiriting (takrorlanishi mumkin, lekin to'plamda faqat noyob qoladi):")
numbers = set()
for i in range(5):
    son = int(input(f"{i+1}-son: "))
    numbers.add(son)
print("Siz kiritgan noyob sonlar to'plami:", numbers)

# 5.QUESTION
print("5. Elementlarni for yordamida:")
for x in numbers:
    print(x)
  
# 6.QUESTION
print("6. Elementlar soni:", len(numbers))
  
# 7. QUESTION
if numbers:
    removed = numbers.pop()   # tasodifiy element o'chiriladi
    print("7. O'chirilgan element:", removed)
    print("Qolgan to'plam:   ", numbers)
else:
    print("To'plam bo'sh edi, o'chirish mumkin emas")
  
# 8. QUESTION
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
union_set = a | b           # yoki a.union(b)
print("8. Birlashtirilgan to'plam:", union_set)
  
# 9. QUESTION
intersection = a & b       
print("9. Kesishma (umumiy elementlar):", intersection)
  
# 10. QUESTION
if union_set:
    random_removed = union_set.pop()
    print("10. Tasodifiy o'chirilgan element:", random_removed)
    print("Qolgan:", union_set)
else:
    print("To'plam bo'sh")
  
# 11. QUESTION
mevalar = {"anor", "olma", "shaftoli", "banan", "uzum", "apelsin"}
print("11. Mevalar (asl):", mevalar)
print("Alifbo tartibida:", sorted(mevalar))
  
# 12. QUESTION
farq = a - b               
print("12. a dan b da yo'q elementlar:", farq)

farq2 = b - a
print("b da bo'lgan, lekin a da yo'q:", farq2)
  
# 13. QUESTION
print("13. Ranglar to'plami orqali chiqarish:")
ranglar = {"qizil", "yashil", "ko'k", "sariq"}
for rang in ranglar:
    print(rang)
  
# 14.QUESTION
print("14. Teskari tartibda (sorted + reverse):")
print("Mevalar teskari:", sorted(mevalar, reverse=True))
  
# 15. QUESTION
mevalar.clear()
print("15. Tozalangandan keyin:", mevalar)
