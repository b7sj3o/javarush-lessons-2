import time
import threading


# def test(num):
#     time.sleep(1)
#     print(f"ok: {num}")
#
#
# start = time.time()
#
# threads = []
#
# for i in range(5):
#     thread = threading.Thread(target=test, args=(i, ))
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
#
#
# end = time.time()
# print(f"Це зайняло: {end-start} секунд")


#
# def greet(name):
#     print(f"Hello {name}")
#
#
# thread = threading.Timer(3.0, greet, ("Alice", ))
# thread.start()


# local_data  = threading.local()
#
# def process_data():
#     local_data.value = threading.current_thread().name
#     print(f'Value in {threading.current_thread().name}: {local_data.value}')
#
# for i in range(5):
#     t = threading.Thread(target=process_data)
#     t.start()

def hdr(t):
    print("\n" + "=" * 60 + f"\n{t}\n" + "=" * 60)

def demo_gil():
    hdr("12. GIL: чи прискорять потоки обчислення?")

    def cpu(n=20_000_000):
        x = 0
        for i in range(n):
            x += i
        return x

    t0 = time.perf_counter()
    cpu(); cpu()

    print(f"  послідовно: {time.perf_counter() - t0:.2f} c")

    t0 = time.perf_counter()
    ts = [threading.Thread(target=cpu) for _ in range(2)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print(f"  2 потоки:   {time.perf_counter() - t0:.2f} c  ← виграшу немає, GIL")
    print("  для обчислень: multiprocessing / ProcessPoolExecutor")

demo_gil()