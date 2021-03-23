"""
Author: hzf
Date: 2021-03-15 17:02:55
LastEditTime: 2021-03-15 17:36:03
LastEditors: Please set LastEditors
Description: 文件夹工具类
FilePath: /IFTUtils/src/file_common/dir_utils.py
"""
import os


default_project_name = 'IFTUtils'


def get_app_root_path(project_name=None):
    """
    获取当前项目根路径
    :param project_name:
    :return: 根路径
    """
    project_name = default_project_name if project_name is None else project_name
    project_path = os.path.abspath(os.path.dirname(__file__))
    regex = "{}" + os.sep
    root_path = project_path[:project_path.find(regex.format(project_name)) + len(regex.format(project_name))]
    return root_path


def get_file_dir_path():
    dir_path = os.path.abspath(os.path.dirname(__file__))
    print(dir_path)
    return dir_path
