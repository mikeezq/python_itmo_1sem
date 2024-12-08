import time
from multiprocessing import Process
from threading import Thread


def fib(n):
    if n <= 0:
        raise ValueError("n must be positive")
    if n <= 2:
        return 1
    a, b = 1, 1
    for i in range(3, n + 1):
        b, a = a + b, b
    return b


if __name__ == "__main__":
    count = 10
    start = time.time()

    threads = []
    for i in range(count):
        thread = Thread(target=fib, args=(800000,))
        thread.start()
        threads.append(thread)

    for i in range(count):
        threads[i].join()

    print(f"Threads run time: {time.time() - start}")


    start = time.time()

    processes = []
    for i in range(count):
        proc = Process(target=fib, args=(800000,))
        proc.start()
        processes.append(proc)

    for i in range(count):
        processes[i].join()

    print(f"Processes run time: {time.time() - start}")