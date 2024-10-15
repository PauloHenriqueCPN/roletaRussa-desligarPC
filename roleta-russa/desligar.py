import random
import os
import time

while True:
    num = random.randint(1,10)

    tiro = int(input("Escolha um numero de 1 a 10:"))
    
    if tiro == num:
        #os.system("shutdown /s /t 1") # desligar
        os.system("shutdown /r /t 1") # reiniciar
        #print("perdeu") # modo facil
    
    elif tiro > 10 or tiro < 1:
        print("Não brinque com coisa séria")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        time.sleep(1)
        os.system("shutdown /s /t 1")
        #print("perdeu") # modo facil

    else:
        print("Está vivo!")

    outro = input("Jogar denovo? s ou sim:")

    if outro == "s" or outro == "sim":
        True
    else:
        print("Você não tem escolha")
