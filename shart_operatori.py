# # son1=int(input("son kirgazing! "))
# # son2=int(input("son kirgazing! "))
# # son3=int(input("son kirgazing! "))
# # if son1>son2 and son1>son3:
# #     print(f"{son1} bu son eng kattasi")
# # elif son2>son1 and son2>son3:
# #     print(f"{son2} bu son eng kattasi")
# # elif son3>son2 and son3>son1:
# #     print(f"{son3} bu son eng kattasi")
# # else:
# #     print("xato kiritilgan")

# # ikki sondi kv ildizni topish

# # import math as mp
# # a=int(input("son kirgazing! "))
# # b=int(input("son kirgazing! "))
# # c=int(input("son kirgazing! "))
# # D=(b**2)-(4*a*c)
# # if D>0:
# #     print("ko'p yechim"
# #           f"""
# #           {(-b+(mp.sqrt(D)))/2*a} x1ning qiymati
# #           {(-b-(mp.sqrt(D)))/2*a} x2ning qiymati""")
# # elif D==0:
# #     print("bitta yechimga ega"
# #           f"{(-b+(mp.sqrt(D)))/2*a} x1ning qiymati")
# # else:
# #     print("yechimga ega emas")



# #istemolni topish

# # c=int(input(" qiymatni kirgazing "))

# # if c>200:
# #     b=c%200
# #     if  b<200:
# #         e=c-b    #200 kv dan oshiqchasini topish 
# #         q=e*100  #200 kv dan oshiqchani summasi
# #         c1=c-e
# #         q1=c1*600 #200kv gacha bo'lgan qiymat summasi
# #         Q=q+q1
# #         print(Q)




# son1=int(input("son kirgazing! "))
# son2=int(input("son kirgazing! "))
# summ=[]
# for a in range(son1,son2): 
#     if a%2==0 and a%3==0:
#         summ.append(a)
# print(sum(summ))


# # unli xariflarni topish
# ism=input("ismizni kiriting!")
# unlilar=("a","o","u","e","i")
# son=[]
# for a in ism:
#     if a in unlilar:   
#         print(a)


# # isimdi uzunini chiqarish
# uzun=[]
# uzun1=[0]
# uzun2=[]
# for Isim in range(3):
#     isim=input("ismizni yozing")
#     for sprate in isim:
#           uzun.append(sprate)
#           uzun1+=1
# print(uzun)
# print(uzun1)



# # ikkiga bo'linadigon
# a=1
# while a<11:
#     print(f"{a*2} 2ga bolinadi")
#     a+=1









                                            #TOPSHIRIQLAR

#Raqamning 2 va 3 ga bo'linadigan bo'lishini tekshirish
n = int(input("Son kiriting: "))
if n % 2 == 0 and n % 3 == 0:
    print(f"{n} 2 ga ham, 3 ga ham bo'linadi")
else:
    print(f"{n} 2 ga yoki 3 ga bo'linmaydi")


#Harorat bo'yicha xabar
harorat = int(input("Haroratni kiriting: "))
if harorat > 30:
    print("Issiq")
elif harorat < 10:
    print("Sovuq")
else:
    print("Iliq")


#Kabisa yilini tekshirish
yil = int(input("Yilni kiriting: "))
if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    print(f"{yil} - kabisa yili")
else:
    print(f"{yil} - kabisa yili emas")


#Kiritilgan satr belgilarni alohida chop etish
matn = input("Matn kiriting: ")
for belgi in matn:
    print(belgi)


#Raqamning dastlabki 10 ko'paytmasi
son = int(input("Son kiriting: "))
for i in range(1, 11):
    print(f"{son} x {i} = {son * i}")


#1 dan 100 gacha sonlar yig'indisi
yigindi = 0
for i in range(1, 101):
    yigindi += i
print("1 dan 100 gacha yig'indi:", yigindi)


#1 dan 50 gacha toq sonlar
for i in range(1, 51, 2):
    print(i, end=" ")


#Ismlar ro'yxatini chop etish
ismlar = ["Ali", "Vali", "Sardor", "Nodir", "Gulnoza"]
for ism in ismlar:
    print(ism)


#Faktorial hisoblash (for tsikli bilan)
n = int(input("Faktorialini hisoblash uchun son kiriting: "))
fakt = 1
for i in range(1, n + 1):
    fakt *= i
print(f"{n}! = {fakt}")


#10 dan 1 gacha teskari tartibda chop etish
for i in range(10, 0, -1):
    print(i)


#1 dan 5 gacha bo'lgan raqamlarni chop etish
i = 1
while i <= 5:
    print(i)
    i += 1


#10 dan 1 gacha teskari tartibda chop etish
i = 10
while i >= 1:
    print(i)
    i -= 1


#1 dan 50 gacha juft raqamlarni chop etish
i = 2
while i <= 50:
    print(i)
    i += 2


#1 dan 50 gacha sonlar yig'indisi
yigindi = 0
i = 1
while i <= 50:
    yigindi += i
    i += 1
print("1 dan 50 gacha yig'indi:", yigindi)


#5 ning ko'paytma jadvali (5 x 1 dan 5 x 10 gacha)
i = 1
while i <= 10:
    print(f"5 x {i} = {5 * i}")
    i += 1


#"to'xtat" so'zi kiritilmaguncha so'rash
matn = ""
while matn.lower() != "to'xtat":
    matn = input("So'z kiriting (to'xtatish uchun 'to'xtat' deb yozing): ")
    print("Siz kiritdingiz:", matn)
print("Dastur to'xtadi.")


# butun son sifatida qabul qilib, matematik yo'l bilan raqamlarni ajratish
raqam = int(input("Raqam kiriting (yana bir marta): "))
print("Raqamning raqamlari (teskari tartibda):")
while raqam > 0:
    oxirgi_raqam = raqam % 10       
    print(oxirgi_raqam)
    raqam = raqam // 10          


                                            #math funksiyasi
import math as mp
a=int(input("son kiriting "))
if (mp.sqrt((3*((mp.cos(2*a))**2))))!=0:
        b=((1-mp.cos(4*a)+(mp.sin(2*a))**2))/(mp.sqrt((3*((mp.cos(2*a))**2))))
        print(b)
else:
        print("xato")
