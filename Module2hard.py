import os
os.system('CLS')
os.system('COLOR 1e')
os.system('VER')
#Задание "Слишком древний шифр":
#Все пароли для чисел от 3 до 20 (для сверки):
#3 - 12
#4 - 13
#5 - 1423
#6 - 121524
#7 - 162534
#8 - 13172635
#9 - 1218273645
#10 - 141923283746
#11 - 11029384756
#12 - 12131511124210394857
#13 - 112211310495867
#14 - 1611325212343114105968
#15 - 1214114232133124115106978
#16 - 1317115262143531341251161079
#17 - 11621531441351261171089
#18 - 12151811724272163631545414513612711810
#19 - 118217316415514613712811910
#20 - 13141119923282183731746416515614713812911

import random

random_number = random.randint(3, 20)
print(f"В первом поле из камней выложено число: {random_number}\n")

number_pairs = []
for i in range(1, 21):
    for j in range(1, 21):
        if random_number % (i + j)  == 0 and i < j:
            number_pairs.append((i, j))

print("СРОЧНО! Введи пароль:\n")
password = ""
for pair in number_pairs:
    password += "".join(map(str, pair))
print(password)