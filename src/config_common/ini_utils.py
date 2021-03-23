import configparser
from file_common import dir_utils
ini_path = dir_utils.get_app_root_path() + "properties/conf/"
print("=============== 配置文件根目录" + ini_path)


def get_config_by_name(config_name, cf: configparser.ConfigParser = None):
    if not cf:
        cf = configparser.ConfigParser()
    # 读取配置文件
    cf.read(ini_path + config_name, encoding='utf-8')
    # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，每个section由[]包裹，即[section])，并以列表的形式返回
    return cf.sections()


def get_config_by_options(config_name, options, cf: configparser.ConfigParser = None):
    if not cf:
        cf = configparser.ConfigParser()
    cf.read(ini_path + config_name, encoding='utf-8')
    # 获取某个section名为Mysql-Database所对应的键
    return cf.options(options)


def get_config_by_item(config_name, item, cf: configparser.ConfigParser = None):
    if not cf:
        cf = configparser.ConfigParser()
    cf.read(ini_path + config_name, encoding='utf-8')
    # 获取section名为Mysql-Database所对应的全部键值对
    return cf.items(item)


def get_config_by_key(config_name, section_name, key, cf: configparser.ConfigParser = None):
    if not cf:
        cf = configparser.ConfigParser()
        cf.read(ini_path + config_name, encoding='utf-8')
    # 获取[Mysql-Database]中host对应的值
    return cf.get(section_name, key)

# cf.read("E:\Crawler\config.ini")  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块
#
# secs = cf.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，每个section由[]包裹，即[section])，并以列表的形式返回
# print(secs)
#
# options = cf.options("Mysql-Database")  # 获取某个section名为Mysql-Database所对应的键
# print(options)
#
# items = cf.items("Mysql-Database")  # 获取section名为Mysql-Database所对应的全部键值对
# print(items)
#
# host = cf.get("Mysql-Database", "host")  # 获取[Mysql-Database]中host对应的值
# print(host)
