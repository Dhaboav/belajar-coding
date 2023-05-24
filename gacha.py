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

bobot = [3] * len(listKarakter4Star) + [10] * len(listItem3Star) + [0.01] * len(listKarakter5Star)
pilihan = listKarakter4Star + listItem3Star + listKarakter5Star

pity = 0
def mesin_gacha():
    global pity
    if pity < 99:
        if random.random() < 0.001:
            pity = 0
            return random.choice(listKarakter6Star)
        else:
            pity+=1
            return random.choices(pilihan, weights=bobot, k=10)
        
    elif pity == 99:
        pity = 0
        return random.choice(listKarakter6Star)
            
    
count6Star = 0
other = 0
for x in range(10):
    gacha = mesin_gacha()
    if gacha in listKarakter6Star:
        count6Star+=1
        print(gacha)
    else:
        other+=1

print(count6Star, other)