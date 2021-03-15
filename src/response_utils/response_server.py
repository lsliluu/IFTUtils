#!coding=UTF-8
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import io
import shutil
import urllib
import log
from utils.configutils import *
import configparser
import json


# import pymysql

class MyHttpHandler(BaseHTTPRequestHandler):

    # conn = pymysql.connect("192.168.153.130", "mysql", "mysql", "dzqd", charset='utf8')
    # # 使用cursor()方法获取操作游标
    # cursor = conn.cursor()

    cf = configparser.ConfigParser()
    ini_path = "/home/hzf/workspace/VSCodeWorkspace/interface_test/app/properties/conf/"
    config_name = "interface.ini"
    cf.read(ini_path + config_name, encoding='utf-8')

    def do_GET(self):
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

    def do_POST(self):
        path = self.path
        r_str = ""
        log.wlog("获取url地址:" + path)

        self.cf.read(self.ini_path + self.config_name, encoding='utf-8')
        config_ret = get_config_by_key(
            self.config_name, 'route', 'path', self.cf)
        print('===============================\nroute is: ' + config_ret)
        json_obj = json.loads(config_ret)

        if (path not in json_obj):
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
                error_dict = {"code": "-1", "msg": error_msg}
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

        # # if (path != "/cloud/rphone/upPhoneInfo"):
        # if (path == "/cdp/taskexecute/getTask"):
        #     # 佳丽
        #     # resp_content =  {"code":"0","msg":"","appId":"","respTime":"1562168411837","data":{"phoneNo":"15960166413","strategyId":"3286","groupId":"8698","tasksetId":"24896","tasksetInstanceName":"2019-07-03 23:40:00","channel":"32","testsrl":"276556515","pauseTime":0,"bamNormalModel":{"objectId":"742443","testType":"32","modelName":"本地化_集团APP_积分查询","modeldesc":"","runflow":"","enabled":"1","remainTime":"0","carrier":"中国移动","province":"福建","brand":"全球通","channel":"32","getValueType":"0","note":"","func":"0","isbalance":"0","balance":"0.0","testplatform":"集团手厅","testsystem":"云测APP","overtime":"0","bamNormalModelDetailParas":[{"stepNo":1.0,"operateType":"49","stepType":"0","target":"com.greenpoint.android.mc10086.activity","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":1.1,"operateType":"21","stepType":"0","target":"fix\u003d5","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":2.0,"operateType":"43","stepType":"0","target":"com.greenpoint.android.mc10086.activity/com.leadeon.cmcc.base.StartPageActivity","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":2.3,"operateType":"21","stepType":"0","target":"fix\u003d25","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":5.0,"operateType":"5","stepType":"0","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":5.3,"operateType":"21","stepType":"0","target":"fix\u003d3","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":6.0,"operateType":"2","stepType":"0","target":"text\u003d我的","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":6.1,"operateType":"21","stepType":"0","target":"fix\u003d3","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":6.2,"operateType":"2","stepType":"0","target":"text\u003d登录","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":7.0,"operateType":"3","stepType":"0","target":"resourceId\u003dcom.greenpoint.android.mc10086.activity:id/user_phoneno_edt","postParam":"15960166413","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":8.0,"operateType":"45","stepType":"0","target":"resourceId\u003dcom.greenpoint.android.mc10086.activity:id/user_login_smspassword_edt","postParam":"resourceId\u003dcom.greenpoint.android.mc10086.activity:id/login_checksms_btn#sms#","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":9.0,"operateType":"2","stepType":"0","target":"resourceId\u003dcom.greenpoint.android.mc10086.activity:id/one_key_login_btn","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":9.1,"operateType":"21","stepType":"0","target":"fix\u003d1","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":10.0,"operateType":"4","timerToken":"积分","stepType":"0","target":"970,1820","succstr1":"积分","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"3","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":11.1,"operateType":"21","stepType":"0","target":"fix\u003d3","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":12.0,"operateType":"49","stepType":"0","target":"com.greenpoint.android.mc10086.activity","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""}]},"getSmskeyconfigs":[{"id":4706,"carrier":"中国移动","province":"福建","brand":"全球通","beforekeywords":"短信验证码是：","afterkeywords":",欢迎使用","keywordslen":6,"symbol":"+","type":5,"note":"集团APP登录","channelname":"真机APP","extType":0},{"id":5143,"carrier":"中国移动","province":"福建","brand":"全球通","beforekeywords":"短信密码为：","afterkeywords":"，请在5分钟","keywordslen":6,"symbol":"+","type":5,"channelname":"真机APP","extType":0},{"id":5562,"carrier":"中国移动","province":"福建","brand":"全球通","beforekeywords":"验证码是：","afterkeywords":"，请在5分钟","keywordslen":6,"symbol":"+","type":5,"note":"省APP登录","channelname":"真机APP","extType":0}]}}
        #     # 锐哥
        #     resp_content = {"code": "0", "msg": "", "appId": "", "respTime": "1562905241075",
        #                     "data": {"phoneNo": "15859091580", "strategyId": "3286", "groupId": "8698",
        #                              "tasksetId": "24922", "tasksetInstanceName": "2019-07-12 12:20:00",
        #                              "channel": "32", "testsrl": "277859806", "pauseTime": 0,
        #                              "bamNormalModel": {"objectId": "742386", "testType": "32",
        #                                                 "modelName": "本地化_集团APP_实时话费", "modeldesc": "", "runflow": "",
        #                                                 "enabled": "1", "remainTime": "0", "carrier": "中国移动",
        #                                                 "province": "广西", "brand": "全球通", "channel": "32",
        #                                                 "getValueType": "0", "note": "", "func": "0", "isbalance": "0",
        #                                                 "balance": "0.0", "testplatform": "集团手厅", "testsystem": "云测APP",
        #                                                 "overtime": "0", "bamNormalModelDetailParas": [
        #                                      {"stepNo": 1.0, "operateType": "49", "stepType": "0",
        #                                       "target": "com.greenpoint.android.mc10086.activity", "enabled": "1",
        #                                       "verify": "", "smsVerify": "", "utf8encode": "", "failRetry": "",
        #                                       "retryCount": "1", "checkPoint": "", "tokenType": "0", "methodType": "1",
        #                                       "carrierType": "0", "sleepTime": "0", "buyfee": "0", "stepfun": "",
        #                                       "urlGetType": "", "recordType": "", "recordBegin": "",
        #                                       "recordDuration": "", "speech": "", "play": "", "callDuration": ""},
        #                                      {"stepNo": 1.1, "operateType": "21", "stepType": "0",
        #                                       "target": "fix\u003d8", "enabled": "1", "verify": "", "smsVerify": "",
        #                                       "utf8encode": "", "failRetry": "", "retryCount": "1", "checkPoint": "",
        #                                       "tokenType": "0", "methodType": "1", "carrierType": "0", "sleepTime": "0",
        #                                       "buyfee": "0", "stepfun": "", "urlGetType": "", "recordType": "",
        #                                       "recordBegin": "", "recordDuration": "", "speech": "", "play": "",
        #                                       "callDuration": ""}, {"stepNo": 2.0, "operateType": "43", "stepType": "0",
        #                                                             "target": "com.greenpoint.android.mc10086.activity/com.leadeon.cmcc.base.StartPageActivity",
        #                                                             "enabled": "1", "verify": "", "smsVerify": "",
        #                                                             "utf8encode": "", "failRetry": "",
        #                                                             "retryCount": "1", "checkPoint": "",
        #                                                             "tokenType": "0", "methodType": "1",
        #                                                             "carrierType": "0", "sleepTime": "0", "buyfee": "0",
        #                                                             "stepfun": "", "urlGetType": "", "recordType": "",
        #                                                             "recordBegin": "", "recordDuration": "",
        #                                                             "speech": "", "play": "", "callDuration": ""},
        #                                      {"stepNo": 2.1, "operateType": "21", "stepType": "0",
        #                                       "target": "fix\u003d25", "enabled": "1", "verify": "", "smsVerify": "",
        #                                       "utf8encode": "", "failRetry": "", "retryCount": "1", "checkPoint": "",
        #                                       "tokenType": "0", "methodType": "1", "carrierType": "0", "sleepTime": "0",
        #                                       "buyfee": "0", "stepfun": "", "urlGetType": "", "recordType": "",
        #                                       "recordBegin": "", "recordDuration": "", "speech": "", "play": "",
        #                                       "callDuration": ""}, {"stepNo": 2.8, "operateType": "11", "stepType": "0",
        #                                                             "target": "text\u003d以后再说", "enabled": "1",
        #                                                             "verify": "", "smsVerify": "", "utf8encode": "",
        #                                                             "failRetry": "", "retryCount": "1",
        #                                                             "checkPoint": "", "tokenType": "0",
        #                                                             "methodType": "1", "carrierType": "0",
        #                                                             "sleepTime": "0", "buyfee": "0", "stepfun": "",
        #                                                             "urlGetType": "", "recordType": "",
        #                                                             "recordBegin": "", "recordDuration": "",
        #                                                             "speech": "", "play": "", "callDuration": ""},
        #                                      {"stepNo": 3.0, "operateType": "5", "stepType": "0", "enabled": "1",
        #                                       "verify": "", "smsVerify": "", "utf8encode": "", "failRetry": "",
        #                                       "retryCount": "1", "checkPoint": "", "tokenType": "0", "methodType": "1",
        #                                       "carrierType": "0", "sleepTime": "0", "buyfee": "0", "stepfun": "",
        #                                       "urlGetType": "", "recordType": "", "recordBegin": "",
        #                                       "recordDuration": "", "speech": "", "play": "", "callDuration": ""},
        #                                      {"stepNo": 4.1, "operateType": "21", "stepType": "0",
        #                                       "target": "fix\u003d5", "enabled": "1", "verify": "", "smsVerify": "",
        #                                       "utf8encode": "", "failRetry": "", "retryCount": "1", "checkPoint": "",
        #                                       "tokenType": "0", "methodType": "1", "carrierType": "0", "sleepTime": "0",
        #                                       "buyfee": "0", "stepfun": "", "urlGetType": "", "recordType": "",
        #                                       "recordBegin": "", "recordDuration": "", "speech": "", "play": "",
        #                                       "callDuration": ""}, {"stepNo": 5.0, "operateType": "2", "stepType": "0",
        #                                                             "target": "text\u003d我的", "enabled": "1",
        #                                                             "verify": "", "smsVerify": "", "utf8encode": "",
        #                                                             "failRetry": "", "retryCount": "1",
        #                                                             "checkPoint": "", "tokenType": "0",
        #                                                             "methodType": "1", "carrierType": "0",
        #                                                             "sleepTime": "0", "buyfee": "0", "stepfun": "",
        #                                                             "urlGetType": "", "recordType": "",
        #                                                             "recordBegin": "", "recordDuration": "",
        #                                                             "speech": "", "play": "", "callDuration": ""},
        #                                      {"stepNo": 5.4, "operateType": "21", "stepType": "0",
        #                                       "target": "fix\u003d3", "enabled": "1", "verify": "", "smsVerify": "",
        #                                       "utf8encode": "", "failRetry": "", "retryCount": "1", "checkPoint": "",
        #                                       "tokenType": "0", "methodType": "1", "carrierType": "0", "sleepTime": "0",
        #                                       "buyfee": "0", "stepfun": "", "urlGetType": "", "recordType": "",
        #                                       "recordBegin": "", "recordDuration": "", "speech": "", "play": "",
        #                                       "callDuration": ""},
        #                                      {"stepNo": 5.5, "operateType": "5", "stepType": "0", "enabled": "1",
        #                                       "verify": "", "smsVerify": "", "utf8encode": "", "failRetry": "",
        #                                       "retryCount": "1", "checkPoint": "", "tokenType": "0", "methodType": "1",
        #                                       "carrierType": "0", "sleepTime": "0", "buyfee": "0", "stepfun": "",
        #                                       "urlGetType": "", "recordType": "", "recordBegin": "",
        #                                       "recordDuration": "", "speech": "", "play": "", "callDuration": ""},
        #                                      {"stepNo": 6.0, "operateType": "2", "stepType": "0",
        #                                       "target": "text\u003d登录", "enabled": "1", "verify": "", "smsVerify": "",
        #                                       "utf8encode": "", "failRetry": "", "retryCount": "1", "checkPoint": "",
        #                                       "tokenType": "0", "methodType": "1", "carrierType": "0", "sleepTime": "0",
        #                                       "buyfee": "0", "stepfun": "", "urlGetType": "", "recordType": "",
        #                                       "recordBegin": "", "recordDuration": "", "speech": "", "play": "",
        #                                       "callDuration": ""}, {"stepNo": 6.1, "operateType": "21", "stepType": "0",
        #                                                             "target": "fix\u003d5", "enabled": "1",
        #                                                             "verify": "", "smsVerify": "", "utf8encode": "",
        #                                                             "failRetry": "", "retryCount": "1",
        #                                                             "checkPoint": "", "tokenType": "0",
        #                                                             "methodType": "1", "carrierType": "0",
        #                                                             "sleepTime": "0", "buyfee": "0", "stepfun": "",
        #                                                             "urlGetType": "", "recordType": "",
        #                                                             "recordBegin": "", "recordDuration": "",
        #                                                             "speech": "", "play": "", "callDuration": ""},
        #                                      {"stepNo": 7.0, "operateType": "3", "stepType": "0",
        #                                       "target": "resourceId\u003dcom.greenpoint.android.mc10086.activity:id/user_phoneno_edt",
        #                                       "postParam": "15859091580", "enabled": "1", "verify": "", "smsVerify": "",
        #                                       "utf8encode": "", "failRetry": "", "retryCount": "1", "checkPoint": "",
        #                                       "tokenType": "0", "methodType": "1", "carrierType": "0", "sleepTime": "0",
        #                                       "buyfee": "0", "stepfun": "", "urlGetType": "", "recordType": "",
        #                                       "recordBegin": "", "recordDuration": "", "speech": "", "play": "",
        #                                       "callDuration": ""}, {"stepNo": 8.0, "operateType": "45", "stepType": "0",
        #                                                             "target": "resourceId\u003dcom.greenpoint.android.mc10086.activity:id/user_login_smspassword_edt",
        #                                                             "postParam": "resourceId\u003dcom.greenpoint.android.mc10086.activity:id/login_checksms_btn#sms#",
        #                                                             "enabled": "1", "verify": "", "smsVerify": "",
        #                                                             "utf8encode": "", "failRetry": "",
        #                                                             "retryCount": "1", "checkPoint": "",
        #                                                             "tokenType": "0", "methodType": "1",
        #                                                             "carrierType": "0", "sleepTime": "0", "buyfee": "0",
        #                                                             "stepfun": "", "urlGetType": "", "recordType": "",
        #                                                             "recordBegin": "", "recordDuration": "",
        #                                                             "speech": "", "play": "", "callDuration": ""},
        #                                      {"stepNo": 9.0, "operateType": "2", "stepType": "0",
        #                                       "target": "resourceId\u003dcom.greenpoint.android.mc10086.activity:id/one_key_login_btn",
        #                                       "enabled": "1", "verify": "", "smsVerify": "", "utf8encode": "",
        #                                       "failRetry": "", "retryCount": "1", "checkPoint": "", "tokenType": "0",
        #                                       "methodType": "1", "carrierType": "0", "sleepTime": "0", "buyfee": "0",
        #                                       "stepfun": "", "urlGetType": "", "recordType": "", "recordBegin": "",
        #                                       "recordDuration": "", "speech": "", "play": "", "callDuration": ""},
        #                                      {"stepNo": 9.1, "operateType": "21", "stepType": "0",
        #                                       "target": "fix\u003d20", "enabled": "1", "verify": "", "smsVerify": "",
        #                                       "utf8encode": "", "failRetry": "", "retryCount": "1", "checkPoint": "",
        #                                       "tokenType": "0", "methodType": "1", "carrierType": "0", "sleepTime": "0",
        #                                       "buyfee": "0", "stepfun": "", "urlGetType": "", "recordType": "",
        #                                       "recordBegin": "", "recordDuration": "", "speech": "", "play": "",
        #                                       "callDuration": ""},
        #                                      {"stepNo": 10.0, "operateType": "2", "timerToken": "实时话费", "stepType": "0",
        #                                       "target": "text\u003d话费余额",
        #                                       "succstr1": "可用余额\u003e\u003e当月消费\u003e\u003e通话", "enabled": "1",
        #                                       "verify": "", "smsVerify": "", "utf8encode": "", "failRetry": "",
        #                                       "retryCount": "1", "checkPoint": "", "tokenType": "3", "methodType": "1",
        #                                       "carrierType": "0", "sleepTime": "0", "buyfee": "0", "stepfun": "",
        #                                       "urlGetType": "", "recordType": "", "recordBegin": "",
        #                                       "recordDuration": "", "speech": "", "play": "", "callDuration": ""},
        #                                      {"stepNo": 10.1, "operateType": "21", "stepType": "0",
        #                                       "target": "fix\u003d2", "enabled": "1", "verify": "", "smsVerify": "",
        #                                       "utf8encode": "", "failRetry": "", "retryCount": "1", "checkPoint": "",
        #                                       "tokenType": "0", "methodType": "1", "carrierType": "0", "sleepTime": "0",
        #                                       "buyfee": "0", "stepfun": "", "urlGetType": "", "recordType": "",
        #                                       "recordBegin": "", "recordDuration": "", "speech": "", "play": "",
        #                                       "callDuration": ""},
        #                                      {"stepNo": 12.0, "operateType": "49", "stepType": "0",
        #                                       "target": "com.greenpoint.android.mc10086.activity", "enabled": "1",
        #                                       "verify": "", "smsVerify": "", "utf8encode": "", "failRetry": "",
        #                                       "retryCount": "1", "checkPoint": "", "tokenType": "0", "methodType": "1",
        #                                       "carrierType": "0", "sleepTime": "0", "buyfee": "0", "stepfun": "",
        #                                       "urlGetType": "", "recordType": "", "recordBegin": "",
        #                                       "recordDuration": "", "speech": "", "play": "", "callDuration": ""}]},
        #                              "getSmskeyconfigs": [
        #                                  {"id": 4723, "carrier": "中国移动", "province": "广西", "brand": "全球通",
        #                                   "beforekeywords": "短信验证码是：", "afterkeywords": ",欢迎使用", "keywordslen": 6,
        #                                   "symbol": "+", "type": 5, "note": "集团APP登录", "channelname": "真机APP",
        #                                   "extType": 0},
        #                                  {"id": 5163, "carrier": "中国移动", "province": "广西", "brand": "全球通",
        #                                   "beforekeywords": "验证码:", "afterkeywords": "，有效时间", "keywordslen": 6,
        #                                   "symbol": "+", "type": 5, "note": "省APP详单", "channelname": "真机APP",
        #                                   "extType": 0},
        #                                  {"id": 8982, "carrier": "中国移动", "province": "广西", "brand": "全球通",
        #                                   "beforekeywords": "短信验证码:", "symbol": "+", "type": 5, "note": "省APP登录",
        #                                   "channelname": "真机APP", "extType": 0}]}}
        #     r_str = json.dumps(resp_content, ensure_ascii=False)
        # elif path == "/cdp/rphone/upResultLog":
        #     resp_content = {'code': '0'}
        #     r_str = json.dumps(resp_content, ensure_ascii=False)
        # elif path == "/cdp/sms/getSmsVerify":
        #     sms = str(input("输入验证码："))
        #     # 改为去数据库获取
        #     resp_content = {"code": "0", "msg": "", "appId": "", "respTime": "1562169223574", "data": {"sms": sms}}
        #     r_str = json.dumps(resp_content, ensure_ascii=False)
        # elif path == "/cdp/upVerify":
        #     verify = '123123'
        #     ## 使用execute方法执行SQL语句
        #     # self.cursor.execute("SELECT VERSION()")
        #     ## 使用 fetchone() 方法获取一条数据
        #     # data = self.cursor.fetchone()
        #     # print("Database version : %s " % data)

        #     self.cursor.execute(
        #         "INSERT INTO dzqd.sms_verify_info (verify, update_time) VALUE (" + verify + ", sysdate())")
        #     self.conn.commit()

        #     resp_content = {'code': '0'}
        #     r_str = json.dumps(resp_content, ensure_ascii=False)
        # elif path == "/pi/v1/user/loginByVCode":
        #     resp_content = {"content": {},"header": {"retCode": "0","retDateTime": "2018-12-11 09:41:59","retMsg": "请求成功","retSeq": "dc6ced79f11a11e8efc67e0c991f9cae"}}
        #     r_str = json.dumps(resp_content, ensure_ascii=False)
        # elif path == "/pi/v1/user/getVCode":
        #     resp_content = {"content": {},"header": {"retCode": "0","retDateTime": "2018-12-11 09:41:59","retMsg": "请求成功","retSeq": "dc6ced79f11a11e8efc67e0c991f9cae"}}
        #     r_str = json.dumps(resp_content, ensure_ascii=False)
        # else:
        #     r_str = '{"code": "-1","msg":"传入的url地址不符合"}'

        # if (path != "/cdp/taskexecute/getTask"):
        #     log.wlog("传入的url地址不符合！")
        #     r_str = '{"code": "-1","msg":"传入的url地址不符合"}'
        # else:
        #     # resp_content = {'code': '0'}
        #     resp_content = {"code":"0","msg":"","appId":"","respTime":"1561731895619","data":{"phoneNo":"18211194744","strategyId":"1546","groupId":"10018","tasksetId":"28526","tasksetInstanceName":"2019-06-28 22:11:05","channel":"32","testsrl":"235405144","pauseTime":0,"bamNormalModel":{"objectId":"754837","testType":"32","modelName":"咪咕视频监控","modeldesc":"复件-复件-null2017112114422020190628165847","runflow":"0","enabled":"1","remainTime":"","carrier":"中国移动","province":"北京","brand":"和4G","channel":"32","getValueType":"0","note":"","func":"0","isbalance":"0","balance":"0.0","testplatform":"咪咕视频","testsystem":"本地化探测","overtime":"0","bamNormalModelDetailParas":[{"stepNo":1.0,"operateType":"49","stepType":"0","describe":"com.cmcc.cmvideo","target":"com.cmcc.cmvideo","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":2.0,"operateType":"21","stepType":"0","describe":"等待","target":"fix\u003d6","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":3.0,"operateType":"43","stepType":"0","describe":"启动集团APP","target":"com.cmcc.cmvideo/com.cmcc.cmvideo.MainActivity","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":4.0,"operateType":"21","stepType":"0","describe":"等待","target":"fix\u003d12","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":9.0,"operateType":"5","timerToken":"视频","stepType":"0","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"3","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":12.0,"operateType":"21","stepType":"0","describe":"等待","target":"fix\u003d5","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":15.0,"operateType":"2","stepType":"0","describe":"元素点击","target":"text\u003d少年派","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":16.1,"operateType":"21","stepType":"0","describe":"点击登录","target":"fix\u003d5","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":20.0,"operateType":"80","stepType":"0","describe":"视频监控","target":"resourceId\u003dcom.cmcc.cmvideo:id/tv_current_time,resourceId\u003dcom.cmcc.cmvideo:id/tv_duration_time","postParam":"{\"beginDelayTime\":5000,\"beginErrorTime\":2,\"cycleTime\":30000,\"faultTolerantTime\":3000,\"taskCount\":30,\"taskErrorTime\":10}","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":24.0,"operateType":"21","stepType":"0","target":"fix\u003d5","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""},{"stepNo":28.0,"operateType":"49","stepType":"0","describe":"结束APP","target":"com.greenpoint.android.mc10086.activity","enabled":"1","verify":"","smsVerify":"","utf8encode":"","failRetry":"","retryCount":"1","checkPoint":"","tokenType":"0","methodType":"1","carrierType":"0","sleepTime":"0","buyfee":"0","stepfun":"","urlGetType":"","recordType":"","recordBegin":"","recordDuration":"","speech":"","play":"","callDuration":""}]},"getSmskeyconfigs":[{"id":5620,"carrier":"中国移动","province":"北京","brand":"全球通","beforekeywords":"随机码是：","afterkeywords":",欢迎使用","keywordslen":6,"symbol":"+","type":5,"note":"集团APP登录","channelname":"真机APP","extType":0}]}}
        #     r_str = json.dumps(resp_content,ensure_ascii=False)
        #     log.wlog("获取识别内容返回按键:" + r_str)
        #
        # enc = "UTF-8"
        # encoded = ''.join(r_str).encode(enc)
        # f = io.BytesIO()
        # f.write(encoded)
        # f.seek(0)
        # self.send_response(200)
        # self.send_header("Content-type", "text/html; charset=%s" % enc)
        # self.send_header("Content-Length", str(len(encoded)))
        # self.end_headers()
        # shutil.copyfileobj(f, self.wfile)


httpd = HTTPServer(('', 8090), MyHttpHandler)
print("httpServer started on 127.0.0.1,port 8090.....")
httpd.serve_forever()
