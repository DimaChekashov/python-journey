import multiprocessing
import os
import time

def worker_process(name):
    print(f"Процесс {name} (PID: {os.getpid()}): начинаю работу.")
    time.sleep(2)
    print(f"Процесс {name} (PID: {os.getpid()}): завершаю работу.")
    
def sender(conn):
    print("Отправитель: отправляю данные.")
    conn.send("Привет от отправителя")
    conn.close()
    print("Отправитель: данные отправлены и канал закрыт.")
    
def receiver(conn):
    print("Получатель: ожидаю данные...")
    msg = conn.recv()
    print(f"Получатель: получил \"{msg}\"")
    conn.close()
    print("Получатель: канал закрыт.")

if __name__ == '__main__':
    print(f"Основной процесс (PID: {os.getpid()})")
    
    process1 = multiprocessing.Process(target=worker_process, args=('Worker-A',))
    process2 = multiprocessing.Process(target=worker_process, args=('Worker-B',))
    
    process1.start()
    process2.start()
    
    print("Все дочерние процессы запущены.")
    
    process1.join()
    process2.join()
    
    print("Все дочерние процессы завершили свою работу.")
    
    print('--------------------------------------')
    
    parent_conn, child_conn = multiprocessing.Pipe()
    
    p_sender = multiprocessing.Process(target=sender, args=(parent_conn,))
    p_receiver = multiprocessing.Process(target=receiver, args=(child_conn,))
    
    p_sender.start()
    p_receiver.start()
    
    p_sender.join()
    p_receiver.join()
    
    print('Обмен через Pipe завершен.')