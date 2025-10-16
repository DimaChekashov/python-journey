import threading
import time
import requests

def worker(number, sleep_time):
    print(f"Поток {number}: начинаю работу, буду спать {sleep_time} сек.")
    time.sleep(sleep_time)
    print(f"Поток {number}: завершаю работу.")
    
thread1 = threading.Thread(target=worker, args=(1, 2))
thread2 = threading.Thread(target=worker, args=(2, 1))

thread1.start()
thread2.start()

print("Все потоки запущены из основного потока.")

thread1.join()
thread2.join()

print("Все потоки завершили свою работу.")

print('--------------------------------------')

event = threading.Event()

def waiter():
    print("Ожидающий поток: жду события...")
    event.wait()
    print("Ожидающий поток: событие получено, продолжаю работу!")

def setter():
    print("Устанавливающий поток: немного подожду...")
    time.sleep(2)
    print("Устанавливающий поток: устанавливаю событие!")
    event.set()

t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=setter)

t1.start()
t2.start()

t1.join()
t2.join()

print('--------------------------------------')

urls = [
    "https://api.github.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://www.python.org/",
    "https://www.google.com/"
]

def fetch_url(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        duration = time.time() - start_time
        print(f"Загружен {url} за {duration:.2f} сек. Статус: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке {url}: {e}")

threads = []
start_total_time = time.time()

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_total_time = time.time()
print(f"\nВсего времени на загрузку: {end_total_time - start_total_time:.2f} сек.")
