import random
import os

num = random.randint(1,10)

tiro = int(input("Escolha un numero de 1 a 10:"))


while True:
    if tiro == num:
        os.system("shutdown /s /t 1") #desligar
        #os.system("shutdown /r /t 1") #reiniciar
    else:
        print("Está vivo!")

    outro = input("Jogar denovo? s ou sim:")

    if outro == "s" or outro == "sim":
        num = random.randint(1,10)
        tiro = int(input("Escolha un numero de 1 a 10:"))
