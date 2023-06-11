penjelasan = """
Get method pada dictionary digunakan untuk mencari dengan memasukan key value 
pada argument, Ketika tidak ditemukan key value maka bisa dilakukan penggantian 
optional seperti dibawah ini:
namaDict.get('key value', optional 2).
untuk optional 2 bisa digunakan atau tidak.
"""

player1 = {'xp': 9999, 'level': 100}
player2 = {'xp': 1000, 'level': 10}
player3 = {'xp':0}
player4 = {'xp':8000, 'level':80}
player_database = [player1, player2, player3, player4]

for players in player_database:
    lvl = players.get('level', 0)
    print(f"Level {lvl}")

# Tanpa get method maka akan muncul error keyError
# for players in player_database:
#     lvl = players['level']
#     print(f"Level {lvl}")