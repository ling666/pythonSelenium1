# coding=utf-8
import logging

# logging只是个模块，需要给它配置后logging.debug('test')才能使用
logger = logging.getLogger()  # 一个对象
logger.setLevel(logging.DEBUG)  # 设置一个等级，logger文件里面如果要把文件输出就需要一个地方给它，输出的东西在Java里面称为流媒体，需要把输出的流传输到控制台
console = logging.StreamHandler()  # 创建了一个流对象
logger.addHandler(console)  # 有了往控制台输出文件的流
logging.debug('test')
console.close()  # consle和logger要删除掉
logger.removeHandler(console)
