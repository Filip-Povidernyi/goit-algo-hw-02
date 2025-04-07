from queue import Queue
from random import uniform
import time


req_queue = Queue()

req_count = 0


def generate_request() -> bool:

    global req_count
    request = f"Request {req_count}"
    req_queue.put(request)
    req_count += 1
    print(f"Generated: {request}")
    if req_count == 10:
        return False
    return True


def process_request() -> None:
    if not req_queue.empty():
        request = req_queue.get()
        print(f"Request {request} in process...")
        time.sleep(uniform(0.5, 1.5))  # Імітація часу обробки
        print(f"Processed: {request}")
    else:
        print("No requests in queue.")


def main() -> None:
    gen_req = True
    while gen_req:
        try:
            print("Requests process")
            gen_req = generate_request()
            time.sleep(uniform(0.5, 1.5))  # Затримка між генерацією
            process_request()
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()
