#Задача "Асинхронные силачи"

import asyncio


# Асинхронная функция для имитации поднятия шара Атласа силовиками
async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")

    for i in range(1, 6):
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональная мощности
        print(f"Силач {name} поднял {i} шар")

    print(f"Силач {name} закончил соревнования.")


# Асинхронная функция для запуска соревнования с несколькими участниками
async def start_tournament():
    participants = [("Pasha", 3), ("Denis", 4), ("Apollon", 5)]

    tasks = [start_strongman(name, power) for name, power in participants]

    await asyncio.gather(*tasks)


# Запуск асинхронной функции start_tournament
asyncio.run(start_tournament())