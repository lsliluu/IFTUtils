#!coding=UTF-8
"""
Author: your name
Date: 2021-03-15 16:33:08
LastEditTime: 2021-03-15 17:37:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /IFTUtils/src/response_utils/response_server.py
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import io
import shutil
from config_common.ini_utils import *
from log_common import log
import configparser
import json
from file_common import dir_utils


# noinspection DuplicatedCode,PyGlobalUndefined
class MyHttpHandler(BaseHTTPRequestHandler):

    cf = configparser.ConfigParser()
    app_root_path = dir_utils.get_app_root_path()
    ini_path = app_root_path + "/src/properties/conf/"
    config_name = "interface.ini"
    cf.read(ini_path + config_name, encoding='utf-8')

    def do_get(self):
        r_str = "Hello world,你好！"
        enc = "UTF-8"
        encoded = ''.join(r_str).encode(enc)
        print(self.path)
        print(self.headers)
        f = io.BytesIO()
        f.write(encoded)
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        shutil.copyfileobj(f, self.wfile)

    def do_post(self):
        global resp_content
        path = self.path
        log.wlog("获取url地址:" + path)

        self.cf.read(self.ini_path + self.config_name, encoding='utf-8')
        config_ret = get_config_by_key(
            self.config_name, 'route', 'path', self.cf)
        print('===============================\nroute is: ' + config_ret)
        json_obj = json.loads(config_ret)

        if path not in json_obj:
            print(path + 'not in route')
            r_str = '{"code": "-1","msg":"传入的url地址不符合"}'
        else:
            key = json_obj[path]
            try:
                resp_content = get_config_by_key(
                    self.config_name, 'interface_path', key, self.cf)
                print(resp_content)
            except configparser.NoOptionError:
                error_msg = "配置文件%s中的%s模块未找到key：%s" % (
                    self.config_name, 'interface_path', key)
                print(error_msg)
                # error_dict = {"code": "-1", "msg": error_msg}
                # r_str = json.dumps(error_dict, ensure_ascii=False)
                r_str = resp_content
                print(r_str)
            else:
                # r_str = json.dumps(resp_content, ensure_ascii=False)
                r_str = resp_content
                print(r_str)

        enc = "UTF-8"
        encoded = ''.join(r_str).encode(enc)
        f = io.BytesIO()
        f.write(encoded)
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        shutil.copyfileobj(f, self.wfile)


httpd = HTTPServer(('', 8090), MyHttpHandler)
print("httpServer started on 127.0.0.1,port 8090.....")
httpd.serve_forever()
