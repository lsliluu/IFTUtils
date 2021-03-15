'''
Author: your name
Date: 2021-03-15 16:30:58
LastEditTime: 2021-03-15 17:16:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /IFTUtils/src/main.py
'''
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    from file_common.dir_utils import get_app_root_path
    print(get_app_root_path())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
