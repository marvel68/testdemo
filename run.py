import logging
import multiprocessing
from logging.handlers import QueueHandler

from common.logger import Logger

def run_parallel(devices_info):
    Logger.info(devices_info)
    for i in range(5):
        i=i+1
        Logger.info(i)

def run():
    devices_info = [(1, 1), (2, 2), (3, 3), (4, 4)]
    Logger.info(devices_info)
    pool = multiprocessing.Pool(5)
    pool.map(run_parallel, devices_info)
    pool.close()
    pool.join()
if __name__ == '__main__':
    run()
    print("start")
