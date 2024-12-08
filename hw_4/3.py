from multiprocessing import Process, Queue
import logging
import time
import codecs


log = logging.getLogger(__name__)
FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(filename="artifacts/3.txt", level=logging.INFO, format=FORMAT)


def worker_a(input_queue, a_queue, b_queue):
    last_send_time = time.time() - 5.1
    while True:
        if not a_queue.empty() and time.time() - last_send_time >= 5.0:
            i_lower = a_queue.get()
            last_send_time = time.time()
            log.info(f"Send message {i_lower} to b queue")
            b_queue.put(i_lower)
        elif not input_queue.empty():
            i = input_queue.get()
            i_lower = i.lower()
            a_queue.put(i_lower)
        continue


def worker_b(output_queue, b_queue):
    while True:
        str_to_encode = b_queue.get()
        encoded_str = codecs.encode(str_to_encode, 'rot_13')
        print(f"Encoded str: {encoded_str}")
        output_queue.put(encoded_str)


def main():
    input_queue = Queue()
    output_queue = Queue()
    a_queue = Queue()
    b_queue = Queue()

    Process(target=worker_a, args=(input_queue, a_queue, b_queue)).start()
    Process(target=worker_b, args=(output_queue, b_queue)).start()
    while True:
        str_to_send = input()
        input_queue.put(str_to_send)


if __name__ == "__main__":
    main()
