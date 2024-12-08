import logging
import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


def integrate(f=math.pow, a=0, b=math.pi, init_index=0, step_index=30000000):
    acc = 0
    step = (b - a) / step_index
    for i in range(init_index, init_index + step_index):
        acc += f(a + i * step, 2) * step
    return acc


if __name__ == "__main__":
    logging.basicConfig(filename='artifacts/2.txt', level=logging.INFO)
    log = logging.getLogger(__name__)

    for n_job in range(1, 25):
        integrate_args = [
            0,
            30000000,
            6000000,
            90000000,
            120000000,
            150000000,
            180000000,
            210000000,
        ]

        start = time.time()
        log.info(f"Running ThreadPoolExecutor with {n_job} jobs\n")
        with ThreadPoolExecutor(max_workers=n_job) as executor:
            futures = []
            for integrate_arg in integrate_args:
                futures.append(executor.submit(integrate, init_index=integrate_arg))
            res = 0
            for future in as_completed(futures):
                res += future.result()

        thread_time = time.time() - start


        start = time.time()
        log.info(f"Running ProcessPoolExecutor with {n_job} jobs\n")
        with ProcessPoolExecutor(max_workers=n_job) as executor:
            futures = []
            for integrate_arg in integrate_args:
                futures.append(executor.submit(integrate, init_index=integrate_arg))
            res = 0
            for future in as_completed(futures):
                res += future.result()

        proc_time = time.time() - start
        log.info(f"ThreadPoolExecutor time: {thread_time}, ProcessPoolExecutor time: {proc_time} with {n_job} jobs\n")
