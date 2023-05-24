import random

listKarakter6Star = ["All for One", "The Best Assassin", "Immortal One"]
listKarakter5Star = ["Keqing", "Ayaka", "Ganyu", "Hu Tao", 
                     "Raiden", "Yoimiya", "Yae Miko", "Venti"
                     "Shenhe", "Xiao", "Yelan", "Zhongli"]

listKarakter4Star = ["Sara", "Razor", "Lisa", "Shinobu",
                     "Dori", "Beidou", "Candace", "Amber",
                     "Xingqiu", "Bennett", "Xiangling", "Ningguang"]

listItem3Star = ["Sword", "Spear", "Bow", "Gun",
                 "Shield", "Dagger", "Knife", "Ballon",
                 "Ball", "Shoes", "Jacket", "Hair"]

bobot = [10] * len(listKarakter4Star) + [50] * len(listItem3Star) + [5] * len(listKarakter5Star) + [1] * len(listKarakter6Star)
pilihan = listKarakter4Star + listItem3Star + listKarakter5Star + listKarakter6Star

def mesin_gacha():
    return random.choices(pilihan, weights=bobot, k=10)


hasil = []
karakter6Star = 0
karakter5Star = 0
karakter4Star = 0
item3Star = 0
total = 0

print("1 = 10 x pull\n")
input_user = int(input("Masukan pull: "))
if input_user >= 0 and input_user <= 1000:
    for x in range(input_user):
        gacha = mesin_gacha()
        hasil.append(gacha)
    
    for x in range(len(hasil)):
        for y in hasil[x]:
            total +=1
            if y in listKarakter6Star:
                karakter6Star+=1
            elif y in listKarakter5Star:
                karakter5Star+=1
            elif y in listKarakter4Star:
                karakter4Star+=1
            elif y in listItem3Star:
                item3Star+=1
    print(f"""
Anda mendapatkan dari {total} pull:   
{karakter6Star} karakter 6 star,
{karakter5Star} karakter 5 star,
{karakter4Star} karakter 4 star, dan
{item3Star} item 3 star.               
    """)
else:
    print("Pull dari 0 - 1000!")