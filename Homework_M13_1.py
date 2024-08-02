import asyncio


async def start_strongmen(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        sleep_ = asyncio.sleep(5 / power)
        await sleep_
        print(f'Силач {name} поднял шар №{i+1}')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    strongmen_1 = asyncio.create_task(start_strongmen('Pasha', 4))
    strongmen_2 = asyncio.create_task(start_strongmen('Andre', 3))
    strongmen_3 = asyncio.create_task(start_strongmen('Apollo', 5))
    await strongmen_1
    await strongmen_2
    await strongmen_3

asyncio.run(start_tournament())
