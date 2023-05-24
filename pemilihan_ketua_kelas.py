import random

list_nama_calket = ["Falencia", "Amuro", "Randy", "Conan", 
                    "Aji", "Sanada", "Sasuke", "Naruto", 
                    "Kuro", "Shiro", "Hanabi", "Andy",
                    "Shery", "Holmes", "Genta", "Kosuke",
                    "Anne", "Marissa", "Arif", "Maruyuma",
                    "Budi", "Ribka", "Furuya", "Cindy"]

ketua_terpilih = random.choice(list_nama_calket)
print(f'Selamat kepada {ketua_terpilih} yang telah terpilih dari {len(list_nama_calket)} calon ketua.')