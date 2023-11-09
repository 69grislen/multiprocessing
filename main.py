# import threading
#
# def greet(name):
#     print('hello', name)
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=greet, args=('bob',), daemon=True)
#     t2 = threading.Thread(target=greet, args=('alice',), daemon=True)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()


# import datetime
# from threading import Semaphore, Thread
# from time import sleep
#
# s = Semaphore(3)
#
# def semaphore_func(payload: int):
#     s.acquire()
#     now = datetime.datetime.now().strftime('%H:%M:%S')
#     print(f'{now=}, {payload=}')
#     sleep(2)
#     s.release()
#
# threads = [Thread(target=semaphore_func, args=(i,)) for i in range(7)]
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()



# import os
# from multiprocessing import Process
#
# def doubler(number):
#     """
#     Функция умножить на два
#     """
#     result = number * 2
#     proc = os.getpid()
#     proc('{0} doubled to {1} by process id: {2}'.format(number, result, proc))
#
# if __name__ == '__main__':
#     numbers = [5, 10, 15, 20, 25]
#     procs = []
#
#     for index, number in enumerate(numbers):
#         proc = Process(target=doubler, args=(number,))
#         procs.append(proc)
#         proc.start()

    # for proc in procs:
    #     proc.join()



# import multiprocessing, time, random
#
# def worker(num, arr):
#     pid_proc = multiprocessing.current_process().pid
# #     блокируем доступ к массиву из других потоков
#     arr.acquire
#     try:
#         for _ in range(3):
#             #    Имитируем нагрузку, для того, что бы было
#             #    конкуренция доступа к общему ресурсу (очереди)
#             time.sleep(random.uniform(0.01, 0.1))
#             #    последовательно изменяем элемент
#             #    массива на PID процесса 3 раза
#             arr[num.value] = pid_proc
#             # счетчик элементов массива
#             num.value = num.value + 1
#
#     finally:
#         arr.release()
#     # завершаем процесс и разрешаем
#     # доступ к массиву другим процессам
#
# if __name__ == '__main__':
#     num = multiprocessing.Value('i', 0)
#
#     arr = multiprocessing.Array('i', 10)
#
#     procs = []
#     for _ in range(3):
#         proc = multiprocessing.Process(target=worker, args=(num, arr))
#         procs.append(proc)
#         proc.start()
#
#     [proc.join() for proc in procs]
#     print('Вывод результатов')
#     print([i for i in arr if i !=0])
#     [proc.close() for proc in procs]


# from multiprocessing import Pool
#
# def doubler(number):
#     return number * 2
#
# if __name__ == '__main__':
#     numbers = [5, 10, 20]
#     pool = Pool(processes = 3)
#     print(pool.map(doubler, numbers))



