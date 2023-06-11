import random

random_machine = random.randint(1, 10)
menebak  = 0
batas_menebak = 3

print("Program tebakan angka 1-10")
while menebak < batas_menebak:
    user_input = int(input("Masukan angka tebakan anda: "))
    if user_input == random_machine:
        print("--> Selamat anda berhasil :)")
        break
    elif user_input > random_machine:
        print("--> Tebakan terlalu tinggi")
        menebak+=1
    elif user_input < random_machine:
        print("--> Tebakan terlalu rendah")
        menebak+=1

else:
    print("--> Anda kalah!")