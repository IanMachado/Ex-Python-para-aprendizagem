from random import randint
from time import sleep
print('\033[33m-=-\033[m' * 20)
print('\033[36mVou pensar em um número entre 0 e 5. Tente advinhar...\033[m')
print('\033[33m-=-\033[m' * 20)
pc = randint(0, 5)

num = int(input("\033[37mEm que número pensei?\033[m "))
print("Processando...")
sleep(2)
if num == pc :
    print(f'\033[32mParabéns, você acertou! Pensei no número {pc}\033[m')

else:
    print(f'\033[31mPensei no número {pc}, você errou!!\033[m')


