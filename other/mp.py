import _thread
import asyncio
import multiprocessing as mp
import os
import random
import time
from multiprocessing import Array, Pipe, Process, Value

from line_profiler import LineProfiler


async def write(p_test_path, p_order):
    try:
        test_str = 'You say that you love rain,but you open your umbrella when it rains.You say that you love the sun,but you find a shadow spot when the sun shines You say that you love the wind,But you close your windows when wind blows...This is why I am afraid;You say that you love me too...You say that you love rain,but you open your umbrella when it rains.You say that you love the sun,but you find a shadow spot when the sun shines You say that you love the wind,But you close your windows when wind blows...This is why I am afraid;You say that you love me too...You say that you love rain,but you open your umbrella when it rains.You say that you love the sun,but you find a shadow spot when the sun shines You say that you love the wind,But you close your windows when wind blows...This is why I am afraid;You say that you love me too...You say that you love rain,but you open your umbrella when it rains.You say that you love the sun,but you find a shadow spot when the sun shines You say that you love the wind,But you close your windows when wind blows...This is why I am afraid;You say that you love me too...\n'
        file_name = "".join(["file", "_", str(p_order).rjust(2, "0")])
        file_path = os.path.join(p_test_path, file_name)
        num = random.randint(2000, 3000)
        test_txt = test_str * num
        with open(file_path, "w") as f:
            f.write(test_txt)
    except Exception as e:
        # p_child_conn.send("sss")
        pass


async def read(p_test_path, p_order):
    try:
        file_name = "".join(["file", "_", str(p_order).rjust(2, "0")])
        file_path = os.path.join(p_test_path, file_name)
        with open(file_path, "r") as f:
            _ = f.read()
    except Exception as e:
        # p_child_conn.send("sss")
        pass


if __name__ == "__main__":
    test_path = r"E:\test_files"
    # p = mp.Pool(mp.cpu_count())

    # s_time = time.time()
    # for i in range(1000):
    #     # write(i) # 7.983128309249878
    #     # p.apply_async(write, (test_path, i))  # 1.250295877456665
    #     # _thread.start_new_thread(write, (test_path, i))
    #     obj = write(test_path, i)
    #     asyncio.run(obj)
    # # child_return = child_conn.recv()
    # # p.close()
    # # p.join()
    # print(time.time() - s_time)
    # # print(child_return)

    s_time = time.time()
    for i in range(1000):
        # read(test_path, i) # 14.414118528366089
        # p.apply_async(read, (test_path, i))  # 3.240330457687378
        # _thread.start_new_thread(read, (test_path, i))
        obj = write(test_path, i)
        asyncio.run(obj)
    # child_return = child_conn.recv()
    # p.close()
    # p.join()
    print(time.time() - s_time)

