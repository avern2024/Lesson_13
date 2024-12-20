import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for ball in range(1, 6):
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональная силе
        print(f'Силач {name} поднял {ball} шар')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    # Создаем задачи для трех силачей
    tasks = [
        start_strongman('Pasha', 3),
        start_strongman('Denis', 4),
        start_strongman('Apollon', 5)
    ]

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(start_tournament())
