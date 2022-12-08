# coding=utf-8
import logging
import os
import datetime


# logging只是个模块，需要给它配置后logging.debug('test')才能使用
class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()  # 一个对象
        self.logger.setLevel(logging.DEBUG)  # 设置一个等级，logger文件里面如果要把文件输出就需要一个地方给它，输出的东西在Java里面称为流媒体，需要把输出的流传输到控制台
        # 创建一个handler控制台输出日志
        # console = logging.StreamHandler()  # 创建了一个流对象
        # logger.addHandler(console)  # 有了往控制台输出文件的流

        # 文件名，创建一个handler，用于写入日志文件
        # 拿到当前文件,并拼接
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, "logs")
        # log_file = datetime.datetime.now().strftime("%y-%m-%d %H%M") + ".log" # 具体到时间
        log_file = datetime.datetime.now().strftime("%y-%m-%d") + ".log"
        log_name = log_dir + "/" + log_file
        print(log_name)

        # 文件输出日志
        self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')  # 追加模式，日志输出到log_name
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s ---->%(funcName)s %(lineno)d %(levelname)s: ---->%(message)s')  # 定义handler的输出格式
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)  # 给logger添加handler

        # logging.debug('test1234')
        # self.logger.removeHandler(self.file_handle)  # 在记录日志之后移除句柄
        # self.file_handle.close()  # 关闭打开的文件

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)  # 在记录日志之后移除句柄
        self.file_handle.close()  # 关闭打开的文件


if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('test')
    user.close_handle()
