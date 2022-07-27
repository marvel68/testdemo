import multiprocessing
import threading

class runner():
    def __init__(self,Logger) -> None:
        self.Logger=Logger
        
    def run_parallel(self):
        self.Logger.infolog(self.devices_info)
        for i in range(5):
            i=i+1
            self.Logger.infolog(i)

    def run(self):
        self.devices_info = [(1, 1), (2, 2), (3, 3), (4, 4)]
        self.Logger.infolog(self.devices_info)
        while threading.activeCount() < 8: #这个8是最大线程数量
            threading.Thread(target=self.run_parallel).start()
if __name__ == '__main__':
    runner().run()
    print("start")
