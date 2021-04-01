import logging
import os
import time
from os import makedirs
from file_common import dir_utils


# noinspection PyShadowingBuiltins
def wlog(str, loglevel='info'):
    # print(datetime.datetime.now().strftime('%Y%m%d%H%M%S.%f'))
    # 创建一个logger
    logger = logging.getLogger('')
    # 设置logger的等级，大于等于这个等级的信息会被输出，其他会被忽略
    logger.setLevel(logging.DEBUG)

    # Handler是英文翻译为处理者，用于输出到不同的地方：Stream为控制台，File为文件
    # 以下创建的是输出到文件的handler，并把等级设为DEBUG
    # 当前文件的路径
    pwd = dir_utils.get_app_root_path()
    # 当前文件的父路径
    # father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
    makedirs(pwd + os.sep + "Log", exist_ok=True)  # 如果不存在目录创建目录
    fh = logging.FileHandler(pwd + os.sep + "Log" + os.sep + "test_" + time.strftime('%Y%m%d') + ".log")
    fh.setLevel(logging.DEBUG)
    # 以下创建的是输出到控制台的handler，并把等级设为DEBUG
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    # 下面指定了handler的信息输出格式，其中asctime,name,levelname，message都是logging的关键字
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    # 把Handler加入到logger中，可理解为给处理者在logger中安排了职位
    logger.addHandler(fh)
    logger.addHandler(sh)

    if loglevel == 'error':
        logger.error(str)
    else:
        logger.info(str)

    logger.removeHandler(sh)
    logger.removeHandler(fh)
    # logger.error('error:数据库插入错误！')
