import asyncio
import time

async def greet(name):
    print(f"Hello {name}")
    await asyncio.sleep(1)
    print(f"Goodbye {name}")
    
coro_obj = greet('Dmitry')

print(type(coro_obj))

asyncio.run(coro_obj)

print('--------------------------------------')

async def worker_task(name, delay):
    print(f"Задача {name}: начинаю, буду ждать {delay} сек.")
    await asyncio.sleep(delay)
    print(f"Задача {name}: завершена.")
    return f"Результат от {name}"

async def main_concurrent():
    start_time = time.time()
    print(f"Запуск конкурентных задач в {time.strftime('%X')}")

    results = await asyncio.gather(
        asyncio.create_task(worker_task("A", 2)),
        asyncio.create_task(worker_task("B", 1)),
        asyncio.create_task(worker_task("C", 3))
    )

    print(f"\nВсе задачи завершены за {time.time() - start_time:.2f} сек.")
    print(f"Результаты: {results}")

if __name__ == "__main__":
    asyncio.run(main_concurrent())