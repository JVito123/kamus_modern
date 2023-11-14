# Kejutkan teman-temanmu!

import random

hobi = input("masukkan hobimu:")
peliharaan = input("masukkan peliharaanmu:")
proyek = input("masukkan proyek favoritmu:")
fav_menu = input("masukkan menu favoritmu:")

fakta_random = [hobi, peliharaan, proyek, fav_menu]
print(random.choice(fakta_random))
