import random

pw = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
p = int(input("Berapa panjang password yang Anda inginkan?"))
hasil = ''

for i in range(p):
    hasil += random.choice(pw)

print("Password kamu:", hasil)