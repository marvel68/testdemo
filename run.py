import multiprocessing


class runner():
    def __init__(self,Logger) -> None:
        self.Logger=Logger
        
    def run_parallel(self,devices_info):
        self.Logger.infolog(devices_info)
        for i in range(5):
            i=i+1
            self.Logger.infolog(i)

    def run(self):
        devices_info = [(1, 1), (2, 2), (3, 3), (4, 4)]
        self.Logger.infolog(devices_info)
        pool = multiprocessing.Pool(5)
        pool.map(self.run_parallel,devices_info)
        pool.close()
        pool.join()
if __name__ == '__main__':
    runner().run()
    print("start")
